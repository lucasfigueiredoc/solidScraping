
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from datetime import datetime
from Dependencias.dbF import *
#mport selenium
#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
createTable()
options = Options()
import os

#drive = webdriver.Chrome('chromedriver.')
#drive.get('http://200.198.139.228/leiloeiros/busca/')
#time.sleep(5)

s = HTMLSession()
userAgent = \
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
link = "http://200.198.139.228/leiloeiros/busca/"
# requisicao = requests.get(link, headers=userAgent) # Faz requisicao do site usando um userAgent

requisicao = open("Dependencias/Portal de Serviços - JUCISRS.html", 'r')
soup = str(BeautifulSoup(requisicao, 'html.parser'))
# print(requisicaoResult.prettify())

## As infos estao separadas entre uma linha visual na tela, conhecida como <hr>, estou tentando separar tudo entre elas
# e assim trabalhar com as informacoes dentro dela, a matricula retira-se do texto

splitHRs = soup.split('<hr/>')
cont = 0
print(len(splitHRs))

for x in range(4, len(splitHRs) - 2):

    bloco = splitHRs[x]
    dataPosse = ""
    dataTxt = ""
    endereco = "Endereco sem registro"
    telefone = "Sem registro"
    email = "Sem registro"
    preposto = "Não registrado"
    cidade = "Não registrado"

    situacao = "Ativo(a)"
    if "(Cancelado)" in bloco:
        situacao = "Cancelado"
    elif "(Suspenso)" in bloco:
        situacao = "Suspenso"

    ############## Encontrar Nome
    inicio = bloco.find("-")
    fim = bloco.find('<', inicio)
    nome = bloco[inicio + 1:fim]
    # %
    ############# Encontrar matricula
    inicio = bloco.find('<font color="#A01A14">')
    fim = bloco.find('</', inicio)
    matricula = bloco[inicio + 22:fim]
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
    strData = re.search(r'\d{2}/\d{2}/\d{4}', bloco)
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

    ############# Encontrar cidade
    padrao = r"<br/>\s*(.*?) - RS"
    if ' - RS' in bloco:
        correspondencia = re.search(padrao, bloco)
        if correspondencia:
            palavra_anterior = correspondencia.group(1)
            cidade = palavra_anterior.replace('<b>', '')
        else:
            print("Cidade nao encontrada")
            cidade = " nulo "
    # %
    ########### Encontrar telefone
    if 'Telefone : ' in bloco:
        inicio = bloco.find('Telefone : ')
        fim = bloco.find('<br/>', inicio)
        telefone = bloco[inicio + 10:fim].strip()
    bloco.find(' ah ze da manga')
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
    print(endereco)
    print("******************************************************")

    try:
        input(nome, matricula, site, dataPosse, email, preposto, situacao, cidade, telefone, endereco)
        print("comitado")
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        print("Por algum motivo nao ocorreu commit")

