from Domain.rezervare import getClasa, getPret, getId
from Logic.CRUD import getById, adaugaRezervare
from Logic.functionalitati import transformareClasaSuperioara, ieftinireRezervariCuProcentaj, pretMaxPeClasa, \
    ordonareDescresPret, sumaPerNume

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

def testPretMaxPeClasa():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 50, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adaugaRezervare("4", "paris", "business", 200, "da", lista)
    lista = adaugaRezervare("5", "new york", "economy plus", 500, "da", lista)
    lista = adaugaRezervare("6", "barcelona", "economy", 1000, "da", lista)

    rezultat = pretMaxPeClasa(lista)

    assert len(rezultat) == 3
    assert rezultat["economy"] == 1000
    assert rezultat["economy plus"] == 500
    assert rezultat["business"] == 200

def testOrdonareDescresPret():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "bucuresti", "economy plus", 290, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 50, "nu", lista)
    lista = adaugaRezervare("4", "new york", "economy plus", 500, "da", lista)

    rezultat = ordonareDescresPret(lista)

    assert getId(rezultat[0]) == "4"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"
    assert getId(rezultat[3]) == "3"

def testSumaPerNume():
    lista = []
    lista = adaugaRezervare("1", "londra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "barcelona", "economy plus", 50, "da", lista)
    lista = adaugaRezervare("3", "milano", "economy", 290, "nu", lista)
    lista = adaugaRezervare("4", "londra", "business", 200, "da", lista)
    lista = adaugaRezervare("5", "londra", "economy plus", 500, "da", lista)
    lista = adaugaRezervare("6", "barcelona", "economy", 1000, "da", lista)

    rezultat = sumaPerNume(lista)

    assert rezultat["londra"] == 900
    assert rezultat["milano"] == 290
    assert rezultat["barcelona"] == 1050


