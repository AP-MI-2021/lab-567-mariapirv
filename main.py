from Logic.CRUD import adauga_rezervare
from Tests.testAll import run_all_tests
from UserInterface.menu import show_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adauga_rezervare("3", "milano", "economy", 290, "nu", lista)
    show_menu(lista)


main()
