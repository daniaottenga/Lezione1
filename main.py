# Scriviamo un codice che modelli un semplice gestionale aziendale. Dovremo
# prevedere la possibilità di definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente scontati, ...

class Prodotto:

    aliquota_iva = 0.22  # variabile di classe, è la stessa per tutte le istanze che verranno crate

    def __init__(self, name: str, price: float, quantity: int, supplier= None):
        self.name = name #se ne metto due ancora più privata (non li usiamo)
        self._price = None # mettere _ mi permette di dire che è privata
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore(self):
        return self.price * self.quantity

    def valore_lordo(self):
        netto = self.price * self.quantity
        lordo = netto * (1 + self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantita_uno(cls, name: str, price: float, supplier: str):
        cls(name, price, quantity= 1, supplier= supplier)

    @staticmethod
    def applica_sconto(price, percentage):
        return price * (1 - percentage)

    @property
    def price(self): # come il getter in java
        return self._price # quando chiamerò "prodotto1.name" chiamerò in realtà questo metodo

    @price.setter # lo posso fare solo se prima ho definito il getter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Atttenzione il prezzo non può essere negativo.")
        self._price = valore

myproduct1 = Prodotto(name= "Laptop", price= 1200.0, quantity= 12, supplier= "ABC")
myproduct2 = Prodotto(name= "Mouse", price= 10, quantity= 25, supplier= "CDE")
p3= Prodotto.costruttore_con_quantita_uno(name= "Auricolari", price= 200.0, supplier= "ABC")

Prodotto.aliquota_iva = 0.24 # aggiorna il valore per tutti

print(f"Nome prodotto: {myproduct1.name}")
print(f"Prezzo prodotto: {myproduct1.price}")
print(f"Totale lordo di myproduct1: {myproduct1.valore_lordo()}") # uso metodo istanza
print(f"Prezzo scontato di myproduct1: {Prodotto.applica_sconto(myproduct1.price, percentage= 0.15)}")
print(f"Nome prodotto2: {myproduct2.name} - Prezzo prodotto2: {myproduct2.price}")

# Scrivere una classe Cliente che abbia i campi "name", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classer avesse un metodo che chiamiamo "descrizione" che deve restituire una stringa
# formattata ad es. "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

# Si modifichi la classe cliente in modo tale che la proprietà categoria sia protetta e accetti soo le
# categorie Gold, Silver e Bronze

class Client:
    def __init__(self, name, email, categoria):
        self.name = name
        self.email = email
        self.categoria = categoria
        self._categoria = None

    def descrizione(self):
        return f"Cliente {self.name} ({self.categoria} - {self.email})"

    @property
    def categoria(self):  # come il getter in java
        return self._categoria # quando chiamerò "prodotto1.name" chiamerò in realtà questo metodo

    @categoria.setter  # lo posso fare solo se prima ho definito il getter
    def categoria(self, categoria):
        categorie = {"Gold", "Silver", "Bronze"}
        if categoria not in  categorie:
            raise ValueError("Atttenzione, puoi assegnare solo Gold, Silver e Bronze.")
        self._categoria = categoria


c1 = Client(name= "Mario Bianchi", email= "mario.bianchi@polito.it", categoria= "Gold")
print(c1)
print(c1.descrizione())