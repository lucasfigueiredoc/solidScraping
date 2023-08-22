

import selenium
import shutil
import sqlite3
import requests
from bs4 import BeautifulSoup
from Dependencias import functionScrap

import datetime
#datab = sqlite3.connect('db/registroLeiloes.db')
#cursor = datab.cursor()
#try:
#    cursor.execute("CREATE TABLE cotacaoDolar(cotacao numeric)")
#except:
#    pass


userAgent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
link = "http://200.198.139.228/leiloeiros/busca/listar"

###### valores
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
motivoCancelamento = " "

requisicao = requests.get(link, headers=userAgent) # Faz requisicao do site usando um userAgent

site = BeautifulSoup(requisicao.text,"html.parser") # 'Parseia' o html e transforma a requisicao em texto para comecar a trabalhar em cima das informacoes.
print(site.prettify())

leiloeiros = site.findAll('b')
print(leiloeiros)










#cursor.execute('INSERT INTO cotacaoDolar VALUES({})'.format(value_))

#datab.commit()
#cursor.execute("select * from cotacaoDolar")
#print(cursor.fetchall())