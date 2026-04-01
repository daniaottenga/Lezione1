import random
from collections import deque, Counter, defaultdict
from dao.dao import DAO
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

""" 
Scrivere un software gestionale che abbia le seguenti funzionalità:
1. Supportare l'arrivo e la gestione di oridni
1bis. Quando arriva un nuovo ordine lo aggiungo ad una coda assicurandomi che sia eseguita solo dopo gli altri
2. Avere delle funzionalità per avere statistiche sugli ordini
3. Fornire statistiche sulla distribuzione di ordini per la categoria cliente
"""

class GestoreOrdini:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = [] # non mi importa delll'ordinamento
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list) # le chiavi sono le categorie, i valori gli ordini
        self._dao = DAO()
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self): # leggo prodotti e clienti da db e creo ordini randomici per testare l'app
        self._allP.extend(self._dao.getAllProdotti()) # così se c'era altro lo mantiene
        self._allC.extend(self._dao.getAllClienti())

        for i in range(10):
            indexP = random.randint(0, len(self._allP) - 1)
            indexC = random.randint(0, len(self._allC) - 1)
            ordine = Ordine([RigaOrdine(self._allP[indexP], random.randint(1, 5))],
                            self._allC[indexC])
            self.add_ordine(ordine)

    def add_ordine(self, ordine: Ordine):
        # Aggiunge un nuovo ordine agli elementi da gestire
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Oridni ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine(self, nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC):
        prod = ProdottoRecord(nomeP, prezzoP)
        cliente = ClienteRecord(nomeC, mailC, categoriaC)

        self._update_DB(prod, cliente)
        return Ordine([RigaOrdine(prod, quantitaP)], cliente)

    def _update_DB(self, prod, cliente):
        if not self._dao.hasProdotto(prod):
            self._dao.addProdotto(prod)

        if not self._dao.hasCliente(cliente):
            self._dao.addCliente(cliente)

    def processa_prossimo_ordine(self):
        # Legge il prossimo ordine in coda e lo gestisce, aggiorna le variabili private di questa classe

        print("\n" + "-" * 60)
        print("\n" + "-" * 60)

        if not self._ordini_da_processare: # se è vuoto
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("", "", "")) # posso fare return di più cose assieme

        ordine = self._ordini_da_processare.popleft() # logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        # su tutte le righe del mio ordine, per ognuna vado ad aggiornare la mia
        # collection di statistiche sui prodotti venduti, è un counter con una losta di stringhe (nomi del
        # prodotto) e mi dirà quante volte sarà venduto quel prodotto
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        # raggruppo gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        # archiviamo l'ordine
        self._ordini_processati.append(ordine)
        print("Ordine correttamente processato")
        return True, ordine

    def processa_tutti_ordini(self):
        # processa tutti gli ordini attualmente presenti in coda

        print("\n" + "-" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        ordini = []
        while self._ordini_da_processare:
            _, ordine = self.processa_prossimo_ordine() # l'underscore mi dà una variabile che non userò
            ordini.append(ordine)
        print("Tutti gli ordini sono stati processati")
        return ordini

    def get_statistiche_prodotti(self, top_n: int = 5):
        # Questo metodo restituisce info su quante unità sono state vendute di un certo prodotto

        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n): # mi restituisce i 5 oggetti +
            # venduti
            valori.append((prodotto, quantita)) # fa una lista di tuple
        return valori

    def get_distribuzione_categorie(self):
        valori = []
        for cat in self._ordini_per_categoria.keys(): # va a leggere tutte le chiavi
            ordini = self._ordini_per_categoria[cat] # va a recuperare la lista degli ordini per categoria
            totale_fatturato = sum([o.totale_lordo(0.22) for o in ordini]) # da la somma del totale lordo per ogni ordine
            valori.append((cat, totale_fatturato)) # lo aggiungo ad una lista con tupla(categoria, fatturato)
        return valori

    def stampa_riepilogo(self):
        # stampa info di massima
        print("\n" + "=" * 60)
        print("Stato attuale del business:")
        print(f"Oridni correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Oridni in coda: {len(self._ordini_da_processare)}")

        print("Prodotti + venduti:")
        for prod, quantita in self.get_statistiche_prodotti(): # che dà una lista di tuple
            print(f"{prod}: {quantita}")

        print("Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat}: {fatturato}")

    def get_riepilogo(self):
        # restituisce una stringa con le info di massima
        sommario = ""
        sommario += "\n" + "=" * 60
        sommario += f"Oridni correttamente gestiti: {len(self._ordini_processati)}"
        sommario += f"Oridni in coda: {len(self._ordini_da_processare)}"

        sommario += "Prodotti + venduti:"
        for prod, quantita in self.get_statistiche_prodotti(): # che dà una lista di tuple
            sommario += f"{prod}: {quantita}"

        sommario += "Fatturato per categoria:"
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario += f"{cat}: {fatturato}"
        return sommario

def test_modulo():
    sistema = GestoreOrdini() # crea un'istanza della classe
    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("Mario Rossi", "mario@gmail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 2),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)
        ], ClienteRecord("Fulvio Bianchi", "bianchi@gmail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
        ], ClienteRecord("Giuseppe Averta", "averta@gmail.it", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 3),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 5),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
        ], ClienteRecord("Carlo Masone", "masone@gmail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Tablet", 500.0), 2),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)
        ], ClienteRecord("Francesca Pistilli", "pistilli@gmail.it", "Bronze")),
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()
    sistema.stampa_riepilogo()


if __name__ == "__main__":
    test_modulo()