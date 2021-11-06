from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UserInterface.console import runMenu

def main():
    runAllTests()
    lista = []
    '''
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 50, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adaugaRezervare("4", "paris", "business", 200, "da", lista)
    lista = adaugaRezervare("5", "new york", "economy plus", 500, "da", lista)
    lista = adaugaRezervare("6", "barcelona", "economy", 1000, "da", lista)
    '''
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adaugaRezervare("4", "londra", "business", 200, "da", lista)
    lista = adaugaRezervare("5", "londra", "economy plus", 500, "da", lista)
    lista = adaugaRezervare("6", "barcelona", "economy", 1000, "da", lista)
    runMenu(lista)

main()
