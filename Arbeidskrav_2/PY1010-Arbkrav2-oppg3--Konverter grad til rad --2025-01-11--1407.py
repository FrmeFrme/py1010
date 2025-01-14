# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:03:02 2025
Programmet konverterer fra grader til radianer
@author: frode meyer
"""

import numpy as np

# Innhent gradtall, som skal omregnes til radian-verdi
v_grad = float(input("Skriv inn gradtallet: "))

# Utfør beregning
v_rad = round(v_grad*np.pi/180, 3)

# Presenter resultatet
print(str(v_grad) + " grader tilsvarer radian-verdi: " + str(v_rad))


