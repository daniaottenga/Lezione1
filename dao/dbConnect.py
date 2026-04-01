import pathlib

import mysql.connector


class DBConnect:
    # problema: gestisce una risorsa scarsa, sto creando diverse istanze di dbconnect
    # vorrei poter usare una sola istanza quindi aggiungo classmetod per dire ch ene puoi creare solo uno
    # così ho più controllo sull'uso di questa risorsa

    _mypool = None

    def __init__(self):
        raise RuntimeError("Attenzione! Non devi creare un0istanza di questa classe. Usa i metodi classe")

    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size = 3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None

        else: # se il pool già esiste restituisco direttamente la connessione
            return cls._myPool.get_connection()