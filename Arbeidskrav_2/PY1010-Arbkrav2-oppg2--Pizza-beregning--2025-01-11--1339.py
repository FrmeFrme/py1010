# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:38:55 2025
Pizza anskaffelses program ut fra antall deltakere i klassefest. 
Tallet runder av desimal til nærmeste heltall oppover for å sikre nok pizzaer 
@author: frode meyer
"""

import math

# Innhent antall eleversom deltar på klassefesten, og angi hva som er forbruk pr elev
antall_elever = int(input("Skriv inn antall elever: "))
forbruk_pr_elev = 1/4

# Utfør bergning, til nærmeste hele pizza med avrunding oppover
beregn_antall_pizza_anskaffelse = math.ceil(antall_elever*forbruk_pr_elev)

# Presenter resultatet i hele pizzaer
print("Det må handles inn: " + str(beregn_antall_pizza_anskaffelse) + " stk pizzaer til festen")

