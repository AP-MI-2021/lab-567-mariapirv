from Domain.rezervare import get_clasa, get_pret, get_id
from Logic.CRUD import get_by_id, adauga_rezervare
from Logic.functionalitati import transformare_clasa_superioara, ieftinire_rezervari_cu_procentaj, pret_max_pe_clasa, \
    ordonare_descres_pret, suma_per_nume, do_undo, do_redo


def test_transformare_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = transformare_clasa_superioara("londra", lista)

    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    assert get_clasa(get_by_id("2", lista)) == "economy plus"


def test_ieftinire_rezervari_cu_procentaj():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = ieftinire_rezervari_cu_procentaj(50, lista)

    assert get_pret(get_by_id("1", lista)) == 100
    assert get_pret(get_by_id("2", lista)) == 25


def test_pret_max_pe_clasa():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 50, "da", lista)
    lista = adauga_rezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adauga_rezervare("4", "paris", "business", 200, "da", lista)
    lista = adauga_rezervare("5", "new york", "economy plus", 500, "da", lista)
    lista = adauga_rezervare("6", "barcelona", "economy", 1000, "da", lista)

    rezultat = pret_max_pe_clasa(lista)

    assert len(rezultat) == 3
    assert rezultat["economy"] == 1000
    assert rezultat["economy plus"] == 500
    assert rezultat["business"] == 200


def test_ordonare_descres_pret():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "bucuresti", "economy plus", 290, "da", lista)
    lista = adauga_rezervare("3", "milano", "economy", 50, "nu", lista)
    lista = adauga_rezervare("4", "new york", "economy plus", 500, "da", lista)

    rezultat = ordonare_descres_pret(lista)

    assert get_id(rezultat[0]) == "4"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"
    assert get_id(rezultat[3]) == "3"


def test_suma_per_nume():
    lista = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adauga_rezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adauga_rezervare("4", "londra", "business", 200, "da", lista)
    lista = adauga_rezervare("5", "londra", "economy plus", 500, "da", lista)
    lista = adauga_rezervare("6", "barcelona", "economy", 1000, "da", lista)

    rezultat = suma_per_nume(lista)

    assert rezultat["londra"] == 900
    assert rezultat["milano"] == 290
    assert rezultat["barcelona"] == 1050


def test_undo_redo():
    lista = []
    undolist = []
    redolist = []
    lista = adauga_rezervare("1", "londra", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adauga_rezervare("3", "milano", "economy", 290, "nu", lista)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')],
                     [('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')]]

    lista = transformare_clasa_superioara("londra", lista)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy plus'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')],
                     [('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')]]

    lista = do_undo(lista, undolist, redolist)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')],
                     [('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')]]

    lista = do_undo(lista, undolist, redolist)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')]]

    lista = do_redo(lista, undolist, redolist)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')],
                     [('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')]]

    lista = ordonare_descres_pret(lista)

    assert lista == [[('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')],
                     [('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')]]

    lista = do_undo(lista, undolist, redolist)

    assert lista == [[('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')],
                     [('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')]]

    lista = do_redo(lista, undolist, redolist)

    assert lista == [[('id', '3'), ('nume', 'milano'), ('clasa', 'economy'), ('pret', 290), ('checkin', 'nu')],
                     [('id', '1'), ('nume', 'londra'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'da')],
                     [('id', '2'), ('nume', 'barcelona'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'da')]]
