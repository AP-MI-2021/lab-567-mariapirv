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