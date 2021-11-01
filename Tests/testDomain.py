from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin

def testRezervare():
    rezervare = creeazaRezervare("1", "londra", "economy", 200, "da")

    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "londra"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 200
    assert getCheckin(rezervare) == "da"