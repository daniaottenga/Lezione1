import mysql.connector


class DBConnect:
    # problema: gestisce una risorsa scarsa, sto creando diverse istanze di dbconnect
    # vorrei poter usare una sola istanza quindi aggiungo classmetod per dire ch ene puoi creare solo uno
    # così ho più controllo sull'uso di questa risorsa

    @classmethod
    def getConnection(self):

        try:
            cnx = mysql.connector.connect(
                user = 'root',
                password = 'rootroot',
                host = '127.0.0.1',
                database = "sw_gestionale"
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al db")
            print(err)
            return None