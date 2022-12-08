from Liste.py import *

class Pile:
    
    def __init__(self):
        self.pile = []
        
    def __str__(self):
        return str(self.pile)
    
    def pile_vide(self): # Return True si la pile est vide, False si elle est pleine
        return len(self.pile) == 0
    
    def empiler(self,n):
        self.pile.append(n)
        
    def depiler(self):
        return self.pile.pop()
        
    def sommet(self):
        return self.pile[-1]
    
    def taille(self):
        return len(self.pile)
    
# pile1 = Pile()
# pile1.empiler(5)
# pile1.empiler(1)
# pile1.empiler(9)
# pile1.empiler(3)
# pile1.empiler(8)
# print(pile1.depiler())
# print(pile1.sommet())
# print(pile1)

class File:
    
    def __init__(self):
        self.file = []
        
    def __str__(self):
        return str(self.file)
        
    def file_vide(self):
        return len(self.file) == 0
    
    def ajout(self, n):
        self.file = [n] + self.file
        
    def retire(self):
        self.file.pop(0)
    
    def premier(self):
        return self.file[-1]
    
    def taille(self):
        return len(self.file)

# file1 = File()
# file1.ajout(5)
# print(file1)


    

