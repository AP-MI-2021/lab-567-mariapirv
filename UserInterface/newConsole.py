from Logic.CRUD import adauga_rezervare, modifica_rezervare, sterge_rezervare
from UserInterface.console import showAll


def newMenu(lista):
    while True:
        comanda = input("Ce comenzi doriti sa efectuati despartite prin ';' ?")
        categorii = comanda.split(";")
        if categorii[0] == "exit":
            break
        else:
            for optiune in categorii:
                camp = optiune.split(",")
                if camp[0] == "add":
                    try:
                        lista = adauga_rezervare(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
                    except IndexError as ie:
                        print("Eroare: {}".format(ie))
                elif camp[0] == "show all":
                    showAll(lista)
                elif camp[0] == "modify":
                    try:
                        lista = modifica_rezervare(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
                    except IndexError as ie:
                        print("Eroare: {}".format(ie))
                elif camp[0] == "delete":
                    lista = sterge_rezervare(camp[1], lista)
                else:
                    print("Optiune gresita! Reincercati!")
