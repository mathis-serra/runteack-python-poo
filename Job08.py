import math


class Cercle:
    
    def __init__(self, rayon):
        self.rayon = rayon 
        
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    def afficherInfos(self):
        print("les infos du cercle son Circonférence :", self.circonférence(), "Diamètre :", self.diametre(), "Aire :", self.aire())
        
    def circonférence(self):
        return 2 * self.rayon * math.pi
    
    def aire(self):
        return math.pi * self.rayon**2
    
    def diametre(self):
        return self.rayon * 2
        
    
        
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
cercle2.afficherInfos()
