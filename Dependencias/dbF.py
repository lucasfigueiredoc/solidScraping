import sqlite3


datab = sqlite3.connect('db/registroLeiloes.db')
cursor = datab.cursor()
def createTable():

    try:
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS leiloeiros(
                nome TEXT,
                matricula INTEGER,
                site TEXT,
                data DATE,
                email TEXT,
                preposto TEXT,
                situacao TEXT,
                cidade TEXT,
                telefone TEXT,
                endereco TEXT
            );

                    """)
    except:
        pass

def input(nome, matricula, site, dataPosse, email, preposto, situacao, cidade, telefone, endereco):
    query = "INSERT INTO leiloeiros(nome, matricula, site, data, email, preposto, situacao, cidade, telefone, endereco) VALUES ('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(nome, matricula, site, dataPosse, email, preposto, situacao, cidade, telefone, endereco)
    cursor.execute(query)
    datab.commit()