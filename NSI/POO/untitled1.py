# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:41:34 2022

@author: Elève
"""

from math import *

class Chrono:
    "une classe pour représenter le temps mesuré en heures, minutes et secondes"
    
    def __init__(self, h, m, s):
        
        "le constructeur prend comme arguments temps, minutes et secondes"
        self.heures = h
        self.minutes = m
        self.secondes = s
        
    def display(self):
        """ affiche les heures, minutes, secondes"""
        return (str(self.heures) + "h"
        + str(self.minutes) + "m"
        + str(self.secondes) + "s")
    
    def __str__(self):
        """ affiche les heures, minutes, secondes"""
        return (str(self.heures) + "h"
        + str(self.minutes) + "m"
        + str(self.secondes) + "s")
    

### Programme principal

# t = Chrono(11,51,46)
# print(t.display())
# print(t.heures,t.minutes,t.secondes)
# t1 = Chrono(11,57,23)
# print(t1.display())
# t2 = Chrono(52,34,12)
# print(t2.secondes)

class Dinosaure:
    
    def __init__(self, longueur, hauteur, poids, vitesse_max):
        
        """
        Summary : Dinosaure
        
        Attributs :
        longueur & hauteur : meters
        poids : tons
        vitesse_max : km / h
        """

        self.longueur = longueur
        self.hauteur = hauteur
        self.poids = poids
        self.vitesse_max = vitesse_max
        
    def __str__(self):
        
        return (str(self.longueur) + " mètres de longueur ; "
        + str(self.hauteur) + " mètres de hauteur ; "
        + str(self.poids) + " Tonnes ; "
        + str(self.vitesse_max) + " km/h ")
    
    def get_mass(self):
        
        """
        Summary
        Affiche la masse du dinosaure
        """
    
        return self.poids
    
    def set_mass(self,m1):
        """
        Summary
        Change la masse du dinosaure pour m1
        """
        
        self.poids = m1
        
# triceratops = Dinosaure(9,3,9,32)
# print("Triceratops :", triceratops)
# Tyrannosaurus_Rex = Dinosaure(13, 6, 8, 27)
# print("Tyrannosaurus_Rex :", Tyrannosaurus_Rex)
# print(triceratops.__init__.__doc__)
# Dinosaure.get_mass(triceratops)

class Point:
    
    def __init__(self, x,y):

        """
        Constructeur de la classe Point
        Arguments :
        x = abscisse du point
        y = ordonné du point
        """
        
        self.__x = x
        self.__y = y
        self.__r = self.calcul_r()
        self.__theta = self.calcul_theta()
    
    def calcul_r(self):

        """
        Calcul de self.__r
        """
        return sqrt(self.__x*self.__x + self.__y*self.__y)
        
    def calcul_theta(self):

        """
        Calcul de self.__theta
        """
        
        if self.__x > 0:
            return atan(self.__y / self.__x)
            
        elif self.__x < 0 and self.__y >= 0:
            return atan(self.__y / self.__x) + pi
            
        elif self.__x < 0 and self.__y < 0:
            return atan(self.__y / self.__x) - pi
            
        elif self.__x == 0 and self.__y > 0:
            return pi / 2
            
        elif self.__x == 0 and self.__y < 0:
            return -pi / 2
            
        elif self.__x == 0 and self.__y == 0:
            return 0
            
    def get_x(self):

        """
        Renvoie x
        """
        return self.__x
    
    def get_y(self):

        """
        Renvoie y
        """
        return self.__y
        
    def get_r(self):

        """
        Renvoie r
        """

        return self.__r
    
    def get_theta(self):

        """
        Renvoie theta
        """

        return self.__theta
        
P1 = Point(5,0)
P2 = Point(5,5)
P3 = Point(0,5)

print(P1.get_r())