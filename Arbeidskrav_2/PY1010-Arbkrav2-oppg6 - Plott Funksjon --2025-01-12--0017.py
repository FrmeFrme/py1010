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
plt.close('all')
plt.plot(xa, f(xa))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funksjonen f(x) = -x² - 5')
plt.legend(labels=('f(x) = -x² - 5'))

# Vis plottet
plt.show()

