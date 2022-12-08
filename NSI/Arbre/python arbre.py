class ABR:
    def __init__(self,val):
        self.valeur=val
        self.gauche=None
        self.droit=None
    def inserer(self,x):
        if x<self.valeur:
            if self.gauche!=None:
                self.gauche.inserer(x)
            else:
                self.gauche=ABR(x)
        else:
            if self.droit!=None:
                self.droit.inserer(x)
            else:
                self.droit=ABR(x)
                
    def taille(self):
        
        if self == None:
            return 0
        else:
            return 1 + ABR.taille(self.gauche) + ABR.taille(self.droit)
        
    def hauteur(self):
        
        if self is None:
            return -1
        elif self.gauche is None and self.droit is None:
            return 0
        else:
            return 1 + max(ABR.hauteur(self.gauche), ABR.hauteur(self.droit))
    
    def affiche(self):
        
        if self == None:
            return None
        else:
            return [self.valeur, ABR.affiche(self.gauche), ABR.affiche(self.droit)]
    
arbre = ABR(51)
arbre.inserer(51)
arbre.inserer(53)
arbre.inserer(18)
arbre.inserer(22)
print(arbre.affiche())
print(arbre.taille())
print(arbre.hauteur())