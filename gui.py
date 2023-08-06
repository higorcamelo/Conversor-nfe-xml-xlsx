import PySimpleGUI as sg
import conversor
import os

lista_arquivos = []

def has_xml_files(folder_path):
    xml_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(".xml")]
    lista_arquivos.extend(xml_files)
    return len(xml_files) > 0

layout = [
    [sg.Text("Digite o caminho da pasta:")],
    [sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("", size=(40, 1), key="-MESSAGE-")],
    [sg.Button("Converter")]
]

window = sg.Window("Converter Arquivos XML", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Converter":
        folder_path = values["-FOLDER-"]
        if folder_path:
            if has_xml_files(folder_path):
                for xml_file in lista_arquivos:
                    arquivo_path = os.path.join(folder_path, xml_file)
                    conversor.get_infos(arquivo_path)
                window["-MESSAGE-"].update(f"Arquivos XML encontrados na pasta! {lista_arquivos}")
            else:
                window["-MESSAGE-"].update("Nenhum arquivo XML na pasta.")

window.close()
