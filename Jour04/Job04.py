class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, largeur):
        self.largeur = largeur
    
    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur
        
    
    def aire(self):
        return self.largeur * self.hauteur

rectangle = Rectangle(5, 3)
print(rectangle.aire())
