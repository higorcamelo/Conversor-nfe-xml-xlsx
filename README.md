# Conversor de NF-e XML para Planilha Excel

Este é um sistema simples desenvolvido em Python que permite a conversão dos principais valores de Notas Fiscais Eletrônicas (NF-e) em um arquivo de planilha Excel (.xlsx). A conversão inclui informações como número da nota, emissor, destinatário, valores monetários, entre outros.

## Funcionalidades

- Processa arquivos XML de NF-e para extrair informações relevantes.
- Gera uma planilha Excel contendo os valores extraídos.
- Oferece uma interface gráfica de usuário (GUI) para facilitar a interação.
 
## Recursos Adicionais

- Tratamento de erros detalhado com registro em arquivo de log (`errors.log`).
- Feedback visual na interface para melhor compreensão do progresso.
- Barra de progresso para indicar o andamento do processamento.
- Responsividade da interface permitindo redimensionamento da janela.

## Tecnologias e Bibliotecas Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias e bibliotecas:

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.
- **PySimpleGUI**: Biblioteca para criar interfaces gráficas de usuário (GUI) de forma rápida e intuitiva.
- **xmltodict**: Biblioteca para análise de arquivos XML de forma mais conveniente.
- **pandas**: Biblioteca para manipulação e análise de dados, utilizada para criar a planilha Excel.
- **openpyxl**: Biblioteca para trabalhar com arquivos Excel.
- **cx-Freeze**: Ferramenta utilizada para empacotar o código Python em um executável (.exe).

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
