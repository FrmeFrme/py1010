# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:17:23 2025
Program som presenterer tekst ut fra et gitt datasett
@author: frode meyer
"""

# Datasett
data = { "Norge": ["Oslo", 0.634], "England": ["London", 8.982], "Frankrike": ["Paris", 2.161], "Italia": ["Roma", 2.873] }
        
# Innhent hvilket land som skal presenteres. Første bokstav konverteres alltid til stor bokstav.
angi_land = str(input("Hvilket land ønsker du informasjon om? ")).capitalize()

# Utfør oppslag i datasettet, og presenter informasjon om landet. Gi info om landet ikke finnes i datasettet
if angi_land in data:
    info = data[angi_land]
    print(f"Land: {angi_land}, Hovedstad: {info[0]}, Befolkning: {info[1]}  [milloner]")
else:
    print("Informasjon om landet finnes ikke.")
