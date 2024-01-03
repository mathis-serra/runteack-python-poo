class Rectangle: 
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def getLongueur(self):
        return self.__longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
    def getLargeur(self):
        return self.__largeur


rectangle = Rectangle(10, 5)


print(rectangle.getLongueur())
print(rectangle.getLargeur())


rectangle.setLongueur(15)
rectangle.setLargeur(10)

print(rectangle.getLongueur())
print(rectangle.getLargeur())



        
    