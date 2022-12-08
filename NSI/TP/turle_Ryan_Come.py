from turtle import *
from random import *

down()
speed(10)

def exercice1():
    
    """
    Cette fonction permet de dessiner un carré de 90 pixels de côté. 
    """
    
    up()
    goto(0,0)
    down()
    
    clear()
    
    for i in range(4):
        forward(100)
        right(90)
        
def exercice2(x : int,y : int, largeur : int, hauteur : int, couleur : list or str):
    
    """
    Cette fonction permet de dessiner un rectangle en précisant en argument les coordonnées en format (x,y) du coin en haut à gauche,
    la largeur et la hauteur des côtés et la couleur de ce dernier
    
    NE MARCHE QU'AVEC DES NOMBRES ENTIERS
    """
    
    assert type(x) == int, """Votre argument 'x' n'est pas un nombre"""
    assert type(y) == int, """Votre argument 'y' n'est pas un nombre"""
    assert type(largeur) == int, """Votre argument 'largeur' n'est pas un nombre"""
    assert type(hauteur) == int, """Votre argument 'hauteur' n'est pas un nombre"""
    assert type(couleur) == str or list, """Votre argument 'couleur' n'est ni une liste(r,g,b) ni un nom de couleur en format str"""
    
    up()
    clear()
    
    goto(x, y)
    setheading(0)
    pencolor(couleur)
    
    down()
    
    for i in range(2):
        forward(largeur)
        right(90)
        forward(hauteur)
        right(90)
        
def exercice3():
    
    """
    Cette fonction permet de dessiner la figure de l'exercice 3
    """
    
    clear()
    
    up()
    goto(0,0)
    down()
    
    for i in range(3):
        
        forward(80)
        left(120)
        
        for y in range(4):
            
            forward(20)
            left(120)
            forward(20)
            right(120)
    
        up()
        
        setheading(0)
        forward(100)
                
        down()

def exercice4():
    
    """
    Cette fonction permet de dessiner une suite d'étoiles de plus en plus grandes puis de plus en plus petites
    """
    
    up()
    clear()
    goto(-500,0)
    down()
    
    longueur = 10
    
    for i in range(4):
        
        forward(longueur)
        
        for j in range(4):
            right(144)
            forward(longueur)
        
        up()
        setheading(0)
        forward(longueur+5)
        down()
        longueur += 10
    
    forward(longueur)
    
    for y in range(4):
        right(144)
        forward(longueur)
        
    up()
    setheading(0)
    forward(longueur+5)
    down()
        
    for z in range(4):
        
        longueur -= 10
        
        forward(longueur)
        
        for w in range(4):
            right(144)
            forward(longueur)
        
        up()
        setheading(0)
        forward(longueur+5)
        down()
        
def exercice5(longueur:int):
    
    """
    Cette fonction permet de reproduire la figure de l'exercice 5 en prenant comme argument la longueur que vous souhaitez pour les
    premières formes qui composent la figure
    """
    
    up()
    goto (-70,70)
    down()
    
    longueur_modif = longueur
    pencolor("orange")
    
    for i in range(4):
        forward(longueur)
        right(90)
    
    up()
    forward(longueur + 5)
    down()
    
    for i in range(8):
        
        longueur_modif -= 3
        
        pencolor("blue")
        
        for i in range(3):
            
            forward(longueur_modif)
            right(120)
        
        forward(longueur_modif / 3)
        left(60)
        forward(longueur_modif / 3)
        right(120)
        
        for i in range(3):
        
            forward(longueur_modif)
            right(120)
        
        up()
        forward(longueur_modif + 5)
        down()
        
        pencolor("orange")
        
        for i in range(3):
            forward(longueur_modif)
            right(120)
        
        up()
        forward(longueur_modif + 5)
        down()
        
        pencolor("blue")
        
        for i in range(5):
            
            forward(longueur_modif)
            right(144)
            
        up()
        forward(longueur_modif + 5)
        down()
        
        pencolor("orange")
        
        for i in range(4):
            
            forward(longueur_modif)
            right(90)
            
        up()
        forward(longueur_modif + 5)
        down()
        
    longueur_modif -= 3
        
    pencolor("blue")
        
    for i in range(3):
            
            forward(longueur_modif)
            right(120)
        
    forward(longueur_modif / 3)
    left(60)
    forward(longueur_modif / 3)
    right(120)
        
    for i in range(3):
        
        forward(longueur_modif)
        right(120)
        
    up()
    forward(longueur_modif + 5)
    down()
        
    pencolor("orange")
    
    for i in range(3):
        forward(longueur_modif)
        right(120)
        
    up()
    forward(longueur_modif + 5)
    down()
        
    pencolor("blue")
    
    for i in range(5):
            
        forward(longueur_modif)
        right(144)
           
    up()
    forward(longueur_modif + 5)
    down()
        


##########################################################
#                                                        #
#                      Fonctions                         #
#                                                        #
##########################################################



def stages(couleur):
    
    """
    Cette fonction permet de tracer les étages UNIQUEMENT, les fenêtres et autres seront tracés indépendemment
    """
    
    fillcolor(couleur)
    pencolor("black")
    begin_fill()
    
    for i in range(2):
    
        forward(140)
        left(90)
        forward(60)
        left(90)
        
    end_fill()
        
def door1(couleur):
    
    """
    Cette fonction permet de tracer le premier type de porte en forme de rectangle basique
    """
    
    fillcolor(couleur)
    pencolor("black")
    begin_fill()
    
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(40)
    
    end_fill()

def door2(couleur):
    
    """
    Cette fonction permet de tracer un second type de porte avec le haut en arc de cercle
    """
    
    fillcolor(couleur)
    pencolor("black")
    
    begin_fill()
    
    forward(40)
    up()
    right(90)
    forward(30)
    down()
    left(90)
    
    circle(15,180)
    
    up()
    left(90)
    forward(30)
    down()
    right(90)
    
    forward(40)
    
    end_fill()
    
def roof1():
    
    """
    Cette fonction permet de tracer le premier type de toit plat
    """
    
    fillcolor("black")
    pencolor("black")
    begin_fill()
    
    forward(140)
    left(135)
    forward(100)
    left(90)
    forward(100)
    left(135)
        
    end_fill()
    
def roof2():
    
    fillcolor("black")
    begin_fill()
    
    """
    Cette fonction permet de tracer un second type de toit en triangle
    """
    
    forward(140)
    circle(5,180)
    forward(140)
    circle(5,180)
    
    end_fill()
    
def fenetre():
    
    fillcolor("white")
    begin_fill()
    
    for i in range(4):
        
        forward(30)
        left(90)
    
    end_fill()
    
def fenetre2():
    
    fenetre()
    
    right(90)
    
    pensize(4)
    
    for i in range(2):
        forward(20)
        left(90)
        forward(30)
        left(90)
        
    pensize(1)
    
    position = [pos()[0], pos()[1]]
    n = 0
    
    for i in range(5):
        
            n += 1
            up()
            goto(position[0] + 5 * n, position[1])
            down()
            forward(20)
            
    setheading(0)
    forward(5)
        
        
        
    

##########################################################
#                                                        #
#                 Programme Principal                    #
#                                                        #
##########################################################


list_color = ["blue", "orange", "pink", "red", "brown", "cyan", "yellow", "green", "purple"]
list_indice_color = [i for i in range(len(list_color))]

def couleur_random(L1,L2):
    
    random = randint(0,len(L2)-1)
    couleur = L1[random]
    
    return couleur

up()
goto(-500,-100)
down()

setheading(0)

pencolor("black")

def TP():
    
    """
    Cette fonction permet de réaliser le TP : tracer les batîments avec des contraites précises
    BONUS : Bâtiments générés aléatoirement
    """
    
    nb_bat = 0
    
    for i in range(7):
        rez_de_chaussee = False
        porte = False
        couleur_etage = couleur_random(list_color, list_indice_color)
        couleur_porte = couleur_random(list_color, list_indice_color)
        
        while couleur_etage == couleur_porte:
            couleur_porte = couleur_random(list_color, list_indice_color)
            
        
        for i in range(randint(1,4)): # Selection aléatoire du nombre d'étages : entre 1 et 4
            
            stages(couleur_etage)
            forward(17)
            
            if rez_de_chaussee:
                
                for i in range(3):
                    
                    random = randint(1,2)
                    
                    if random == 1:
                        
                        up()
                        left(90)
                        forward(20)
                        down()
                        right(90)
                        
                        fenetre()
                            
                        up()
                        forward(30)
                        right(90)
                        forward(20)
                        left(90)
                        down()
                        forward(8)
                        
                    elif random == 2:
                        
                        up()
                        left(90)
                        forward(20)
                        down()
                        right(90)
                        
                        fenetre2()
                        
                        forward(8)
                        
                forward(9)
                left(90)
                forward(60)
                left(90)
                forward(140)
                left(180)
                        
            else:
                
                limite_porte = 0
                rez_de_chaussee = True
                
                for i in range(3):
                    
                    limite_porte += 1
                    
                    if limite_porte == 3 and porte == False: # Si il n'y a toujours pas de portes au dernier élément 
                        porte = True
                        
                        left(90)
                        
                        random = randint(1,2)
                        if random == 1:
                            door1(couleur_porte)
                        elif random == 2:
                            door2(couleur_porte)
                            
                        left(90)
                        forward(8)
                            
                    elif porte: # Si il y a déjà une porte
                        
                        up()
                        left(90)
                        forward(20)
                        down()
                        right(90)
                        
                        fenetre()
                            
                        up()
                        forward(30)
                        right(90)
                        forward(20)
                        left(90)
                        down()
                        forward(8)
                        
                        
                    else: # Si il n'y a pas de portes
                        random = randint(1,2)
                        if random == 1:
                            
                            up()
                            left(90)
                            forward(20)
                            down()
                            right(90)
                            
                            fenetre()
                                
                            up()
                            forward(30)
                            right(90)
                            forward(20)
                            left(90)
                            down()
                            forward(8)
                                    
                        elif random == 2:
                            porte = True
                            
                            left(90)
                            
                            random = randint(1,2)
                            if random == 1:
                                door1(couleur_porte)
                            elif random == 2:
                                door2(couleur_porte)
                                
                            left(90)
                            forward(8)
                                
                forward(9)
                left(90)
                forward(60)
                left(90)
                forward(140)
                left(180)
                
        random = randint(1,2)
           
        if random == 1:
            roof1()
                
        elif random == 2:
            roof2()
                
        nb_bat += 1
        
        up()
        goto(-500,-100)
        forward(160 * nb_bat)
        down()
                                
    
            
            
    
    
