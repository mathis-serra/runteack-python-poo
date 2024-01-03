class Animal:
    
    def __init__(self,):
        self.age = 0
        self.prenom = ""
        
    def vieillir(self):
        self.age +=1
    
    
    def nommer(self, prenom):
        self.prenom = prenom
        
        
animal = Animal()
print("L'êge de l'animal est", animal.age)
animal.vieillir()
print("L'êge de l'animal est", animal.age)
animal.nommer("Luna")
print("Le prénom de l'animal est", animal.prenom)


