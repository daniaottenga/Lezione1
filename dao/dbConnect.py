import pathlib
import mysql.connector

class DBConnect:
    # problema: gestisce una risorsa scarsa, sto creando diverse istanze di dbconnect
    # vorrei poter usare una sola istanza quindi aggiungo classmethod per dire ch ene puoi creare solo uno
    # così ho più controllo sull'uso di questa risorsa

    _mypool = None # il pool di connessioni velocizza la connessione, centralizzo il controllore delle connessioni

    def __init__(self): # impedisce al chiamante di creare un'istanza della classe, gli imponiamo di usare
        # get connection e non db connect, questo per il pattern singleton
        raise RuntimeError("Attenzione! Non devi creare un'istanza di questa classe. Usa i metodi di classe")

    # FUNZIONE SEMPRE GIA' DATA ALL'ESAME
    @classmethod
    def getConnection(cls): # cls funziona come self ma indica che è un attributo della classe, non dell'istanza
        if cls._mypool is None: # si chiede se la connessione già esiste
            try: # allora crea la connessione
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size = 3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg" # recuperiamo il
                    # path del nostro file con la libreria pathlib
                    # fino a resolve ci dice che lo voglio da questo file
                    # parent mi dice che voglio questa cartella
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None

        else: # se il pool già esiste restituisco direttamente la connessione
            return cls._myPool.get_connection()