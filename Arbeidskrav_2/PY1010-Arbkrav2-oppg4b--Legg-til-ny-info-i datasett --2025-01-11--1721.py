# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:17:23 2025
Program som utvider dictionary og som printer datasettet etter utvidelsen. Det gjøres også en sjekk
om landet som legges inn allerede finnes fra før av. Hvis det skrives info ut uten at nytt land
legges til.
@author: frode
"""

# Dictionary 
data = { "Norge": ["Oslo", 0.634], "England": ["London", 8.982], "Frankrike": ["Paris", 2.161], "Italia": ["Roma", 2.873] }
    
# Legg inn nytt land. Konverter alltid første bokstav til stor bokstav.    
angi_nytt_land = str(input("Legg inn et nytt land med tilhørende informasjon. Hvilket land? ")).capitalize()
angi_land = angi_nytt_land

# UTfør oppslag - sjekk om landet allerede eksisterer i dictionary og presenter det. Hvis nytt land oppgis bes det om 
# ny info som legges til datasettet
if angi_land in data:
    info = data[angi_nytt_land]
    print(f"Land: {angi_land}, Hovedstad: {info[0]}, Befolkning: {info[1]}  [milloner]")
else:
    # Innhent info om hovedstad og antall innbyggere til det nye landet som er angitt
    angi_hovedstad = str(input("Informasjon om landet legges til. Hva heter hovedstaden i " + str(angi_nytt_land) + "? "))
    angi_antall_innbyggere = str(input("Hvor mange innbyggere har " + str(angi_nytt_land) + "? "))

    # Utvid dictenary
    data[str(angi_nytt_land)] = [str(angi_hovedstad), str(angi_antall_innbyggere)]

# Presenter gjeldende/oppdatert dictionary
print("Dictionary ser slik ut: ", data)
