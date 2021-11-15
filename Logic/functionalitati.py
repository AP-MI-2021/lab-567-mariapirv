from Domain.rezervare import get_nume, get_clasa, get_id, get_pret, get_checkin, creeaza_rezervare


def transformare_clasa_superioara(nume, lista):
    """
    transforma intr-o clasa superioara rezervarile cu numele citit
    :param nume: numele unei rezervari
    :param lista: lista rezervarilor
    :return: o noua lista transformata cu rezervarile cu un anumit nume la o clasa superioara,
    restul ramanand nemodificate
    """
    new_list = []
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == 'economy':
                clasa_noua = 'economy plus'
            else:
                clasa_noua = 'business'
            rezervare_noua = creeaza_rezervare(get_id(rezervare), get_nume(rezervare), clasa_noua, get_pret(rezervare),
                                               get_checkin(rezervare))
            new_list.append(rezervare_noua)
        else:
            new_list.append(rezervare)
    return new_list


def ieftinire_rezervari_cu_procentaj(procent, lista):
    """
    ieftineste toate rezervărilor la care s-a făcut checkin cu un procentaj citit
    :param procent: procentul cu care se va face ieftinirea
    :param lista: lista de rezervari
    :return: o lista noua cu toate rezrevarile la care s-a facut checkin cu un anumit procentaj,
    restul ramanad nemodificate
    """
    new_list = []
    for rezervare in lista:
        if get_checkin(rezervare) == "da":
            pret = get_pret(rezervare)
            rezervare_noua = creeaza_rezervare(get_id(rezervare), get_nume(rezervare), get_clasa(rezervare),
                                               pret - (procent * pret / 100), get_checkin(rezervare))
            new_list.append(rezervare_noua)
        else:
            new_list.append(rezervare)
    return new_list


def pret_max_pe_clasa(lista):
    """
    determina prețul maxim pentru fiecare clasă
    :param lista: lista de rezervari
    :return: un dictionar care contine preturile maxime pentru fiecare clasa
    """
    rezultat = {}
    for rezervare in lista:
        pret = get_pret(rezervare)
        clasa = get_clasa(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat


def ordonare_descres_pret(lista):
    """
    ordoneaza rezervările descrescător după preț
    :param lista: lista de rezervari
    :return: lista de rezervari ordonata dupa pret
    """
    return sorted(lista, key=lambda rezervare: get_pret(rezervare), reverse=True)


def suma_per_nume(lista):
    """
    determina suma preturilor pentru fiecare nume
    :param lista: lista de rezervari
    :return: un dictionar care contine suma preturilor pentru fiecare nume
    """
    rezultat = {}
    for rezervare in lista:
        nume = get_nume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + get_pret(rezervare)
        else:
            rezultat[nume] = get_pret(rezervare)
    return rezultat


def do_undo(lista, undolist, redolist):
    if undolist:
        top_undo = undolist.pop()
        redolist.append(lista)
        return top_undo
    return None


def do_redo(lista, undolist, redolist):
    if redolist:
        top_redo = redolist.pop()
        undolist.append(lista)
        return top_redo
    return None
