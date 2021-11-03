
from Domain.rezervare import getClasa, getPret
from Logic.CRUD import getById, adaugaRezervare
from Logic.functionalitati import transformareClasaSuperioara, ieftinireRezervariCuProcentaj

def testTransformareClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = transformareClasaSuperioara("londra",lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "economy plus"

def testIeftinireRezervariCuProcentaj():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 50, "da", lista)

    lista = ieftinireRezervariCuProcentaj(50,lista)

    assert getPret(getById("1", lista)) == 100
    assert getPret(getById("2", lista)) == 25

    lista = ieftinireRezervariCuProcentaj(10, lista)

    assert getPret(getById("1", lista)) == 180
    assert getPret(getById("2", lista)) == 45