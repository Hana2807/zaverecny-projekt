#!/usr/bin/env python3
from klient import Klient

"""
Trida zajisti funkce 1-3: pridavani novych klientu, vypsani seznamu stavajicich klientu a vyhledavani klientu.
"""
class Evidence:
    def __init__(self):
        self.seznam = []

    def pridej(self): #volba 1: vyzada si udaje a prida klienta do seznamu
        jmeno = str(input("Zadejte jmeno pojisteneho: "))
        prijmeni = str(input("Zadejte prijmeni pojisteneho: "))
        vek = int(input("Zadejte vek: "))
        telefon = int(input("Zadejte telefonni cislo: "))
        klient = Klient(jmeno, prijmeni, vek, telefon)
        self.seznam.append(klient)
        print("Data  byla ulozena.")

    def vypis(self): #volba 2: vypise seznam stavajicich klientu
        for klient in self.seznam:
            print(klient)

    def vyhledej(self): # volba 3: vyzada si jmeno a prijmeni klienta a vyhleda klienta v seznamu
        jmeno = input("Zadejte jmeno pojisteneho: ")
        prijmeni = input("Zadejte prijmeni pojisteneho: ")

        for klient in self.seznam:
            if jmeno == klient.jmeno and prijmeni == klient.prijmeni:
                print(klient)
                return

        print("Tento klient neni v dabatazi.")

