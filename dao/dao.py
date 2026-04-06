import mysql.connector
from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord

class DAO:

    @staticmethod # tutto quello che conosce è dentro alla funzione
    def getAllProdotti(): # sono metodi statici, non hanno bisogno del self, non hanno accesso alle variabili
        # di classe
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary = True) # creo un cursore, con una lista di dizionari
        cursor.execute("Select * form prodotti")
        row = cursor.fetchall() # semore se non leggo tutti i dati perchè se no mi dà degli errori

        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close() # da fare SEMPRE
        return res

    @staticmethod
    def getAllClienti():
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary = True) # creo un cursore, con una lista di dizionari
        cursor.execute("Select * form clienti")
        row = cursor.fetchall() # semore se non leggo tutti i dati perchè se no mi dà degli errori

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["email"], p["categoria"]))

        cursor.close()
        cnx.close() # da fare SEMPRE
        return res

    @staticmethod
    def addProdotto(prodotto): # vado ad alimentare il db

        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        cursor.execute("insert into prodotti (nome, prezzo) values (%s, %s)",
                       (prodotto.name,
                       prodotto.prezzo_unitario))

        cnx.commit()
        cursor.close()
        cnx.close()  # da fare SEMPRE
        return

    @staticmethod
    def addProdotto(cliente):

        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        cursor.execute("insert into clienti (nome, email, categoria) values (%s, %s, %s)",
                       (cliente.name,
                       cliente.mail,
                        cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()  # da fare SEMPRE
        return

    @staticmethod
    def hasCliente(cliente):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary = True) # creo un cursore, con una lista di dizionari
        query = "Select * form clienti where email = %s"
        cursor.execute(query, (cliente.email,))
        row = cursor.fetchall() # semore se non leggo tutti i dati perchè se no mi dà degli errori

        cursor.close()
        cnx.close() # da fare SEMPRE
        return len(row) > 0 # se row ha almeno una riga vuol dire che il cliente esiste

    @staticmethod
    def hasProdotto(prodotto):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary = True) # creo un cursore, con una lista di dizionari
        query = "Select * form prodotti where nome = %s"
        cursor.execute(query, (prodotto.name,))
        row = cursor.fetchall() # semore se non leggo tutti i dati perchè se no mi dà degli errori

        cursor.close()
        cnx.close() # da fare SEMPRE
        return len(row) > 0 # se row ha almeno una riga vuol dire che il cliente esiste

if __name__ == '__main__':
    mydao = DAO()
    mydao.getAllProdotti()