class Vehicule:
    
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque
    
    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele
    
    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee
    
    def get_prix(self):
        return self.prix

    def set_prix(self, prix):
        self.prix = prix
    
    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_modele())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix(), "€")
        
    def demarrer(self):
        print("Attention, je roule ")
    
class Voiture(Vehicule):
    
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def get_portes(self):
        return self.portes
    
    def set_portes(self, portes):
        self.portes = portes
        
        
    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_modele())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix(), "€")
        print("Nombre de portes:", self.get_portes())
        
    def demarrer(self):
        print("Attention, j'accèlère ")


class Moto(Vehicule):
    
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roues = 2

    def get_roues(self):
        return self.roues
    
    def set_roues(self, roues):
        self.roues = roues
    
    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_modele())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix(), "€")
        print("Nombre de roues:", self.get_roues())
        
    def demarrer(self):
        print("Attention, je cabre")
        
        
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)       
    
voiture.informationsVehicule()
moto.informationsVehicule()
voiture.demarrer()
moto.demarrer()


