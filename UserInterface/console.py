from Logic.CRUD import sterge_rezervare, modifica_rezervare, adauga_rezervare
from Domain.rezervare import to_string
from Logic.functionalitati import transformare_clasa_superioara, ieftinire_rezervari_cu_procentaj, pret_max_pe_clasa, \
    ordonare_descres_pret, suma_per_nume, do_redo, do_undo


def print_menu():
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


def ui_adauga_rezervare(lista, undolist, redolist):
    try:
        id_rezervare = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Ati facut checkin-ul?: ")

        rezultat = adauga_rezervare(id_rezervare, nume, clasa, pret, checkin, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_rezervare(lista, undolist, redolist):
    id_rezervare = input("Dati id-ul rezervarii de sters: ")

    rezultat = sterge_rezervare(id_rezervare, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat


def ui_modifica_rezervare(lista, undolist, redolist):
    try:
        id_madificare = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Ati facut checkin-ul la noua rezervare?: ")

        rezultat = modifica_rezervare(id_madificare, nume, clasa, pret, checkin, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_transformare_clasa_superioara(lista, undolist, redolist):
    nume_citit = input("Dati numele la care doriti sa faceti trecerea la clasa superioara a rezervarii: ")
    rezultat = transformare_clasa_superioara(nume_citit, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat


def ui_ieftinire_rezervari_cu_procentaj(lista, undolist, redolist):
    try:
        procentaj = float(input("Dati procentajul cu care doriti sa se faca ieftinirea: "))
        rezultat = ieftinire_rezervari_cu_procentaj(float(procentaj), lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_pret_max_pe_clasa(lista, undolist, redolist):
    rezultat = pret_max_pe_clasa(lista)
    for clasa in rezultat:
        print("Clasa {} are pretul maxim {}".format(clasa, rezultat[clasa]))
    undolist.append(lista)
    redolist.clear()
    return rezultat


def uiOrdonareDescresPret(lista, undolist, redolist):
    rezultat = ordonare_descres_pret(lista)
    showAll(rezultat)
    undolist.append(lista)
    redolist.clear()
    return rezultat


def uiSumaPerNume(lista, undolist, redolist):
    rezultat = suma_per_nume(lista)
    for nume in rezultat:
        print("{} are suma preturilor {}".format(nume, rezultat[nume]))
    undolist.append(lista)
    redolist.clear()
    return rezultat


def showAll(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def runMenu(lista):
    undolist = []
    redolist = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adauga_rezervare(lista, undolist, redolist)
        elif optiune == "2":
            lista = ui_sterge_rezervare(lista, undolist, redolist)
        elif optiune == "3":
            lista = ui_modifica_rezervare(lista, undolist, redolist)
        elif optiune == "4":
            lista = ui_transformare_clasa_superioara(lista, undolist, redolist)
        elif optiune == "5":
            lista = ui_ieftinire_rezervari_cu_procentaj(lista, undolist, redolist)
        elif optiune == "6":
            ui_pret_max_pe_clasa(lista, undolist, redolist)
        elif optiune == "7":
            lista = uiOrdonareDescresPret(lista, undolist, redolist)
        elif optiune == "8":
            uiSumaPerNume(lista, undolist, redolist)
        elif optiune == "u":
            if len(undolist) > 0:
                lista = do_undo(lista, undolist, redolist)
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redolist) > 0:
                lista = do_redo(lista, undolist, redolist)
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
