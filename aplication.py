

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
matricula = 0
nome = " "
situacao = False
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


listaElementos = soup.find_all('b')
for elemento in listaElementos:
    elementFont = elemento.findAll('font')
    for font in elementFont:
        if font:
            entry_number = font.text.strip()
            try:
                name = font.next_sibling.strip()# Extract name
            except:
                name =  " "
                pass
            # Print or process the extracted information
            ##print("Name:", name)
            #print("**     \n\n    **")
    elementBr = elemento.findAll('br')
    cont = 0
    for br in elementBr:

        if br:

            cidade = br.next_sibling.strip()

            print(cidade)
#leiloeirosLista = site.findAll("option")
#for x in leiloeirosLista:
#    print(x)










#cursor.execute('INSERT INTO cotacaoDolar VALUES({})'.format(value_))

#datab.commit()
#cursor.execute("select * from cotacaoDolar")
#print(cursor.fetchall())