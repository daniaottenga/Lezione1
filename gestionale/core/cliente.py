from dataclasses import dataclass


@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

    def __hash__(self): # identificato dalla mail
        return hash(self.email)

    def __eq__(self, other):
        self.email == other.email

    def __str__(self):
        return f"{self.name} -- {self.email} ({self.categoria})"
