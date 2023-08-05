import xmltodict
import os


def get_infos(arquivo):
    with open(arquivo,'rb') as arquivo_xml:
        dict_arquivo = xmltodict.parse(arquivo_xml.read())
        print(dict_arquivo)
