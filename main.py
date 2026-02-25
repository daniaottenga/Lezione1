# Scriviamo un codice che modelli un semplice gestionale aziendale. Dovremo
# prevedere la possibilità di definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente scontati, ...

class Prodotto:

    aliquota_iva = 0.22  # variabile di classe, è la stessa per tutte le istanze che verranno crate

    def __init__(self, name: str, price: float, quantity: int, supplier= None):
        self.name= name
        self.price= price
        self.quantity= quantity
        self.supplier= supplier

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


myproduct1 = Prodotto(name= "Laptop", price= 1200.0, quantity= 12, supplier= "ABC")
myproduct2 = Prodotto(name= "Mouse", price= 10, quantity= 25, supplier= "CDE")
p3= Prodotto.costruttore_con_quantità_uno(name= "Auricolari", price= 200.0, supplier= "ABC")

print(f"Nome prodotto: {myproduct1.name}")
print(f"Prezzo prodotto: {myproduct1.price}")
print(f"Totale lordo di myproduct1: {myproduct1.valore_lordo()}") # uso metodo istanza
print(f"Prezzo scontato di myproduct1: {Prodotto.applica_sconto(myproduct1.price, percentage= 0.15)}")
print(f"Nome prodotto2: {myproduct2.name} - Prezzo prodotto2: {myproduct2.price}")

# Scrivere una classe Cliente che abbia i campi "name", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classer avesse un metodo che chiamiamo "descrizione" che deve restituire una stringa
# formattata ad es. "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

class Client:
    def __init__(self, name, email, categoria):
        self.name = name
        self.email = email
        self.categoria = categoria

    def descrizione(self):
        return f"Cliente {self.name} ({self.categoria} - {self.email})"


c1 = Client(name= "Mario Bianchi", email= "mario.bianchi@polito.it", categoria= "Gold")
print(c1)
print(c1.descrizione())