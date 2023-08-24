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
                posse DATE,
                email TEXT,
                preposto TEXT,
                situacao TEXT,
                motivo TEXT,
                cidade TEXT,
                telefone TEXT,
                endereco TEXT
                
            );

                    """)
    except:
        pass

def input(nome, matricula, site, dataPosse, email, preposto, situacao, motivo, cidade, telefone, endereco):
    query = "INSERT INTO leiloeiros(nome, matricula, site, posse, email, preposto, situacao, motivo, cidade, telefone, endereco) VALUES ('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(nome, matricula, site, dataPosse, email, preposto, situacao, motivo, cidade, telefone, endereco)
    cursor.execute(query)
    datab.commit()