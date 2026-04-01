import flet as ft
from gestionale.gestoreOrdini import GestoreOrdini

class Controller:

    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdini()

    def add_ordine(self, e):

        # Prodotto
        nomePstr = self._view._txtInNomeP.value
        if nomePstr == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il campo nome prodotto non può essere vuoto", color = "red"))
            self._view.update_page()
            return

        try:
            prezzoPstr = float(self._view._txtInPrezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Attenzione, il prezzo deve essere un numero",
                                                      color = "red"))
            self._view.update_page()
            return

        try:
            quantitaPstr = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Attenzione, la quantità deve essere un intero",
                                                      color = "red"))
            self._view.update_page()
            return

        # Cliente
        nomeCstr = self._view._txtInNomeC.value
        if nomeCstr == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il campo nome cliente non può essere vuoto", color = "red"))
            self._view.update_page()
            return

        mailCstr = self._view._txtInMail.value
        if mailCstr == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il campo nome prodotto non può essere vuoto", color = "red"))
            self._view.update_page()
            return

        categoriaCstr = self._view._txtInCategoria.value
        if categoriaCstr == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il campo nome prodotto non può essere vuoto", color = "red"))
            self._view.update_page()
            return

        ordine = self._model.crea_ordine(nomePstr, prezzoPstr, quantitaPstr, nomeCstr, mailCstr, categoriaCstr)
        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMailC.value = ""
        self._view._txtInCategoriaC.value = ""

        self._view._lvOut.controls.append(ft.Text(value = "Ordine correttamente inserito", color = "green"))
        self._view._lvOut.controls.append(ft.Text(value = "Dettagli dell'ordine"))
        self._view._lvOut.controls.append(ft.Text(ordine.riepilogo()))
        self._view._lvOut.controls.append(ft.Text("\n"))

        self._view.update_page()

    def gestisci_ordine(self, e):
        self._view._lvOut.controls.clear() # svuoto l'interfaccia grafica
        res, ordine = self._model.processa_prossimo_ordine() # devo processare il prossimo ordine

        if res:
            self._view._lvOut.controls.append(ft.Text("Ordine processato con successo", color = "green"))
            self._view._lvOut.controls.append(ft.Text(ordine.riepilogo()))
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text("Non ci sono ordini in coda", color = "blue"))
            self._view.update_page()

    def gestisci_all_ordini(self, e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini()

        if not ordini:
            self._view._lvOut.controls.append(ft.Text("Non ci sono ordini in coda", color = "blue"))
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text(f"Ho processato correttamente {len(ordini)} ordini", color = "green"))
            for o in ordini:
                self._view._lvOut.controls.append(ft.Text(o.riepilogo()))
            self._view.update_page()

    def stampa_sommario(self, e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Di seguito il sommario dello stato del business", color = "orange"))

        self._view._lvOut.controls.append(ft.Text(self._model.get_riepilogo()))
        self._view.update_page()
