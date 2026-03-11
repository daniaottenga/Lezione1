import copy
from collections import Counter

from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


# LISTE


p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello")
for i, p in enumerate(carrello): # restituisce una lista di tuple con indice e elemento stesso
    print(f"{i + 1}) {p.name} - {p.prezzo_unitario}")

# Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario) # sort per prezzo unitario
print("Prodotti nel carrello ordinati per prezzo")
for i, p in enumerate(carrello): # restituisce una lista di tuple con indice e elemento stesso
    print(f"{i + 1}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello) # cicla sul carrello facendo la somma
print(f"Totale del carrello: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Prodotto", 100.0)) # aggiunge un solo elemento in coda
carrello.extend([ProdottoRecord("aaa", 50.0), ProdottoRecord("bbb", 60.0)]) # agggiunge una lista di elementi
carrello.insert(2, ProdottoRecord("ccc", 40.0)) # aggiunge alla posizione specifica

# Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) # rimuove il prodotto specifico, scorre tutta la lista, cerca p1 e lo toglie
# carrello.clear() # toglie tutto

# Sorting
# carrello.sort() # ordina, deve avere il metodo __lt__ per farlo
# carrello.sort(reverse = True) # al contrario
# carrello.sort(key = function) # ordina seguendo una funzione
# carrello_ordinato = sorted(carrello) # prende carrello, lo riordina e gli cambia nome creando una seconda lista

carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # crea una nuova lista e ci va a mettere dentro gli stessi elementi della lista
# di partenza, se modifico carrello, modifico anche carrello_copia
carrello_copia2 = copy.deepcopy(carrello) # se modifico quella di partenza non modifico anche questa, gli oggetti
# sono distinti da quella di partenza


# TUPLE


sede_principale = (45, 8) # latitudine e longitudine, non cambiano mai quindi tupla, non lista
sede_milano =(45, 9)

print(f"Sede principale lat: {sede_principale[0]} long: {sede_principale[1]}")

aliquota_iva = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente iva", 0.00)
) # tupla di tuple

for descrizione, valore in aliquota_iva:
    print(f"{descrizione}: {valore}")

def calcola_statistiche_carrello(carrello):
    """ Restituisce prezzo totale, medio, massimo, minimo """
    prezzi = [p.prezzo_unitario for p in carrello] # metto tutti i prezzi nel carrello
    return sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi)

tot, media, max, min = calcola_statistiche_carrello(carrello) # fa un unpacking di questi affidandoli a variabili
# elementi

tot, *altri_campi = calcola_statistiche_carrello(carrello) # fa un unpacking mettendo gli altri valori tutti
# assieme moltiplicati
print(tot)


# SET


categorie = {"Gold", "Silver", "Bronze", "Gold"} # il secondo gold non lo inserisce perchè ci può essere solo un
# elemento per tipo
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
categorie_all = categorie.union(categorie2) # unisce i due set
categorie_all2 = categorie | categorie2 # stessa cosa
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 # elementi presenti solo in categorie, non acnhe in categorie2
print(categorie_esclusive)

categorie_esclusive2 = categorie ^ categorie2 # differenza simmetrica, stampa gli elementi che sono solo nel primo
# o solo nel secondo
print(categorie_esclusive2)

prodotti_ordine_A = {p1, p2, p3}
prodotti_ordine_A = {ProdottoRecord("Tablet", 700.0),
                     ProdottoRecord("Monitor", 150.0),
                     ProdottoRecord("Prodotto", 100.0)}

# Metodi utili
s = set()
s1 = set()

# Aggiungere
s.add(ProdottoRecord("aaa", 50.0)) # aggiunge un elemento
s.update([ProdottoRecord("bbb", 60.0), ProdottoRecord("ccc", 40.0)]) # aggiunge più elementi

# Togliere
s.remove(p1) # se non esiste solleva errore
s.discard(p1) # non solleva l'errore se non esiste
s.pop() # rimuove e restituisce un elemento
s.clear() # svuota

# Operazioni insiemistiche
s.union(s1) # s | s1, fa unione
s.intersection(s1) # s & s1, fa intersezione
s.difference(s1) # s - s1, fa la differenza
s.symmetric_difference(s1) # s ^ s1, elementi solo in uno o nell'altro

s1.issubset(s) # se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono in s1 (sovrainsieme)
s1.isdisjoint(s) # se gli elementi di s e di s1 sono diversi, gli insiemi sono totalmente disgiunti


# DIZIONARIO


catalogo = {
    "LAP001" : p1,
    "LAP002" : ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001" : p2,
    "AUR001" : p3
}

cod = "LAP002"
prod = catalogo[cod]
print(f"Il prodotto con codice {cod} è {prod}")
# print(f"Cerca un altro oggetto: {catalogo["NonEsiste"]}") # se non lo trova manda errore

prod1 = catalogo.get("NonEsiste")
if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0)) # se non trova il prodotto, stampa il
# prodotto record sconosciuto
print(prod2)

# COMPREHENSION DIZIONARIO

prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()} # crea un dizionario con l'argomento
# delle graffe

v = catalogo["chiave"] # per leggere, restituisce errore se non esiste
v = catalogo.get("chiave", "default") # uguale ma se non esiste rende il default
catalogo["chiave"] = v # scrivo sul dizionario
v = catalogo.get("chiave")
rimosso = catalogo.pop("LAP002") # toglie l'elemento con la chiave che gli passo, se lo pongo uguale a qualcosa
# mi assegna quello che tolgo
catalogo.clear()
keys = list(catalogo.keys()) # lista di chiavi
values = list(catalogo.values()) # lista di valori
for k in keys:
    print(k)
for v in values:
    print(v)
for key, value in catalogo.items():  # catalogo.items() dà le coppie chiave valore
    print(f"Cod {key} è assoviata a: {value}")
key in catalogo # verifica se la chiave è presente nel dizionario

""" ESERCIZIO: PER CIASCUNO DEI SEGUENTI CASI DECIDERE CHE STRUTTURA USARE"""

""" 1) memorizzare una lista di ordini che dovranno essere processati in ordine di arrivo """ # lista
c1 = ClienteRecord("Giovanni", "g.l@gmail.com", "Gold")
ordini = [(Ordine([RigaOrdine(p1, 3), RigaOrdine(p3, 4)], c1), 0)] # è una tupla che mi dice quando sono arrivati
# gli ordini

""" 2) memorizzare i codici fiscali dei clienti, univoci """ # set
codici_fiscali = {"AAA", "BBB"}

""" 3) creare un database di prodotti che posso cercare con un codice univoco """ # dizionario
diz = {"AAA": p1, "BBB": p2}

""" 4) memorizzare le coordinate gps della nuova sede di roma """ # tupla
coordinate = (45, 56)

""" 5) tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale """ # set


# COUNTER


lista_clienti = [
    ClienteRecord("Paolo", "p@polito.it", "Gold"),
    ClienteRecord("Cigo", "c@polito.it", "Silver"),
    ClienteRecord("Vale", "v@polito.it", "Bronze"),
    ClienteRecord("Lollo", "l@polito.it", "Goold"),
    ClienteRecord("Jaco", "j@polito.it", "Silver"),
    ClienteRecord("Sara", "s@polito.it", "Silver"),
    ]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)
print("Distribuzione categorie clienti")
print(categorie_counter)
print("2 domande più frequenti")
print(categorie_counter.most_common(2))
print("Totale")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13,
     "Tablet": 14}
)
vendite_febbraio = Counter(
    {"Laptop": 3, "Tablet": 5}
)
vendite_bimestre = vendite_febbraio + vendite_gennaio # le metto assieme
differenza_vendiite = vendite_gennaio - vendite_febbraio # differenza delle vendite
vendite_gennaio["Laptop"] += 4 # modifico
