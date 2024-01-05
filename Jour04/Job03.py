class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur 
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.get_longueur() + self.get_largeur())
    
    def surface(self):
        return self.get_longueur() * self.get_largeur()

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.get_hauteur()

rectangle = Rectangle(5, 3)
print("Perimetre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

parallelepiped = Parallelepipede(5, 3, 2)
print("Volume du parallelepipede:", parallelepiped.volume())

   