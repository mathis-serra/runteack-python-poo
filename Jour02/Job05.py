class Voiture: 
    
    
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque 
        self.__modele = modele
        self.__annee = annee 
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoire = 5
    
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_reservoire(self):
        return self.__reservoire
    
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
        
    def set_reservoire(self, reservoire):
        self.__reservoire = reservoire 
    
    def __verifier_plein(self):
        return self.get_reservoire()
    
    def demarrer(self):
        if self.__verifier_plein() >= 5:
            self.set_en_marche(True)
            return "La voiture a démarré avec succès."
        else:
            return "Le réservoir est trop bas, la voiture ne peut pas démarrer."

    
    def arreter(self):
        if self.get_en_marche() == False:
            self.set_en_marche(False)
            
    
            
voiture = Voiture("Renault", "Clio", 2019, 10000)

print(f"la voiture est une {voiture.get_marque()} {voiture.get_modele()} de {voiture.get_annee()} avec {voiture.get_kilometrage()} km au compteur")
            
print(voiture.demarrer())