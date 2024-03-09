import PySimpleGUI as sg
import conversor
import os
import threading

def has_xml_files(folder_path):
    xml_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(".xml")]
    return len(xml_files) > 0, xml_files

def clear_fields(window):
    window["-FOLDER-"].update("")
    window["-MESSAGE-"].update("")
    window["-PROGRESS-"].update(0, 1)

def process_xml_files(folder_path, selected_files, filename, progress_bar, message_field):
    for xml_file in selected_files:
        arquivo_path = os.path.join(folder_path, xml_file)
        conversor.get_infos(arquivo_path)
        progress_bar.update(selected_files.index(xml_file) + 1)
        message_field.update(f"Processando arquivo: {xml_file}", text_color="blue")

    conversor.criar_tabela(filename)
    message_field.update("Arquivos XML processados com sucesso!", text_color="#32CD32")

layout = [
    [sg.Text("Conversor de NF-e XML para Planilha Excel", font=("Helvetica", 18), justification="center")],
    [sg.Text("Digite o caminho da pasta:"), sg.InputText(key="-FOLDER-"), sg.FolderBrowse(), sg.Button("Importar Arquivos")],
    [sg.Listbox(values=[], size=(40, 10), key="-FILES-", select_mode="multiple")],
    [sg.Text("Nome do arquivo (opcional):"), sg.InputText(key="-FILENAME-")],
    [sg.Text("", size=(40, 1), key="-MESSAGE-", text_color="green")],
    [sg.ProgressBar(1, orientation="h", size=(20, 20), key="-PROGRESS-")],
    [sg.Button("Converter"), sg.Button("Limpar"), sg.Button("Fechar")]
]

window = sg.Window("Conversor XML para Excel", layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Fechar":
        break
    elif event == "Importar Arquivos":
        folder_path = values["-FOLDER-"]
        if folder_path:
            has_files, files = has_xml_files(folder_path)
            window["-FILES-"].update(files)
            if has_files:
                window["-MESSAGE-"].update(f"{len(files)} arquivo(s) encontrado(s).", text_color="blue")
            else:
                window["-MESSAGE-"].update("Nenhum arquivo XML encontrado na pasta.", text_color="red")
        else:
            window["-MESSAGE-"].update("Escolha uma pasta que possua NF-e em formato XML.", text_color="red")
    elif event == "Converter":
        folder_path = values["-FOLDER-"]
        selected_files = values["-FILES-"]
        filename = values["-FILENAME-"].strip() or "notas_fiscais"

        if folder_path and selected_files:
            window["-MESSAGE-"].update("Processando arquivos XML...", text_color="blue")
            progress_bar = window["-PROGRESS-"]
            progress_bar.update(0, len(selected_files))

            thread = threading.Thread(target=process_xml_files, args=(folder_path, selected_files, filename, progress_bar, window["-MESSAGE-"]))
            thread.start()
        else:
            window["-MESSAGE-"].update("Selecione uma pasta e pelo menos um arquivo XML para converter.", text_color="red")
    elif event == "Limpar":
        clear_fields(window)

window.close()