from math import *
from random import *

# dico = {"1" : "un", "2" : "deux", "3" : "trois"}
# print(dico.keys())
# print(dico.values())
# print(dico.items())

# Exercice 1

# personnage = {1 : ("Come", "16 ans", "NSI / MATHS"), 2 : ("Ryan", "16 ans", "NSI / MATHS"), 3 : ("Maxime", "16 ans", "NSI / MATHS"), 4 : ("Martin", "16 ans", "CHOMEUR")}
# 
# random = randint(1, len(personnage))
# print(personnage[random])

personnage = {1 : ("Come", "16 ans", "NSI / MATHS"), 2 : ("Ryan", "16 ans", "NSI / MATHS"), 3 : ("Maxime", "16 ans", "NSI / MATHS"), 4 : ("Martin", "16 ans", "CHOMEUR")}

liste_cle = personnage.keys()
liste_cle = list(liste_cle)
indice_random = randint(0,len(liste_cle) - 1)
cle = liste_cle[indice_random]
print(personnage[cle])