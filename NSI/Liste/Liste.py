class Maillon :
    def __init__(self,valeur=None):
        self.val = valeur
        self.suiv = None # Pas de maillon suivant
    
class ListeC :
    def __init__(self):
        self.tete = None # Liste vide
    
    def est_vide(self):
        return self.tete == None
    
    def __str__(self):
        if self.tete == None :
            affichage = "[]" 
        else :
            m = self.tete
            affichage = "[" + str(m.val)
            while m.suiv is not None:
                m = m.suiv
                affichage += ", " + str(m.val)
        return affichage + "]"
    
    def taille(self):
        if self.tete == None :
            taille_liste = 0 
        else :
            m = self.tete
            taille_liste  = 1
            while m.suiv is not None:
                m = m.suiv
                taille_liste += 1
        return taille_liste
    
    def get_maillon_indice(self,i):
        assert 0 < i < self.taille() - 1 , " abruti "
        m = self.tete
        for i in range(1,i+1):
            m = m.suiv
        return m.val
    
    def get_dernier_maillon(self):
        if self.tete == None :
            dernier_maillon = "Pas de maillon"
        else :
            m = self.tete
            while m.suiv is not None :
                m = m.suiv
        return m.val
    
    def ajouter_debut(self,M):
        """ Ajoute le maillon M en tÃªte de la liste L """
        M.suiv = L.tete
        L.tete = M
    
    def ajouter_fin(self,M):
        M.suiv = self.get_dernier_maillon()
        M = M.suiv
    
    def ajouter_apres(self, i, M):
        m = self.getMaillonIndice(i)
        M.suiv = m.suiv
        m.suiv = M
    
    def supprimer_debut(self):
        t = L.tete
        L.tete = L.tete.suiv
        return t
    
    def supprimer_fin(self):
        t = L.tete
        while m.suiv.suiv is not None :
            m = m.suiv
        m.suiv = None
        return m
    
    def supprimer_apres(self,i):
        m= self.getMaillonIndice(i)
        m.suiv = m.suiv.suiv
        return m


# L = ListeC()
# print(L.est_vide())
# M1 = Maillon(5)
# M2 = Maillon(7)
# L.tete = M1
# print(L)
# M1.suiv = M2
# print(L.est_vide())
# print(L)
# M3 = Maillon(9)
# M2.suiv = M3
# print(L)
# print(L.taille())
# print(L.get_dernier_maillon())
# M4,M5,M6,M7 = Maillon(1),Maillon(2),Maillon(8),Maillon(6)
# M3.suiv = M4
# M4.suiv = M5
# M5.suiv = M6
# M6.suiv = M7
# print(L)
# print(L.get_maillon_indice(2))
# M7 = Maillon(5)
# L.ajouter_debut(M7)
# print(L)
# L.ajouter_fin(M7)
#print(L)

class Liste_lc:
    
    def __init__(self):
        self.pile = ListeC()
        
    def taille_lc(self):
        return self.pile.taille()
    
    def enpiler_lc(self, x):
        if self.pile.taille() == 0:
            self.pile.ajouter_debut(x)
        else:
            self.pile.ajouter_fin(x)
    
    def __str__(self):
        return str(self.pile)
    
    def depiler_lc(self):
        a = self.pile.supprimer_fin()
        return a
    
    def sommet_lc(self):
        m = self.pile.get_dernier_maillon()
        return m.val
    
    def supprimer_debut(self):
        t = self.tete
        self.tete = self.tete.suiv
        return t
    
    def supprimer_fin(self):
        m = self.tete
        while m.suiv.suiv is not None:
            m = m.suiv
        m.suiv = None
        return m