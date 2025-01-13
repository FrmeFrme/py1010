# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:07:16 2025
PY1010-Arbeidskrav2-Oppg1-Beregn-Alder-et-gitt-år
Program beregner alder som personer blir i løpet av et gitt år, her 2024. 
Skriv svar til skjerm.
Med variabel vil det være enkelt å korrigere det for nytt valgt år, f.eks 2025
@author: frode meyer
"""

# Hvilket år skal programmet beregnet alder ut fra. Oppdatert til 2025 ved neste anledning.
valgt_ar = 2024

#Innhent fødselår som det skal beregnes alder/hvilket år som fylles
fodselsar = int(input("Hvilket år er du født? "))

# Beregn alder som fylles i løpet av valgt år
beregn_alder = valgt_ar - fodselsar

# Presenter beregnet alder
print("Alderen i løpet av året " + str(valgt_ar) + " er: " + str(beregn_alder) + " år")

