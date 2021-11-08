from Logic.CRUD import stergeRezervare, modificaRezervare, adaugaRezervare
from Domain.rezervare import toString
from Logic.functionalitati import transformareClasaSuperioara, ieftinireRezervariCuProcentaj, pretMaxPeClasa, \
    ordonareDescresPret, sumaPerNume

def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari")
    print("x. Iesire")

def uiAdaugaRezervare(lista, undolist, redolist):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Ati facut checkin-ul?: ")

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeRezervare(lista, undolist, redolist):
    id = input("Dati id-ul rezervarii de sters: ")

    rezultat = stergeRezervare(id, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def uiModificaRezervare(lista, undolist, redolist):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Ati facut checkin-ul la noua rezervare?: ")

        rezultat =  modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiTransformareClasaSuperioara(lista, undolist, redolist):
    numeCitit = input("Dati numele la care doriti sa faceti trecerea la clasa superioara a rezervarii: ")
    rezultat =  transformareClasaSuperioara(numeCitit, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat


def uiIeftinireRezervariCuProcentaj(lista, undolist, redolist):
    try:
        procentaj = float(input("Dati procentajul cu care doriti sa se faca ieftinirea: "))
        rezultat = ieftinireRezervariCuProcentaj(float(procentaj), lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))

def uiPretMaxPeClasa(lista, undolist, redolist):
    rezultat = pretMaxPeClasa(lista)
    for clasa in rezultat:
        print("Clasa {} are pretul maxim {}".format(clasa, rezultat[clasa]))
    undolist.append(lista)
    redolist.clear()
    return rezultat

def uiOrdonareDescresPret(lista, undolist, redolist):
    rezultat = ordonareDescresPret(lista)
    showAll(rezultat)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def uiSumaPerNume(lista, undolist, redolist):
    rezultat = sumaPerNume(lista)
    for nume in rezultat:
        print("{} are suma preturilor {}".format(nume, rezultat[nume]))
    undolist.append(lista)
    redolist.clear()
    return rezultat

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def runMenu(lista):
    undolist = []
    redolist = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista,undolist,redolist)
        elif optiune == "2":
            lista = uiStergeRezervare(lista,undolist,redolist)
        elif optiune == "3":
            lista = uiModificaRezervare(lista,undolist,redolist)
        elif optiune == "4":
            lista = uiTransformareClasaSuperioara(lista,undolist,redolist)
        elif optiune == "5":
            lista = uiIeftinireRezervariCuProcentaj(lista,undolist,redolist)
        elif optiune == "6":
            uiPretMaxPeClasa(lista,undolist,redolist)
        elif optiune == "7":
            uiOrdonareDescresPret(lista,undolist,redolist)
        elif optiune == "8":
            uiSumaPerNume(lista,undolist,redolist)
        elif optiune == "u":
            if len(undolist) > 0:
                redolist.append(lista)
                lista = undolist.pop()
            else:
                print("Nu se poate face und!")
        elif optiune == "r":
            if len(redolist) > 0:
                undolist.append(lista)
                lista = redolist.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")