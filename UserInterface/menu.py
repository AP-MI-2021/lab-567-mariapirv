from UserInterface.console import run_menu
from UserInterface.newConsole import new_menu


def show_menu(lista):
    print("1. Meniu 'pas cu pas' + functionalitati")
    print("2. Meniu CRUD")
    meniu = input("Ce meniu doriti sa alegeti?")
    if meniu == "1":
        run_menu(lista)
    elif meniu == "2":
        new_menu(lista)
    else:
        print("Meniu gresit! Reincercati!")
