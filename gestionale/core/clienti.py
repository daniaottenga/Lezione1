# Scrivere una classe Cliente che abbia i campi "name", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classer avesse un metodo che chiamiamo "descrizione" che deve restituire una stringa
# formattata ad es. "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

# Si modifichi la classe cliente in modo tale che la proprietà categoria sia protetta e accetti soo le
# categorie Gold, Silver e Bronze

from dataclasses import dataclass

categorie_valide = {"Gold", "Silver", "Bronze"}

class Cliente:
    def __init__(self, name, email, categoria):
        self.name = name
        self.email = email
        self.categoria = categoria
        self._categoria = None

    def descrizione(self):
        return f"Cliente {self.name} ({self.categoria} - {self.email})"

    @property
    def categoria(self): # come il getter in java
        return self._categoria # quando chiamerò "prodotto1.name" chiamerò in realtà questo metodo

    @categoria.setter # lo posso fare solo se prima ho definito il getter
    def categoria(self, categoria):
        if categoria not in  categorie_valide:
            raise ValueError("Atttenzione, puoi assegnare solo Gold, Silver e Bronze.")
        self._categoria = categoria


def _test_modulo():
    c1 = Cliente(name="Mario Bianchi", email="mario.bianchi@polito.it", categoria="Gold")
    print(c1)
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()