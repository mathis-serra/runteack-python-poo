class point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
    def afficherLesPoints(self): 
        print("les coordonnées des points sont x =", self.x, ", y =", self.y)
        
    def AfficherX(self):
        return self.x
    
    def AfficherY(self):
        return self.y
    
    def changerX(self, new_x):
        self.x = new_x
    
    def changerY(self, new_y):
        self.y = new_y
    

point1 = point(2, 3)
point2 = point(5, 6)

point1.afficherLesPoints()
point2.afficherLesPoints()
print(point1.AfficherX())
print(point1.AfficherY())
print(point2.AfficherX())
print(point2.AfficherY())
point1.changerX(10)
point1.changerY(20)
point2.changerX(30)
point2.changerY(40)
point1.afficherLesPoints()

