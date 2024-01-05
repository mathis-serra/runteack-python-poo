class Ville:
    
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants
        
    def get_nom(self):
        return self.__nom
    
    def get_nb_habitants(self):
        return  self.__nb_habitants
        
    def set_nom(self, nom):
        self.__nom = nom
        
    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants


class Personne:
    
    
    def __init__(self, nom , age , objet_ville):
        self.__nom = nom 
        self.__age = age
        self.__objet_ville= objet_ville
        
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_objet_ville(self):
        return self.__objet_ville
    
    def set_nom(self, nom):
        self.__nom = nom
        
    def set_age(self, age):
        self.__age = age
    
    def set_objet_ville(self, objet_ville):
        self.__objet_ville = objet_ville
    
    def ajouterPopulation(self, objet_ville):
        objet_ville.set_nb_habitants(objet_ville.get_nb_habitants() + 1)
        print("La ville de " + objet_ville.get_nom() + " a maintenant " + str(objet_ville.get_nb_habitants()) + " habitants.")
    
paris = Ville("Paris", 1000000)

print(paris.get_nb_habitants())

marseille = Ville("Marseille", 861635) 

print(marseille.get_nb_habitants())

jonh = Personne("Jonh", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloé = Personne("Chloé", 18, marseille)
jonh.ajouterPopulation(paris)
myrtille.ajouterPopulation(paris)
chloé.ajouterPopulation(marseille)



        
        
        