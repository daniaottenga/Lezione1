# Scriviamo un codice che modelli un semplice gestionale aziendale. Dovremo
# prevedere la possibilità di definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente scontati, ...

from dataclasses import dataclass # mi scrive già di suo un str

class Prodotto:

    aliquota_iva = 0.22  # variabile di classe, è la stessa per tutte le istanze che verranno crate

    def __init__(self, name: str, price: float, quantity: int, supplier = None): # costruttore della classe, metodo
        # dunder
        self.name = name # se ne metto due non ci si può proprio accedere (non li usiamo)
        self._price = None # mettere _ mi permette di dire che è privata anche se realmente non lo è
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self.price * self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto * (1 + self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantita_uno(cls, name: str, price: float, supplier: str):
        cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(price, percentage):
        return price * (1 - percentage)

    @property # come il getter in java, lo faccio sulle variabili con _
    def price(self):
        return self._price # quando chiamerò "prodotto1.name" chiamerò in realtà questo metodo

    @price.setter # lo posso fare solo se prima ho definito il getter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo.")
        self._price = valore

    def __str__(self): # per stampare l'oggetto
        return f"{self.name} - disponibilità {self.quantity} pezzi a {self.price}$"

    def __repr__(self): # stampa l'oggetto ma deve essere molto più rappresentativa dell'oggetto in sè mentre str è una
        # stringa solo carina da leggere. Questo metodo mi fa vedere i valori della variabile quando debuggo
        return (f"Prodotto (name = {self.name}, price = {self.price}, quantity = {self.quantity}, "
                f"supplier = {self.supplier}) ")

    def __eq__(self, other: object): # definisce se un istanza è uguale ad un'altra, scrivendo object dico che può
        # essere un qualsiasi oggetto
        if not isinstance(other, Prodotto): # verifico se other è un oggetto diverso da self
            return NotImplemented

        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)


    def __lt__(self, other: "Prodotto") -> bool : # rappresenta il comparatore <, scrivendo bool specifico che ritorna
        # un booleano
        return self.price < other.price # restituisce true se il prezzo di quest'oggetto è minore dell'altro

    def prezzo_finale(self) -> float:
       return self.price * (1 + self.aliquota_iva)

class ProdottoScontato(Prodotto): # classe che eredita da prodotto, ha già tutti i metodi di prodotto definiti

    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        # Prodotto.__init__() è un alternativa, uguale
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo() * (1 - self.sconto_percento / 100)

class Servizio(Prodotto):

    def __init__(self, name: str, tariffa_oraria: float, ore: int):
        super().__init__(name = name, price = tariffa_oraria, quantity = 1, supplier = None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

class Abbonamento():

    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile * self.mesi

@dataclass # come scrivere il costruttore ma più veloce
class ProdottoRecord:
    name: str
    prezzo_unitario: float

MAX_QUANTITA = 1000

def crea_prodotto_standard(name: str, price: float):
    return Prodotto(name, price, quantity = 1, supplier = None)

def _test_modulo():

    print("Sto testando il modulo prodotti.py")

    myproduct1 = Prodotto(name= "Laptop", price= 1200.0, quantity= 12, supplier= "ABC")
    myproduct2 = Prodotto(name= "Mouse", price= 10, quantity= 25, supplier= "CDE")
    p3= Prodotto.costruttore_con_quantita_uno(name= "Auricolari", price= 200.0, supplier= "ABC")
    p_a = Prodotto(name= "Laptop", price= 1200.0, quantity= 12, supplier= "ABC")
    p_b = Prodotto("Mouse", 10, 14, "CDE")

    Prodotto.aliquota_iva = 0.24 # aggiorna il valore per tutti

    print(f"Nome prodotto: {myproduct1.name}")
    print(f"Prezzo prodotto: {myproduct1.price}")
    print(f"Totale lordo di myproduct1: {myproduct1.valore_lordo()}") # uso metodo istanza
    print(f"Prezzo scontato di myproduct1: {Prodotto.applica_sconto(myproduct1.price, percentage= 0.15)}")
    print(f"Nome prodotto2: {myproduct2.name} - Prezzo prodotto2: {myproduct2.price}")
    print(myproduct1) # avendo scritto il metodo __str__ mi stampa quello che gli ho scritto dentro, da usare col debugger

    print("---------------------------------------------------")

    print("myproduct1 == p_a?", myproduct1 == p_a) # chiama __eq__
    print("p_b == p_a?", p_b == p_a)

    mylist = [p_a, p_b, myproduct1]
    mylist.sort(reverse = True)
    print("Lista prodotti ordinata:")
    for p in mylist:
        print(f" * {p}")

if __name__ == "__main__": # così se faccio run prodotti posso vedere queste stampe di testing, quando lo importo
    # in main non le stamperà
    _test_modulo()