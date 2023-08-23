

import selenium
import shutil
import sqlite3
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

import datetime
#datab = sqlite3.connect('db/registroLeiloes.db')
#cursor = datab.cursor()
#try:
#    cursor.execute("CREATE TABLE cotacaoDolar(cotacao numeric)")
#except:
#    pass


###### Variavies que servirao ao db
#matricula = ""
nome = " "
situacao = 0
endereco = " "
cep = " "
cidade = " "
#posse = datetime.now()
email = " "
telefone = " "
preposto = " "
atoCancelamento = " "
motivoCancelamento = " "

cont = 0

s = HTMLSession()
userAgent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
link = "http://200.198.139.228/leiloeiros/busca/"
#requisicao = requests.get(link, headers=userAgent) # Faz requisicao do site usando um userAgent

requisicao = open("../Portal de Serviços - JUCISRS.html", 'r')
soup = BeautifulSoup(requisicao,'html.parser')
#print(requisicaoResult.prettify())

## As infos estao separadas entre uma linha visual na tela, conhecida como <hr>, estou tentando separar tudo entre elas
# e assim trabalhar com as informacoes dentro dela, a matricula retira-se do texto

tagHRs = str(soup.findAll('hr'))

#print(tagB)
listaDeEntradas = []
for hr in tagHRs:
    href = "Sem link"
    hr = hr.find_next()
    #print(hr)
    for a in hr.findAll('a', href=True):
        if a:
            href = a['href']
        else:
            href = "Sem link"

    situacao = 0

    hrFont = hr.findAll('font')
    hrBolt = hr.findAll('b')

    for font in hrFont:

        if font:

            matricula = font.text.strip()
            nome = font.next_sibling.strip().replace("- ", "")

            if "(Cancelado)" in matricula:
                matricula.replace("(Cancelado)", "")
                nome.replace("(Cancelado)", "")
                situacao = 1
            elif "(Suspenso)" in matricula:
                matricula.replace("(Suspenso)", "")
                nome.replace("(Suspenso)", "")
                situacao = 2

            # print("   ``   ")
            print("Nome: ", nome)
            print("Matricula : ",matricula)
            print("situacao : ",situacao)
            # print("   ``   ")
            print(href)

    bold_tags = soup.find_all('b')


    try:
        texto = hr.find_next().get_text(strip=True)
    except:
        pass
    listaDeEntradas.append(texto)

# Print the extracted text entries
for entrada in listaDeEntradas:
    #print(entrada)
    pass
#leiloeirosLista = site.findAll("option")
#for x in leiloeirosLista:
#    print(x)










#cursor.execute('INSERT INTO cotacaoDolar VALUES({})'.format(value_))

#datab.commit()
#cursor.execute("select * from cotacaoDolar")
#print(cursor.fetchall())