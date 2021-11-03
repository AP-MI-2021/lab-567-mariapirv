from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UserInterface.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 300, "da", lista)
    lista = adaugaRezervare("2", "madrid", "business", 100, "da", lista)

    runMenu(lista)

main()
