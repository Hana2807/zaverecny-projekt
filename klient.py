#!/usr/bin/env python3

"""
Trida reprezentuje klienta a udaje, ktere kazdemu zaznamu nalezi, tj. jmeno, prijmeni, vek a telefonni cislo.
"""

class Klient:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    # vraci textovou reprezentaci klienta
    def __str__(self):
        return ("{0}\t{1}\t{2}\t{3}").format(self.jmeno, self.prijmeni, self.vek, self.telefon)
    




