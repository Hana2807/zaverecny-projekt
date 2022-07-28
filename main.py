#!/usr/bin/env python3
import os
from evidence import Evidence

evidence = Evidence()

opakovat = True
while opakovat:
    os.system('cls') #cisti obrazovku
    print("Evidence pojistenych")

    # textova reprezentace volby jednotlivych operaci na zaklade ciselne volby
    print("1 - Pridat noveho pojisteneho")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojisteneho")
    print("4 - Konec")

    vstup = input("Vyberte si akci: ") #vyzada si vstup ve forme cisla
    if vstup.isnumeric(): #osetri, ze vstup je cislo
        cislo_operace = int(vstup)
        if cislo_operace == 1:
            evidence.pridej()
        elif cislo_operace == 2:
            evidence.vypis()
        elif cislo_operace == 3:
            evidence.vyhledej()
        elif cislo_operace == 4: # ukonci program
            opakovat = False
            print("Zavreli jste evidenci.")
        else:
            print("Zadat lze pouze cisla 1-4.") # osetri, ze cislo je 1-4
    else:
        print("Zadat lze pouze cisla 1-4.") # osetri, ze cislo je 1-4

    os.system('pause')