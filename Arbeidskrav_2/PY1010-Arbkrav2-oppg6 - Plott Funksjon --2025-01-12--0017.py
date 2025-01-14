# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:16:15 2025
Programmet plotter funksjonen f(x) = -x^2 - 5 for intervallet hvor x har verdiområdet: [-10,10]
@author: frode meyer
"""

import numpy as np
import matplotlib.pyplot as plt

# Opprett en funksjon
def f(x):
    return -x**2 - 5

# Definer rekke med tall fra nedre til øvre grense, og med oppløsning
xa = np.linspace(-10,10, 200)

# Plott funksjonen med oppgitt nedre og øvre grense, med 200 punktsoppløsning
# med beskrivelse og tittel

# Slett eventuelt tidligere grafer
plt.close('all')

# Grafen som skal plottes, med etikett beskrivelse
plt.plot(xa, f(xa), label='f(x) = -x² - 5')  # Legg til etikett for funksjonen

# Legg til en vertikal linje ved x=0
plt.axvline(x=0, color='black', linestyle='--')  # Vertikal linje ved x-aksens verdi 0

# Legg til tekst til x og y aksen
plt.xlabel('x-verdi')
plt.ylabel('y-verdi')

#L Legg til tittel til grafen
plt.title('Graf til funksjonen f(x) = -x² - 5')
plt.legend()

# Vis plottet
plt.show()

