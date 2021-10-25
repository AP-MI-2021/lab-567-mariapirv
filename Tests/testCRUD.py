def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)

    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "londra"
    assert getClasa(lista[0]) == "economy"
    assert getPret(lista[0]) == 200
    assert getCheckin(lista[0]) == "da"

def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = stergeRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


