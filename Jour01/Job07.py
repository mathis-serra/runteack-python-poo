class Personnage:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1 
    
    def bas(self):
        self.y -= 1 
    
    def haut(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)


    
    
#test pour le mettre dans dans une matrice 
    
# personnage = Personnage(0, 0)
# matrice = [
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
# ]

# matrice[personnage.x][personnage.y] = 'X'


# personnage.gauche()
# print(personnage.position())

# matrice[personnage.x][personnage.y] = 'X'

# for lignes in matrice:
#     print(lignes)

