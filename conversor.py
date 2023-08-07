import xmltodict
import os
import pandas as pd

def get_infos(arquivo):
    with open(arquivo, 'rb') as arquivo_xml:
        dict_arquivo = xmltodict.parse(arquivo_xml.read())
            
        try:
            if 'NFe' in dict_arquivo:
                infos_nfe = dict_arquivo['NFe']['infNFe']
            else:
                infos_nfe = dict_arquivo['nfeProc']['NFe']['infNFe']  # Ajuste para suportar a NFE 3.0
                    
            num_nota = infos_nfe.get('@Id', 'N/A')
            nome_emit = infos_nfe.get('emit', {}).get('xNome', 'N/A')
            nome_dest = infos_nfe.get('dest', {}).get('xNome', 'N/A')
                
            endereco_dest = infos_nfe.get('dest', {}).get('enderDest', {})
            lgr_nro_dest = f"{endereco_dest.get('xLgr', 'N/A')}, {endereco_dest.get('nro', 'N/A')}"
            mun_uf_dest = f"{endereco_dest.get('xMun', 'N/A')} - {endereco_dest.get('UF', 'N/A')}"
                
            tributos = infos_nfe.get('total', {}).get('ICMSTot', {})
            val_prod = tributos.get('vProd', 'N/A')
            val_icms = tributos.get('vICMS', 'N/A')
            val_pis = tributos.get('vPIS', 'N/A')
            val_cofins = tributos.get('vCOFINS', 'N/A')
                
            peso_produto = infos_nfe.get('transp', {}).get('vol', {}).get('pesoB', 'N/A')

            # Formatação de valores numéricos e monetários
            val_prod = format(float(val_prod), '.2f')
            val_icms = format(float(val_icms), '.2f')
            val_pis = format(float(val_pis), '.2f')
            val_cofins = format(float(val_cofins), '.2f')
            
            valores_cell.append([num_nota, nome_emit, nome_dest, lgr_nro_dest, mun_uf_dest, 
                                 val_prod, val_icms, val_pis, val_cofins, peso_produto])
            

        except Exception as excep:
            error_msg = f"Erro ao processar arquivo {arquivo}: {excep}"
            logging.error(error_msg)
            print(error_msg)
                
                
valores_cell = []

def criar_tabela():
    colunas = ['Nº Nota','Emissor','Destinatário', 'Logradouro', 'Cidade', 'Val. Produto',
               'Val. ICMS', 'Val. PIS', 'val. COFINS', 'Peso Bruto']
    
    tabela = pd.DataFrame(columns=colunas, data=valores_cell)
    nome_arquivo = 'notas_fiscais.xlsx'
    
    # Verifica se o arquivo já existe
    if os.path.isfile(nome_arquivo):
        num_arquivo = 1
        while os.path.isfile(f'notas_fiscais_{num_arquivo}.xlsx'):
            num_arquivo += 1
        nome_arquivo = f'notas_fiscais_{num_arquivo}.xlsx'
    
    tabela.to_excel(nome_arquivo, index=False)
    print(f"Arquivo {nome_arquivo} criado com sucesso!")

