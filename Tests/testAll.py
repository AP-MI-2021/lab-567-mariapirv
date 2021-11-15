from Tests.testCRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare, test_get_by_id
from Tests.testDomain import test_rezervare
from Tests.testFunctionalitati import test_transformare_clasa_superioara, \
    test_ordonare_descres_pret, test_pret_max_pe_clasa, test_suma_per_nume, test_ieftinire_rezervari_cu_procentaj


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_get_by_id()
    test_transformare_clasa_superioara()
    test_ieftinire_rezervari_cu_procentaj()
    test_pret_max_pe_clasa()
    test_ordonare_descres_pret()
    test_suma_per_nume()