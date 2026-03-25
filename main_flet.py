import flet as ft
from UI.controller import Controller
from UI.view import View

# verrà data già implementata
def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c) # non posso passare a v c all'inizio quindi lo faccio così
    v.carica_interfaccia()

ft.app(target = main)