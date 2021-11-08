from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UserInterface.menu import showMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 290, "nu", lista)
    showMenu(lista)

main()
