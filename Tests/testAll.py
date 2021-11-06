from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testGetById
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testIeftinireRezervariCuProcentaj, testTransformareClasaSuperioara, \
    testOrdonareDescresPret, testPretMaxPeClasa, testSumaPerNume


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testGetById()
    testTransformareClasaSuperioara()
    testIeftinireRezervariCuProcentaj()
    testPretMaxPeClasa()
    testOrdonareDescresPret()
    testSumaPerNume()