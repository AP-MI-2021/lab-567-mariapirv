def creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin):
    """
    creeaza un dictionar ce reprezinta o rezervare
    :param id_rezervare: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce contine o rezervare
    """
    return {
        "id": id_rezervare,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }


def get_id(rezervare):
    return rezervare["id"]


def get_nume(rezervare):
    return rezervare["nume"]


def get_clasa(rezervare):
    return rezervare["clasa"]


def get_pret(rezervare):
    return rezervare["pret"]


def get_checkin(rezervare):
    return rezervare["checkin"]


def to_string(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )
