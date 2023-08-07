import PySimpleGUI as sg
import conversor
import os
import threading

lista_arquivos = []

def has_xml_files(folder_path):
    xml_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(".xml")]
    lista_arquivos.extend(xml_files)
    return len(xml_files) > 0

layout = [
    [sg.Text("Converter Arquivos XML", font=("Helvetica", 18), justification="center")],
    [sg.Text("Digite o caminho da pasta:"), sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("", size=(40, 1), key="-MESSAGE-", text_color="green")],
    [sg.ProgressBar(1, orientation="h", size=(20, 20), key="-PROGRESS-")],
    [sg.Button("Converter"), sg.Button("Limpar"), sg.Button("Fechar")]
]

window = sg.Window("Conversor XML para Excel", layout, resizable=True)

def clear_fields():
    window["-FOLDER-"].update("")
    window["-MESSAGE-"].update("")
    window["-PROGRESS-"].update(0)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Fechar":
        break
    elif event == "Converter":
        folder_path = values["-FOLDER-"]
        if folder_path:
            if has_xml_files(folder_path):
                window["-MESSAGE-"].update("Processando arquivos XML...", text_color="blue")
                progress_bar = window["-PROGRESS-"]
                progress_bar.update_bar(0, 1)
                
                def process_xml_files():
                    for xml_file in lista_arquivos:
                        arquivo_path = os.path.join(folder_path, xml_file)
                        conversor.get_infos(arquivo_path)
                        progress_bar.update_bar(lista_arquivos.index(xml_file) + 1, len(lista_arquivos))
                    
                    conversor.criar_tabela()
                    window["-MESSAGE-"].update("Arquivos XML processados com sucesso!", text_color="green")

                thread = threading.Thread(target=process_xml_files)
                thread.start()
            else:
                window["-MESSAGE-"].update("Nenhum arquivo XML na pasta.", text_color="red")
        else:
            window["-MESSAGE-"].update("Escolha uma pasta que possua NF-e em formato XML.", text_color="red")

    elif event == "Limpar":
        clear_fields()

window.close()
