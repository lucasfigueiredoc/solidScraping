
from bs4 import BeautifulSoup
from datetime import datetime
from Dependencias.dbF import *
import re

createTable() ## função para criar tabela onde serão registrados os leiloeiros
requisicao = open("Dependencias/Portal de Serviços - JUCISRS.html", 'r') ## leitura do arquivo que vai ser raspado
soup = str(BeautifulSoup(requisicao, 'html.parser')) ## o converto para str,
# print(requisicaoResult.prettify())

splitHRs = soup.split('<hr/>') ## separo todas as <hr> encontradas, entre as elas se encontra as infos dos leiloeiros

for x in range(4, len(splitHRs) - 2): ## A partir do hr 4 e até o antepenúltimo ficam as informações que preciso, os outros fazem parte da estilização do site.

    ##Variáveis que precisam ser inicializadas e reiniciadas com valores padrão antes de cada ciclo.
    bloco = splitHRs[x] ###### Bloco se refere a parte do código onde se renderiza as informações de cada leiloeiro
    dataPosse = ""
    dataTxt = ""
    endereco = "Endereço não registrado"
    telefone = "Sem registro"
    email = "Sem registro"
    preposto = "Não registrado"
    cidade = "Não registrado"
    situacao = "Ativo(a)"
    motivo = "Não foi cancelado"


    #### Com cada bloco transformado em str, se inicia o fatiamento utilizando referências em que se precede cada dado específico

    ############## Encontrar Nome
    inicio = bloco.find("-") ## cada nome é precedido de um ifem
    fim = bloco.find('<', inicio)
    nome = bloco[inicio + 1:fim]
    # %

    ############# Encontrar matricula
    inicio = bloco.find('<font color="#A01A14">') ## matricula precedida por esta estrutura css
    fim = bloco.find('</', inicio)
    matricula = bloco[inicio + 22:fim]
    # %

    ##### Verifica situação no bloco atual
    if "(Cancelado)" in bloco:
        situacao = "Cancelado"
    elif "(Suspenso)" in bloco:
        situacao = "Suspenso"
    # %

    ############# Motivo do cancelamento
    if 'Motivo do Cancelamento: ' in bloco:
        inicio = bloco.find('Motivo do Cancelamento: ')
        fim = bloco.find('')
        motivo = bloco[inicio+23:]
    # %

    ############# Encontrar site
    if '<a href="' in bloco:
        inicio = bloco.find('<a href="')
        fim = bloco.find('" ', inicio)
        site = bloco[inicio + 9:fim]
    else:
        site = "sem endereco"
    # %

    ############# Encontrar preposto
    if 'Preposto : ' in bloco:
        inicio = bloco.find('Preposto : ')
        fim = bloco.find('<', inicio)
        preposto = bloco[inicio + 9:fim]
    # %

    ############# Encontrar email
    if 'e-Mail : ' in bloco:
        inicio = bloco.find('e-Mail : ')
        fim = bloco.find('<', inicio)
        email = bloco[inicio + 8:fim]
    # %

    ############# Encontrar data
    strData = re.search(r'\d{2}/\d{2}/\d{4}', bloco) ### estrutura regular do formato de data
    try:
        dataPosse = datetime.strptime(strData.group(), '%d/%m/%Y').date()
        dataTxt = dataPosse.strftime('%d/%m/%Y')
    except:
        pass
    # %

    ############# Encontrar endereco
    varEndereco = str(dataTxt + '<br/>')
    if varEndereco in bloco:
        inicio = bloco.find(varEndereco)
        fim = bloco.find('</b>', inicio)
        endereco = bloco[inicio + 14:fim]
        if "<a href=" in endereco:
            endereco = "Endereço não registrado"
    # %

    ############# Encontrar cidade
    padrao = r"<br/>\s*(.*?) - RS"
    if ' - RS' in bloco:
        correspondencia = re.search(padrao, bloco)
        if correspondencia:
            palavra_anterior = correspondencia.group(1)
            cidade = palavra_anterior.replace('<b>', '')
        else:
            print("Cidade nao encontrada")
            cidade = " Sem registro "
    # %

    ########### Encontrar telefone
    if 'Telefone : ' in bloco:
        inicio = bloco.find('Telefone : ')
        fim = bloco.find('<br/>', inicio)
        telefone = bloco[inicio + 10:fim].strip()
    # %

    print("Nome: ", nome)
    print("Matricula: ", matricula)
    print("Site: ", site)
    print("Data: ", dataTxt)
    print("Email: ", email)
    print("Preposto: ", preposto)
    print("Situação: ", situacao)
    print("Cidade: ", cidade)
    print("telefone: ", telefone)
    print("Endereço :",endereco)
    print("Motivo: ", motivo)
    print("******************************************************")

    try:
        input(nome, matricula, site, dataPosse, email, preposto, situacao, motivo, cidade, telefone, endereco.replace('>',''))
        print("comitado")
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
