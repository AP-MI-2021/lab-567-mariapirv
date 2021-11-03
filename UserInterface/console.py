from Logic.CRUD import stergeRezervare, modificaRezervare, adaugaRezervare
from Domain.rezervare import toString
from Logic.functionalitati import transformareClasaSuperioara, ieftinireRezervariCuProcentaj


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("a. Afisare rezervari")
    print("x. Iesire")

def uiAdaugaRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin = input("Ati facut checkin-ul?: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)

def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Ati facut checkin-ul la noua rezervare?: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def uiTransformareClasaSuperioara(lista):
    numeCitit = input("Dati numele la care doriti sa faceti trecerea la clasa superioara a rezervarii: ")
    return transformareClasaSuperioara(numeCitit, lista)

def uiIeftinireRezervariCuProcentaj(lista):
    procentaj = float(input("Dati procentajul cu care doriti sa se faca ieftinirea: "))
    return ieftinireRezervariCuProcentaj(float(procentaj), lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiTransformareClasaSuperioara(lista)
        elif optiune == "5":
            lista = uiIeftinireRezervariCuProcentaj(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")