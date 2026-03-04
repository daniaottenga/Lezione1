from datetime import date
from dataclasses import dataclass

from gestionale.core.clienti import Cliente
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"=" * 60, # ripeto l'uguale per 60 volte
            f"Fattura numero {self.numero_fattura} del {self.data}",
            f"=" * 60,
            f"Cliente: {self.ordine.cliente.name}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail: {self.ordine.cliente.email}",
            f"=" * 60,
            f"DETTAGLIO ORDINE"
        ]
        for i, riga in enumerate(self.ordine.righe): # enumerate mi restituisce l'indice con cui ho trovato l'oggetto
            # l'altro è l'oggetto stesso
            linee.append(
                f"{i}. "
                f"{riga.prodotto.name} "
                f"Quantità {riga.quantita} x {riga.prodotto.prezzo_unitario} = "
                f"TOT. {riga.totale_riga()}"
            )

        linee.extend([
            f"-" * 60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA(22%): {self.ordine.totale_netto() * 0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"-" * 60,
            ]
        )

        return "\n".join(linee)

def _test_modulo():
    cliente = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    p1 = ProdottoRecord("Cioccolata", 2.0)
    p2 = ProdottoRecord("Pistacchi", 20.0)
    p3 = ProdottoRecord("Caramelle", 5.0)
    ordine = Ordine(righe = [
        RigaOrdine(p1, 100),
        RigaOrdine(p2, 3),
        RigaOrdine(p1, 70)
    ], cliente = cliente)
    fattura = Fattura(ordine, "2026/01", date.today())

    print(fattura.genera_fattura())


if __name__ == "__main__":
    _test_modulo()