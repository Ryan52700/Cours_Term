from math import *
from random import * 

############################################
#|                                        |#
#|                 MP3                    |#
#|                                        |#
############################################

"""
MP3 de Duthé Ryan & Pettazzoni Côme - Terminal
"""

liste_abonnes = []

parking = [
           [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
           [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
           [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
           [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
           [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
          ]

# Componsition du parking : 5 niveau de 8 rangees de 10 places chacune

class Voiture: # Classe Voiture
    
    def __init__(self, m : str, p : str, a : bool):
        
        """
        Construction de la classe Voiture
        
        Arguments :
        m = str
        p = str
        a = boolean
        """
        
        self.__plaque = randint(100000,999999)
        self.__marque = m
        self.__proprio = p
        self.__abonnement = a
        self.__place = -1
        self.__n = -1
        self.__rangee = -1
        self.__etage = -1
        
        if self.__abonnement: self.attribution_abonnement()
        
    def attribution_abonnement(self): # Ajoute la voiture à la liste des abonnés si elle l'est    
        if self.__abonnement:
            liste_abonnes.append(self)
        
    def get_plaque(self): # Obtenir la plaque de la voiture
        return self.__plaque
    
    def get_marque(self): # Obtenir la marque de la voiture
        return self.__marque
    
    def get_proprio(self): # Obtenir le propriétaire de la voiture
        return self.__proprio
    
    def get_abonnement(self): # Savoir si la voiture est abonnée ou non
        return self.__abonnement
    
    def get_place(self): # Obtenir la place de la voiture
        return self.__place
    
    def modif_abonnement(self): # Abonner ou désabonné la voiture
        
        if self.get_abonnement():
            self.__abonnement = False
            liste_abonnes.remove(self)
        else:
            self.__abonnement = True
            liste_abonnes.append(self)
        
    def modif_place(self, place : int, n : int, rangee : int, etage : int, p): # Attribuer / Modifier la place de la voiture
        
        """
        Arguments :
            place, de type int
            n, de type int
            etage, de type int
            p, de type Parking
            
        methode appelee en appelant une methode sur la classe Parking, elle n'est pas censee etre appelee directement !
        
        Sert a modifier la place d'une voiture
        """
                        
        if self.__n != -1:
            p.liste_places[self.__etage][self.__rangee][self.__n] = " "
                
            if self.__abonnement:
                if self.__place in p.liste_places_abonnes:
                    p.liste_places_abonnes.remove(self.__place)
                else:
                    p.liste_places_non_abonnes.remove(self.__place)
                   
            else:
                if self.__place in p.liste_places_non_abonnes:
                    p.liste_places_non_abonnes.remove(self.__place)
                else:
                    p.liste_places_abonnes.remove(self.__place) 
            
        self.__n = n
        self.__rangee = rangee
        self.__etage = etage
            
        self.__place = place
        p.liste_places[etage][rangee][n] = self
    
class Parking: # Classe Parking

    def __init__(self, abonnes, places):
        
        """
        Constructeur de la classe Parking
        
        Arguments :
        abonnes : liste des abonnes creee au prealable
        places : liste des places creee au prealabe
        """
        self.abonnes = abonnes
        self.liste_places = parking
        self.liste_places_abonnes = []
        self.liste_places_non_abonnes = [] 
    
    def infos_voiture(self, voiture : Voiture):
        """
        Argument : voiture, de type Voiture

        Recuperation des informations de la voiture selectionnee. On vient les chercher avec les accesseurs de la class voiture.
        """
        return voiture.get_plaque(), voiture.get_marque(), voiture.get_proprio(), voiture.get_abonnement(), voiture.get_place()
    
    def abonnement(self, voiture : Voiture):
        """
        Argument : voiture, de type Voiture
        
        Modifie le statut de l'abonnement de la voiture : Desabonne si il est abonne et inversement.
        ATTENTION : comme dans la vraie vie, si votre abonnement expire la voiture ne changera pas de place automatiquement. Cependant,
        au prochain stationnement l'acces aux places abonnes sera bel et bien bloque.
        """
        voiture.modif_abonnement()
    
    def affecter_place(self, voiture : Voiture, place : int):
        
        """
        Arguments :
            voiture, de type Voiture
            place, int
            
        Affectation d'une place a une voiture. On renseigne le numero de la place et on cherche a determiner son niveau, sa rangee et
        sa place dans la rangee via des boucles. Toutes les 10 places on passe a la rangee suivante, toutes les 10 rangees on passe au
        niveau suivant. On cherche a determiner les indices pour pouvoir les placer dans le tableau parking directement.
        
        Verification de l'abonnement et de la validite de la place selectionnee par rapport au statut de l'abonnement.
        """

        assert 1 <= place <= 480, """Veuillez selectionner une place entre 1 et 480."""

        if self.verification_place(place): # Vérifie si la place est libre
        
            if voiture.get_abonnement(): # Si la voiture est abonnée - Accès au premier étage réservé aux abonnés
                
                self.liste_places_abonnes.append(place)
               
                n = -1 # On demarre a -1 pour eviter un decalage de 1 (On cherche a determiner les indices et non les numeros de place)
                rangee = 0 
                etage = 0
                
                for i in range(place): # Boucle presentee dans la doc
                    
                    n += 1
                    
                    if n == 10:
                        rangee += 1
                        n = 0
                    
                    if rangee == 8:
                        etage += 1
                        rangee = 0
                
                voiture.modif_place(place, n, rangee, etage, self) # On va modifier la place de la voiture directement dans la class Voiture
                
            else: # Si la voiture n'est pas abonnée
                
                assert 81 <= place <= 480, """Place max : 480, Place min : 81. Pour obtenir l'accès aux places inférieur abonnez-vous"""
                
                self.liste_places_non_abonnes.append(place)
                
                ancienne_place = voiture.get_place()
                n = -1
                rangee = 0
                etage = 0
                
                for i in range(place):
                    
                    n += 1
                    
                    if n == 10:
                        rangee += 1
                        n = 1
                    
                    if rangee == 8:
                        etage += 1
                        rangee = 0
                
                voiture.modif_place(place, n, rangee, etage, self)
                
        else: # Si la place est prise, ecrit :
            
            print("La place est prise, veuillez en selectionner une autre !")
            
    def verification_place(self, place):
        """
        Argument : place, de type int
        
        Verifie que la place selectionnee est bien vide.
        On vient verifier si l'emplacement qui correspond au numero de place entre contient une voiture ou " " (ce qui signifierait que la
        place est vide).
        Vide : renvoie True
        Occupee : Renvoie False
        """
        
        n = -1
        rangee = 0
        etage = 0
            
        for i in range(place): # Meme systeme que dans la methode affecter_place()
                
            n += 1
                
            if n == 10:
                rangee += 1
                n = 0
                
            if rangee == 8:
                etage += 1
                rangee = 0
                
        return self.liste_places[etage][rangee][n] == " " #Renvoie True si elle est vide, False si elle est occupée
    
    def places_libres(self):
        """
        Renvoie le nombre de places libres
        Operation : place_total - place_occupes
        
        On utilise pour cela les tableau self.liste_places_non_abonnes et self.liste_places_abonnes qui sont remplis a l'affectation d'une
        place. On distingue les abonnes et les non-abonnes car on ne melange pas les torchons et les seviettes. (D'un point de vue
        administratif, c'est bien plus pratique pour un vraie parking de les différencier, par exemple pour les services que l'on peut
        leur apporter)
        """
        
        return "{} places libres abonnees et {} non-abonnees".format(80 - len(self.liste_places_abonnes), 400 - len(self.liste_places_non_abonnes))
    
    def representation(self, niveau):
        """
        Argument : niveau, int
        
        Reperesentation textuel du parking.
        
        On utilise "|" pour representer les murs et "¤" pour les voitures. On vient simplement afficher les differentes rangees selon le
        niveau selectionne.
        
        Note : le choix du format de laa variable parking ligne 16 prend tout son sens : l'affichage de tableau est simple.
        
        Renvoie egalement le nom des proprietaires et les plaques des voitures garees par rangee dans l'ordre de gauche a droite
        """
        
        assert 0 < niveau <= 8, """Il n'y a que 8 niveau, veuillez entrer un chiffre entre 1 et 8."""
        
        print("|", end = " ")
        
        for p in range(9):
            print(p+1, end = " ")
            
        print("10", end = "")    
        print("|")
        
        for i in range(8):
            
            liste_stationnement = []
            
            
            print("|", end=" ")
            for y in range(10):
                if self.liste_places[niveau-1][i][y] != " ":
                    print("¤", end=" ")
                    liste_stationnement.append((self.liste_places[niveau-1][i][y].get_proprio(), self.liste_places[niveau-1][i][y].get_plaque()))
                else:
                    print(" ", end=" ")
             
            if len(liste_stationnement) == 0:
                print("|")
            
            else:
                print("|", liste_stationnement)
        
            

# Lignes pour vérifier que tout marche bien :

parking = Parking(liste_abonnes, parking) # Initialisation d'une instance de la classe Parking 
voiture1 = Voiture("Opel","Come",True) # Initialisation d'une instance de la classe Voiture
voiture2 = Voiture("Renaut", "Ryan", True) # Initialisation d'une instance de la classe Voiture
voiture3 = Voiture("Dacia", "Maxime", True) # Initialisation d'une instance de la classe Voiture
print(parking.infos_voiture(voiture1)) # Verification de la recuperation d'informations des voitures dans la classe Parking
parking.affecter_place(voiture1,6) # Affecter les places
parking.affecter_place(voiture2,6) # Affecter les places - Verification que si une place est occupee, la seconde voiture ne se gare pas
parking.affecter_place(voiture3,7) # Affecter les places
print(parking.liste_places_abonnes) # Liste des places des abonnes occupees
print(parking.liste_places) # Liste totale des places du parking
parking.affecter_place(voiture2,18) # Affectation d'une place
print(parking.liste_places_non_abonnes) # On voit que les places occupees par des abonnes ne sont pas ajoutees dans la listes des non-abonnes
print(parking.liste_places) # Liste totale des places du parking
print(parking.verification_place(6)) # Verifie si la place est vide
print(parking.verification_place(18)) # Verifie si la place est vide
print(parking.verification_place(188)) # Verifie si la place est vide
print(parking.places_libres()) # Renvoie le nombre de places libres (400 - places occupees)
parking.representation(1) # Representation de l'etage 1 (ou sont placees les voitures)