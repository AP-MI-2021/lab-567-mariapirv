from UserInterface.console import runMenu
from UserInterface.newConsole import newMenu


def showMenu(lista):
    print("1. Meniu 'pas cu pas' + functionalitati")
    print("2. Meniu CRUD")
    meniu = input("Ce meniu doriti sa alegeti?")
    if meniu == "1":
        runMenu(lista)
    elif meniu == "2":
        newMenu(lista)
    else:
        print("Meniu gresit! Reincercati!")