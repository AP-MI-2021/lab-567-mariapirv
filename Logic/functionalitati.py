from Domain.rezervare import getNume, getClasa, getId, getPret, getCheckin, creeazaRezervare

def transformareClasaSuperioara(nume, lista):
    '''
    transforma intr-o clasa superioara rezervarile cu numele citit
    :param nume: numele unei rezervari
    :param lista: lista rezervarilor
    :return: o noua lista transformata cu rezervarile cu un anumit nume la o clasa superioara, restul ramanand nemodificate
    '''
    new_list = []
    for rezervare in lista:
        if getNume(rezervare) == nume:
            if getClasa(rezervare) == 'economy':
                clasa_noua = 'economy plus'
            else:
                clasa_noua = 'business'
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                clasa_noua,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            new_list.append(rezervareNoua)
        else:
            new_list.append(rezervare)
    return new_list

def ieftinireRezervariCuProcentaj(procent, lista):
    '''
    ieftineste toate rezervărilor la care s-a făcut checkin cu un procentaj citit
    :param procent: procentul cu care se va face ieftinirea
    :param lista: lista de rezervari
    :return: o lista noua cu toate rezrevarile la care s-a facut checkin cu un anumit procentaj, restul ramanad nemodificate
    '''
    new_list = []
    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            pret = getPret(rezervare)
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                pret - (procent * pret / 100),
                getCheckin(rezervare)
            )
            new_list.append(rezervareNoua)
        else:
            new_list.append(rezervare)
    return new_list

def pretMaxPeClasa(lista):
    '''
    determina prețul maxim pentru fiecare clasă
    :param lista: lista de rezervari
    :return: un dictionar care contine preturile maxime pentru fiecare clasa
    '''
    rezultat = {}
    for rezervare in lista:
        pret = getPret(rezervare)
        clasa = getClasa(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat

def ordonareDescresPret(lista):
    '''
    ordoneaza rezervările descrescător după preț
    :param lista: lista de rezervari
    :return: lista de rezervari ordonata dupa pret
    '''
    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=True)

def sumaPerNume(lista):
    '''
    determina suma preturilor pentru fiecare nume
    :param lista: lista de rezervari
    :return: un dictionar care contine suma preturilor pentru fiecare nume
    '''
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + getPret(rezervare)
        else:
            rezultat[nume] = getPret(rezervare)
    return rezultat

def do_undo(lista,undolist,redolist):
        if undolist:
            top_undo = undolist.pop()
            redolist.append(top_undo)
            return top_undo
        return lista

def do_redo(lista,undolist,redolist):
    if redolist:
        top_redo = redolist.pop()
        undolist.append(top_redo)
        return top_redo
    return lista