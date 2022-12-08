from math import *

#--------------------------------------
#|                                    |
#|            Exercice 3              |
#|                                    |
#--------------------------------------

class Angle:

    def __init__(self, angle):
        
        self.__angle = self.calcul_angle(angle)
        self.__cosinus = self.calcul_cosinus()
        self.__sinus = self.calcul_sinus()

    def calcul_angle(self,angle):

        if angle >= 360:
            return angle - 360
        else:
            return angle

    def afficher(self):

        print("{} degrès".format(self.__angle))

    def ajoute(self, angle_ajoute):

        if self.__angle + angle_ajoute >= 360:
            self.__angle += angle_ajoute - 360
        
        else:
            self.__angle += angle_ajoute

    def calcul_sinus(self):
        return sin((self.__angle*pi) / 180)
    
    def calcul_cosinus(self):
        return cos((self.__angle*pi) / 180)

    def get_angle(self):
        return self.__angle
    
    def get_cosinus(self):
        return self.__cosinus

    def get_sinus(self):
        return self.__sinus

#Angle1 = Angle(359)
#Angle1.afficher()
#print(Angle1.get_angle())
#print(Angle1.get_sinus())
#print(Angle1.get_cosinus())

#--------------------------------------
#|                                    |
#|            Exercice 4              |
#|                                    |
#--------------------------------------

class Date:

    def __init__(self, d, m, a):
        
        assert type(m) == int,"""Vous devez rentrer le mois par son nombre et non son nom complet !"""

        self.__jour = d
        self.__mois = m
        self.__annee = a

        self.__liste_mois = ["janvier", "fevrier", "mars", "avril", "mai","juin", "juillet", "aout",
        "septembre", "octobre", "novembre", "decembre"]

    def afficher(self):
        return("{} {} {}".format(self.__jour, self.__liste_mois[self.__mois - 1], self.__annee))

    def anterieurA(self,date):
        if date.__annee < self.__annee:
            print("La date entrée est antérieur à la date initiale")
        elif date.__mois < self.__mois and date.__annee == self.__annee:
            print("La date entrée est antérieur à la date initiale")
        elif date.__jour < self.__jour and date.__mois == self.__mois and date.__annee == self.__annee:
            print("La date entrée est antérieur à la date initiale")
        else:
            print("La date entrée n'est pas antérieur à la date initiale")

#date1 = Date(8,6,2004)
#date2 = Date(7,9,2004)
#print(date1.afficher())
#print(date1.afficher())
#date1.anterieurA(date2)

#--------------------------------------
#|                                    |
#|            Exercice 1              |
#|                                    |
#--------------------------------------

class Personnage:

    def __init__(self,x,y,z):

        self.__x = x
        self.__y = y
        self.__z = z

    def avance(self):

        self.__x += 1

    def droite(self):
        
        self.__y += 1
        
    def saute(self):
        
        self.__z += 1
        
    def coord(self):
        
        return self.__x, self.__y, self.__z

#Laura = Personnage(0,0,0)
#Laura.saute()
#Laura.saute()
#Laura.droite()

#print(Laura.coord())

#--------------------------------------
#|                                    |
#|            Exercice 2              |
#|                                    |
#--------------------------------------

# Ce programme permet d'afficher la moyenne sur les 100 lancés de pièces comparable au jeu
# "Pile ou Face". On peut définir des probabilités de cette manière même si ici on sait déjà qu'elle
# Sera égale à 50% environ

#--------------------------------------
#|                                    |
#|            Exercice 3              |
#|                                    |
#--------------------------------------

class Carre:
    
    def __init__(self,c):
        
        self.__longueur_cote = c
    
    def perimetre(self):
        return self.__longueur_cote*4
    
    def aire(self):
        return self.__longueur_cote**2

#carre1 = Carre(5)
#carre2 = Carre(9)
#carre3 = Carre(3)

#--------------------------------------
#|                                    |
#|            Exercice 4              |
#|                                    |
#--------------------------------------

class Eleve:
    
    def __init__(self,n):
        
        self.__nom = n
        self.__notes = []
        self.__moyenne = self.calculer_moyenne()
        
    def calculer_moyenne(self):
        
        if len(self.__notes) == 0:
            return "Pas de notes , Pas de moyenne"
        
        moyenne = 0
        n = 0
        
        for i in self.__notes:
            moyenne += i
            n += 1
        
        return moyenne / n
    
    def ajouter_note(self,note):
        self.__notes.append(note)
        
    def get_nom(self):
        return self.__nom

    def get_notes(self):
        return self.__notes
    
    def get_moyenne(self):
        return self.calculer_moyenne()
    
eleve1 = Eleve("Tom")
print(eleve1.get_moyenne())
eleve1.ajouter_note(15)
print(eleve1.get_moyenne())

#--------------------------------------
#|                                    |
#|            Exercice 5              |
#|                                    |
#--------------------------------------

class Temps:
    
    def __init__(self, h, m, s):
        
        self.__heure = h
        self.__minute = m
        self.__seconde = s
        
        while self.__seconde >= 60:
            
            self.__seconde -= 60
            self.__minute + 1
        
        while self.__minute >= 60:
            
            self.__minute -= 60
            self.__heure += 1
    
    def __str__(self):
        return str(self.__heure) + "h", str(self.__minute) + "m", str(self.__seconde) + "s"
    
    def __add__(self,n,u):
        
        if u == "h":
            
            self.__heure += n
        
        elif u == "m":
            
            self.__minute += n
            
            while self.__minute >= 60:
            
                self.__minute -= 60
                self.__heure += 1        
        
        elif u == "s":
            
            self.__seconde += n
            
            while self.__seconde >= 60:
            
                self.__seconde -= 60
                self.__minute += 1   
            
            while self.__minute >= 60:
            
                self.__minute -= 60
                self.__heure += 1
        
    def __sub__(self, heure_sub):
                
        heure_diff = self.__heure - heure_sub.__heure
        minute_diff = self.__minute - heure_sub.__minute
        seconde_diff = self.__seconde - heure_sub.__seconde 
        
        seconde_diff += heure_diff * 3600 + minute_diff * 60
        minute_diff = 0
        heure_diff = 0
        
        if seconde_diff < 0:
            seconde_diff = seconde_diff * -1
        
        while seconde_diff >= 60:
            
            seconde_diff -= 60
            minute_diff += 1
        
        while minute_diff >= 60:
            
            minute_diff -= 60
            heure_diff += 1
            
        return str(heure_diff) + "h", str(minute_diff) + "m", str(seconde_diff) + "s"
        
                
#heure1 = Temps(22,54,59)
#heure2 = Temps(23,59,59)
#print(heure1.__sub__(heure2))
#heure1.__add__(1, "s")
#print(heure1.__str__())

#--------------------------------------
#|                                    |
#|            Exercice 6              |
#|                                    |
#--------------------------------------

class Vecteur:
    
    def __init__(self,x,y,z):
        
        self.__x = x
        self.__y = y
        self.__z = z
        
    def __add__(self, vecteur2):
        return [self.__x + vecteur2.__x, self.__y + vecteur2.__y, self.__z + vecteur2.__z]
    
    def norme(self):
        return sqrt(self.__x**2 + self.__y**2 + self.__z**2)
    
    def __mul__(self, vecteur2):
        return self.norme() * vecteur2.norme() * ((self.__x * vecteur2.__x + self.__y * vecteur2.__y + self.__z * vecteur2.__z) / sqrt((self.__x ** 2 + self.__y ** 2 + self.__z ** 2 ) * (vecteur2.__x ** 2  + vecteur2.__y ** 2 + vecteur2.__z ** 2)))
    
    def is_colin(self, vecteur2):
        if self.__mul__(vecteur2) == self.norme() * vecteur2.norme(vecteur2) or self.__mul__(vecteur2) == -(self.norme(self) * vecteur2.norme(vecteur2)):
            
            return True

        else:
            
            return False
        
    def is_ortho(self, vecteur2):
        
        if self.__mul__(vecteur2) == 0:
            
            return True
        
        else:
            
            return False
        
vecteur1 = Vecteur(1,2,3)
vecteur2 = Vecteur(1,2,3)

print(vecteur1.norme())
print(vecteur1.__mul__(vecteur2))