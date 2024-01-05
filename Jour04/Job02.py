class Personne: 
    
    
    def __init__(self):
        self.age = 14
        

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    
    def afficherAge(self):
        print(f"l'age de la personne est {self.get_age()}")
    
    def bonjour(self):
        print ("Hello")
    
    def modifierAge(self, age):
        self.age = age 
    

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    
    def afficherAge(self):
        print(f"J'ai {self.get_age()}")
    
    
class Professeur(Personne):
    
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
        
    def enseigner(self):
        print ("Le cour va commencer")


anthony = Personne()     
pierre = Eleve()  

pierre.bonjour()
pierre.allerEnCours()
pierre.modifierAge(15)

prof = Professeur("Mathématiques")
prof.set_age(40)
prof.bonjour()
prof.enseigner()
