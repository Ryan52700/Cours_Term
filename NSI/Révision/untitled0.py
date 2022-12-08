# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:09:17 2022

@author: Elève
"""

from random import *

# Exercice 1

def exercice_1():

    liste = [45, 17, 89, 38, 10, 74]
    
    liste.sort()
    print(liste)
    print("")
    
    liste.append(12)
    print(liste)
    print("")
    
    liste.reverse()
    print(liste)
    print("")
    
    indice = 0
    for i in liste:
        
        if i == 10:
            
            print(indice)
            indice += 1
            
        else:
            indice += 1
            
    print("")
            
    print(liste[-1])
    print("")
    
    for i in range(len(liste)):
        
        print(i, end = " ; ")
    
    print("")
    
    for i in range(len(liste)):
        
        print(liste[i], end = " ; ")
        
    print("")
    print("")
    
    for i in liste:
        print(i, end = " ; ")
    
# Exercice 2

def generate_tab(n, mini, maxi):
    
    nouvelle_liste = []
    
    for i in range(n):
        
        nouvelle_liste.append(randint(mini,maxi))
    
    print(nouvelle_liste)
    
# Exercice 3

def exercice3():

    chaine1 = "abc"
    chaine2 = "de"
    
    liste = []
    
    for i in range(len(chaine1)):
        
        for y in range(len(chaine2)):
            
            liste.append(chaine1[i] + chaine2[y])

    print(liste)

# Exercice 4

def occurence(lettre, chaine):
    
    occu = 0
    
    for i in chaine:
        
        if i == lettre:
            
            occu += 1 
            
    return occu

# Exercice 5

def moyenne(tab):
    
    assert len(tab) > 0, """Erreur"""
    
    somme = 0
    
    for i in tab:
        somme += i
        
    return(somme / len(tab))
    
# Exercice 6

def recherche(lst, nombre):
    
    occurence = -1
    
    for i in range(len(lst)):
        
        if lst[i] == nombre:
            
            occurence = i
    
    if occurence == -1 :
        
        return len(lst)
    
    else:
        
        return occurence
    
# Exerice 7

def recherchebis(elt, tab):
    
    for i in range(len(tab)):
        
        if tab[i] == elt:
            
            return i
        
    return -1

# Exercice 7 bis

def recherchebisbis(elt, tab):
    
    loop = True
    occurence = False
    indice = 0
    
    while loop:
        
        if tab[indice] == elt :
            occurence = True
            loop = False
            
        elif indice >= len(tab):
            loop = False
            
        else:
            indice += 1
    
    print(occurence)
    
    if occurence: 
        return indice
    
    else:
        return -1

# Exercice 8

liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []

    for compteur in range(len(liste_eleves)):
        
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
            
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]

    return (note_maxi,nb_eleves_note_maxi,liste_maxi)


