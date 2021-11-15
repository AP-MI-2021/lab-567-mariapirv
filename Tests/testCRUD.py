from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, sterge_rezervare, get_by_id, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)

    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "londra"
    assert get_clasa(lista[0]) == "economy"
    assert get_pret(lista[0]) == 200
    assert get_checkin(lista[0]) == "da"


def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = sterge_rezervare("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = modifica_rezervare("1", "paris", "business", 1000, "nu", lista)

    rezervare_verificare = get_by_id("1", lista)

    assert get_id(rezervare_verificare) == "1"
    assert get_nume(rezervare_verificare) == "paris"
    assert get_clasa(rezervare_verificare) != "economy"
    assert get_pret(rezervare_verificare) == 1000
    assert get_checkin(rezervare_verificare) == "nu"


def test_get_by_id():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is None
