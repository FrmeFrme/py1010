# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:50:34 2024

@author: frme - Frode Meyer
"""

K = 15000 # forventet kjørelengde i [km]

Fel = 5000 # Forsikringskostnad El-bil [kr/år]

Fbe = 7500 # Forsikringskostnad Bensin bil [kr/år]

Trforsikrdag = 8.38 # Trafikkforsikringsavgift [kr/dag] (både elbil og bensinbil)

Drforbr = 0.2 # Drivstofforbruk Elbil [kWh/km]

Stromkostn = 2.00 # Strømkostnad [kr/kWh]

Bekostnkn = 1.0 # Bensinkostnader pr kjørte km [kr/km]

ElbilBomavgiftkm = 0.1 # Elbil bomavgift pr kjørte km [kr/km]

BebilBomavgiftkm = 0.3 # Elbil bomavgift pr kjørte km [kr/km]


Elkostn = Fel + (365 * Trforsikrdag) + (K * Stromkostn * Drforbr) + (K * ElbilBomavgiftkm)

print(' El-bil-kostn =', Elkostn, ' kr/år')

 

Bekostn = Fbe + (365 * Trforsikrdag) + (K * Bekostnkn) + (K * BebilBomavgiftkm )

print(' Bensin-bil-kostn =', Bekostn, ' kr/år')