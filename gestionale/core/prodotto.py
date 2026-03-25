from dataclasses import dataclass


@dataclass # come scrivere il costruttore ma più veloce
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        self.name == other.name

    def __str__(self):
        return f"{self.name} - prezzo unitario {self.prezzo_unitario}"