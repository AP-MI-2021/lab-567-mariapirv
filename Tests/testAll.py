from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare
from Tests.testDomain import testRezervare

def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()