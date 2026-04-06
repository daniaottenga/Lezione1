import flet as ft

# view è dato all'esame, modificato pochissimo
class View:

    def __init__(self, page):
        self._controller = None # non necessario, buona norma
        self._page = page
        self._page.title = "TdP 2025 -- software gestionale" # titolo
        self._page.horizontal_alignment = "CENTER" # mi allinea tutto al centro
        self._page.theme_mode = ft.ThemeMode.LIGHT # dà una schermata bianca
        self._txtInNomeP = None # dovrei farlo per ogni elemento creato nell'interfaccia, non obbligatorio
        self.update_page()

    def carica_interfaccia(self):

        # Prodotto
        self._txtInNomeP = ft.TextField(label = "Nome prodotto", width = 200)
        self._txtInPrezzo = ft.TextField(label = "Prezzo", width = 200)
        self._txtInQuantita = ft.TextField(label = "Quantità", width = 200)
        row1 = ft.Row(controls = [self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita],
                      alignment = ft.MainAxisAlignment.CENTER)

        # Cliente
        self._txtInNomeC = ft.TextField(label = "Nome cliente", width = 200)
        self._txtInMail = ft.TextField(label = "Mail", width = 200)
        self._txtInCategoria = ft.TextField(label = "Categoria", width = 200)
        row2 = ft.Row(controls = [self._txtInNomeC, self._txtInMail, self._txtInCategoria],
                      alignment = ft.MainAxisAlignment.CENTER)

        # Buttons
        self._btnAdd = ft.ElevatedButton(text = "Aggiungi ordine",
                                         on_click = self._controller.add_ordine,
                                         width = 200) # per fare un nuovo ordine
        self._btnGestisciOridne = ft.ElevatedButton(text = "Gestisci ordine",
                                         on_click = self._controller.gestisci_ordine,
                                         width = 200) # per processare un ordine
        self._btnGestisciAllOrdini = ft.ElevatedButton(text = "Gestisci tutti gli ordini",
                                         on_click = self._controller.gestisci_all_ordini,
                                         width = 200)
        self._btnStampaInfo = ft.ElevatedButton(text = "Stampa sommario",
                                         on_click = self._controller.stampa_sommario,
                                         width = 200) # per stampare
        row3 = ft.Row(controls = [self._btnAdd, self._btnGestisciOridne, self._btnGestisciAllOrdini, self._btnStampaInfo],
                      alignment = ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand = True)

        self._page.add(row1, row2, row3, self._lvOut)


    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()