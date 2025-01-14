# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:16:38 2025
Programmet regner ut arealet og ytre omkret av en figur sammensatt av en rettviklet
trekant og en halvsirkel der hvor en av katetrene normal skal være.
@author: frode meyer
"""

import numpy as np
import math

# Opprett en funksjon
def beregn_areal_og_omkrets(kat_a, kat_b):
    # Beregn areal av trekant
    areal_trekant = kat_a*kat_b/2
    # Finn radius av sirkel, benyttes i formel nedenfor
    r = kat_a/2
    # Beregnet arealet av halvsirkel (først arealet av hele sirkelen, deretter halvsirkelen)
    areal_sirkel = math.pi*r**2
    areal_halvsirkel = areal_sirkel/2
    # Beregn hypotesen i trekanten, benyttes i formel nedenfor
    hypotenus_trekant = math.sqrt(kat_a**2 + kat_b**2 )
    # Beregn omkrets av de to frittstående sidene i trekanten
    omkrets_trekant_to_kateter = kat_b + hypotenus_trekant
    # Beregn omkrets av sirkel (først omkretsen av hele sirkelen, deretter halvsirkelen)
    omkrets_sirkel = 2*math.pi*r
    omkrets_halvsirkel = omkrets_sirkel/2
    # Beregn sanlet areal og samlet omkrets av figuren
    total_areal_local = round(areal_trekant + areal_halvsirkel, 2)
    total_omkrets_local = round(omkrets_trekant_to_kateter + omkrets_halvsirkel, 2)
    # Returner beregende verider av total areal og tatal omkrets
    return total_areal_local, total_omkrets_local
    

# Innhent lengdene i kateterene a og b (den ene kateteren er tilsvarende diameter av halvsirkelen)
kateter_a = float(input("Hva er lengden av kateter a [cm]? "))
kateter_b = float(input("Hva er lengden av kateter b [cm]? "))

# Utfør beregning ved å kalle på funksjonen
(total_areal, total_omkrets) = beregn_areal_og_omkrets(kateter_a, kateter_b) 

# Presenter resulatet av areal og omkrets av figuren
print(str("Den sammensatte trekant og halvsirkel har arelet: " + str(total_areal) + "[cm²]" + " og omkrets: " + str(total_omkrets) + "[cm]" ))    
    
    