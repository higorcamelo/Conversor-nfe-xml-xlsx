import xmltodict
import os
import json


def get_infos(arquivo):
    with open(arquivo,'rb') as arquivo_xml:
        dict_arquivo = xmltodict.parse(arquivo_xml.read())
        
        try:
            if 'NFe' in dict_arquivo:
                infos_nfe = dict_arquivo['NFe']['infNFe']
            else:
                infos_nfe = dict_arquivo['nfeProc']['NFe']['infNFe'] #Ajuste para suportar a NFE 4.0
                
            num_nota = infos_nfe['@Id']
            nome_emit = infos_nfe['emit']['xNome']
            nome_dest = infos_nfe['dest']['xNome']
            
            endereco_dest = infos_nfe['dest']['enderDest']
            lgr_nro_dest = endereco_dest['xLgr'] + ', ' + endereco_dest['nro']
            mun_uf_dest = endereco_dest['xMun'] + ' - ' + endereco_dest['UF']
            
            tributos = infos_nfe['total']['ICMSTot']
            val_prod = tributos['vProd']
            val_icms = tributos['vICMS']
            val_pis = tributos['vPIS']
            val_cofins = tributos['vCOFINS']
            
            peso_produto = infos_nfe['transp']['vol']['pesoB']
        except Exception as excep:
            print(excep)
            print(json.dumps(dict_arquivo, indent= 4))

            
        print(num_nota, nome_emit, nome_dest, lgr_nro_dest, mun_uf_dest, peso_produto, val_prod, val_icms, val_pis, val_cofins, sep='\n')
