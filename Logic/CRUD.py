from Domain.rezervare import creeaza_rezervare, get_id


def adauga_rezervare(id_rezervare, nume, clasa, pret, checkin, lista):
    """
    adauga o rezervare intr-o lista
    :param id_rezervare: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista care contine elementele noi, cat si cele vechi
    """
    if get_by_id(id_rezervare, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    return lista + [rezervare]


def get_by_id(id_rezervare, lista):
    """
    gaseste o rezervare cu id-ul dat intr-o lista
    :param id_rezervare: string
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat din lista sau None, daca aceasta nu exista
    """
    for rezervare in lista:
        if get_id(rezervare) == id_rezervare:
            return rezervare
    return None


def sterge_rezervare(id_rezervare, lista):
    """
    sterge o rezervare cu id-ul dat din lista
    :param id_rezervare: id-ul rezervarii care trebuie stearsa
    :param lista: o lista de rezervari
    :return: lista de rezervari fara rezervarea cu id-ul dat
    """
    return [rezervare for rezervare in lista if get_id(rezervare) != id_rezervare]


def modifica_rezervare(id_rezervare, nume, clasa, pret, checkin, lista):
    """
    modifica o rezervare cu id-ul dat
    :param id_rezervare: id-ul rezervarii
    :param nume: numele rezervarii
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkin: checkin-ul rezervarii
    :param lista: o lista de rezervari
    :return: lista modificata
    """
    new_lista = []
    for rezervare in lista:
        if get_id(rezervare) == id_rezervare:
            new_rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
            new_lista.append(new_rezervare)
        else:
            new_lista.append(rezervare)
    return new_lista
