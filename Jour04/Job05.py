class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius 
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.get_radius() ** 2

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
# Création d'une instance de Cercle
cercle = Cercle(5)
print("Aire du cercle:", cercle.aire())

# Création d'une instance de Rectangle
rectangle = Rectangle(4, 6)
print("Aire du rectangle:", rectangle.aire())
    
