import time
import keyboard
from random import *


# Définition de la carte de jeu, sous forme de matrice pour faciliter l'affichage de la carte durant la partie
carte_1 = [  ["#", "I", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
             ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
             ["#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
             ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#"],
             ["#", " ", " ", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", "#"],
             ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0"],
             ["#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
             [" ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
             [" ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " "]
    ]

class Lemming:
    
    def __init__(self, l : int, c : int):
        """
        Arguments :
        l = int, ligne d'apparition
        c = int, colonne d'apparition
        """
        self.l = l
        self.c = c
        self.d = 1
        
    def __str__(self):
        """
        Définition de l'apparence du lemmings dans le jeu en fonction de sa direction
        """
        if self.d == 1 : return ">"
        else: return "<"
        
    def get_ligne(self):
        """
        Renvoie la ligne ou se trouve le Lemming
        """
        return self.l
    
    def get_colonne(self):
        """
        Renvoie la colonne ou se trouve le Lemming
        """
        return self.c
    
    def get_direction(self):
        """
        Renvoie la direction vers laquelle se dirige le Lemming
        1 : Droite
        -1 : Gauche
        """
        return self.d
    
    def avancer(self):
        """
        Modifie la colonne ou se trouve le Lemming en fonction de sa position
        +1 : a droite
        -1 : a gauche
        """
        if self.d == 1 : self.c += 1
        else: self.c -= 1
        
    def retourner(self):
        """
        Fait se retourner le Lemming en changeant sa direction
        """
        if self.d == 1 : self.d = -1
        else: self.d = 1
        
    def tomber(self):
        """
        Fait tomber le Lemming d'une ligne en modifiant la ligne ou il se trouve
        -1 : Tomber
        +1 : Monter (Inutile ici donc pas present)
        """
        self.l -= 1
        
class Case:
    
    def __init__(self):
        """
        Constructeur de la classe Case
        """
        self.__lemming = None
        self.__l = None
        self.__c = None
        
    def set_coordonnees(self, l : int, c : int):
        """
        Attribue aux attributs l et c les arguments l et c
        l = int, ligne
        c = int, colonne 
        """
        self.__l = l
        self.__c = c
    
    def get_terrain(self):
        """
        Renvoie l'élément de terrain correspondant aux coordonnées.
        # : Mur
          : Vide
        < ou > : Lemming
        1 : Lieu d'apparition
        0 : Sortie
        """
        return jeu1.grille[self.__l][self.__c]
    
    def __str__(self):
        """
        Renvoie le resultat de la méthode get_terrain()
        """
        return str(self.get_terrain())
    
    def estLibre(self):
        """
        Renvoie True si la case selectionnée est libre, False si elle ne l'est pas
        """
        return self.get_terrain() == " " 
    
    def liberer(self):
        """
        Libère une case en attribuant à son contenu un vide
        """
        jeu1.grille[self.__l][self.__c] = " "
    
    def occuper(self, lem):
        """
        Modifie le statut de la case : Lui attribue un lemming, l'affichage diffèrera en fonction de la direction du
        Lemming
        """
        jeu1.grille[self.__l][self.__c] = lem.__str__()
        
    def sortie(self):
        """
        Définition de la sortie : si le contenu de la case est 0, il s'agit de la sortie
        """
        return jeu1.grille[self.__l][self.__c] == "0"
        
    
class Jeu:
    
    def __init__(self, carte, spawn : list, arrivee : list):
        """
        Arguments:
        Carte : Carte selectionnée pour la partie : matrice
        spawn : coordonnées d'apparition : liste
        arrivee : coordonnées de la sortie : liste
        """
        self.l_spawn = spawn[0]
        self.c_spawn = spawn[1]
        self.l_arrivee = arrivee[0]
        self.c_arrivee = arrivee[1]
        self.grille = carte
        self.lemmings_en_jeu = [] # Liste des Lemmings présents en jeu, ils sont ajoutés a leur apparition
        self.score = 0
        self.jeu_periode = 0.5 # Intervalle entre chaque mis a jour du jeu en seconde
        self.jeu = True # Pour faire tourner la boucle while du jeu
        self.nombre_lemmings_total = 0
        self.nombre_lemmings_gagnants = 0
        
    def afficher(self):
        """
        Affiche la grille (carte) avec tous ses éléments
        """
        for i in self.grille:
            for y in i:
                print(y, end="")
            print("")
    
    def tour(self):
        """
        Effectue un tour du jeu, déplacement des Lemmings, actualisation du score / statistiques
        """
        for i in range(len(self.lemmings_en_jeu)):
            case_test.set_coordonnees(self.lemmings_en_jeu[i].l + 1, self.lemmings_en_jeu[i].c) # Test de la case en bas
            if case_test.sortie(): # Si c'est la sortie
                case_test.set_coordonnees(self.lemmings_en_jeu[i].l, self.lemmings_en_jeu[i].c)
                case_test.liberer()
                self.score += 10 # Score augmente
                self.nombre_lemmings_gagnants += 1 
                self.lemmings_en_jeu[i].l = 10 # On va enfermer le Lemming dans la zone en bas de la carte
                self.lemmings_en_jeu[i].c = 1 # On va enfermer le Lemming dans la zone en bas de la carte
            if case_test.estLibre(): # Si la case est libre
                self.lemmings_en_jeu[i].l += 1 # Le Lemming tombe
                case_test.occuper(self.lemmings_en_jeu[i]) 
                case_test.set_coordonnees(self.lemmings_en_jeu[i].l - 1, self.lemmings_en_jeu[i].c)
                case_test.liberer()
            else: # Sinon..
                case_test.set_coordonnees(self.lemmings_en_jeu[i].l, self.lemmings_en_jeu[i].c + self.lemmings_en_jeu[i].d) # Case a droite ou a gauche suivant la direction du lemming
                if case_test.sortie(): # Si c'est la sortie
                    case_test.set_coordonnees(self.lemmings_en_jeu[i].l, self.lemmings_en_jeu[i].c)
                    case_test.liberer()
                    self.score += 10 # Le score augmente (10 / Lemming)
                    self.nombre_lemmings_gagnants += 1
                    self.lemmings_en_jeu[i].l = 10 
                    self.lemmings_en_jeu[i].c = 1
                elif case_test.estLibre(): # Si la case est libre
                    self.lemmings_en_jeu[i].c += self.lemmings_en_jeu[i].d # Le Lemming bouge en fonction de sa direction
                    case_test.occuper(self.lemmings_en_jeu[i])
                    case_test.set_coordonnees(self.lemmings_en_jeu[i].l, self.lemmings_en_jeu[i].c - self.lemmings_en_jeu[i].d)
                    case_test.liberer()
                else: # Sinon
                    self.lemmings_en_jeu[i].retourner() # Changement de direction
        
                
        jeu1.afficher() # Affichage du jeu
        print("Score :", self.score) # Affichage du score
        print("Nombre de Lemmings invoques :", self.nombre_lemmings_total)
        print("Nombre de Lemmings sortis :", self.nombre_lemmings_gagnants)
    
    def demarrer(self):
        
        while self.jeu:
            self.tour()
            keyboard.on_press(onkeypress)
            time.sleep(self.jeu_periode)      

def onkeypress(event):
    if keyboard.is_pressed("q"): # Si q est pressé
        keyboard.release("q") # La touche q n'est plus pressé
        time.sleep(0.01)
        jeu1.jeu = False # On stop la boucle du jeu
    if keyboard.is_pressed("space"): # Si espace est pressé
        keyboard.release("space") # La touche espace n'est plus pressée
        time.sleep(0.01) # sleep pour eviter l'apparition de plusieurs lemmings en un clic
        n = randint(1,1000000000000000) # Creation du lemming
        while n in jeu1.lemmings_en_jeu: # Si la valeur de n est deja une instance de la class Lemming, on en redéfinit une (le but est juste de créer des instances de la class Lemming, le nom n'apporte rien)
            n = randint(1,1000000000000000)
        n = Lemming(jeu1.l_spawn, jeu1.c_spawn)
        jeu1.lemmings_en_jeu = jeu1.lemmings_en_jeu + [n] # Ajout du Lemming dans la liste des lemming du jeu
        jeu1.nombre_lemmings_total += 1 
        time.sleep(1) # Délai d'apparition entre chaque Lemming
        
        
jeu1 = Jeu(carte_1, [0,1], [5,17])
case_test = Case()

"""
Note : Pour démarrer le jeu, taper jeu1.demarrer()
Pour Stopper le jeu, appuyer sur q
Pour faire apparaître un lemming, appuyer sur espace

ATTENTION : Stopper le jeu ne veut pas dire le mettre en pause, la partie sera perdue !
"""