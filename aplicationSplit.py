

import selenium
import shutil
import sqlite3
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from datetime import datetime
import re

#datab = sqlite3.connect('db/registroLeiloes.db')
#cursor = datab.cursor()
#try:
#    cursor.execute("CREATE TABLE cotacaoDolar(cotacao numeric)")
#except:
#    pass

s = HTMLSession()
userAgent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
link = "http://200.198.139.228/leiloeiros/busca/"
#requisicao = requests.get(link, headers=userAgent) # Faz requisicao do site usando um userAgent

requisicao = open("../Portal de Serviços - JUCISRS.html", 'r')
soup = str(BeautifulSoup(requisicao,'html.parser'))
#print(requisicaoResult.prettify())

## As infos estao separadas entre uma linha visual na tela, conhecida como <hr>, estou tentando separar tudo entre elas
# e assim trabalhar com as informacoes dentro dela, a matricula retira-se do texto

splitHRs = soup.split('<hr/>')

print(len(splitHRs))

for bloco in splitHRs:
    situacao = 0
    dataPosse =  0
    email = "Sem registro"
    preposto = "Nao registrado"
    cidade = ""
    if "(Cancelado)" in bloco:
        situacao = 1
    elif "(Suspenso)" in bloco:
        situacao = 2

    ##### Encontrar Nome
    inicio = bloco.find("-")
    fim = bloco.find('<',inicio)
    nome = bloco[inicio+1:fim]
    #####
    ##### Encontrar matricula
    inicio = bloco.find('<font color="#A01A14">')
    fim = bloco.find('</',inicio)
    matricula = bloco[inicio+22:fim]
    #####
    ##### Encontrar site
    if '<a href="' in bloco:
        inicio = bloco.find('<a href="')
        fim = bloco.find('" ',inicio)
        site = bloco[inicio+9:fim]
    else:
        site = "sem endereco"
    #####
    ##### Encontrar preposto
    if 'Preposto : ' in bloco:
        inicio = bloco.find('Preposto : ')
        fim = bloco.find('<',inicio)
        preposto = bloco[inicio+9:fim]
    #####
    ##### Encontrar email
    if 'e-Mail : ' in bloco:
        inicio = bloco.find('e-Mail : ')

        fim = bloco.find('<',inicio)
        email = bloco[inicio+8:fim]
    ##### Encontrar data
    strData = re.search(r'\d{2}/\d{2}/\d{4}',bloco)
    try:
        dataPosse = datetime.strptime(strData.group(), '%d/%m/%Y').date()
    except:
        pass
    ########
    ##### Encontrar cidade
    if ' - RS' in bloco:
        inicio = bloco.find(' - RS')
        fim = bloco.find('<b>')
        cidade = bloco[fim-8:inicio]


    bloco.find(' ah ze da manga')


    print("*******************~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`***********************************")
    print(nome)
    print('-')
    print(matricula)
    print('-')
    print(site)
    print('-')
    print(dataPosse)
    print(email)
    print(preposto)
    #print(bloco.strip())
    print(situacao)
    print(cidade)
    print("******************************************************")



#cursor.execute('INSERT INTO cotacaoDolar VALUES({})'.format(value_))

#datab.commit()
#cursor.execute("select * from cotacaoDolar")
#print(cursor.fetchall())