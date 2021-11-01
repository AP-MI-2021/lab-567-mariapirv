def creeazaRezervare (id, nume, clasa, pret, checkin):
    '''
    creeaza un dictionar ce reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce contine o rezervare
    '''
    lista = [id, nume, clasa, pret, checkin]
    return lista

def getId(rezervare):
    return rezervare[0]

def getNume(rezervare):
    return rezervare[1]

def getClasa(rezervare):
    return rezervare[2]

def getPret(rezervare):
    return rezervare[3]

def getCheckin(rezervare):
    return rezervare[4]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )