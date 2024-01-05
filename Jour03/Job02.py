class CompteBancaire:
    
    def __init__(self, nb_compte, nom, prenom, solde, decouvert):
        self.__nb_compte = nb_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        
    def get_nb_compte(self):
        return self.__nb_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def get_decouvert(self):
        return self.__decouvert
    
    def set_nb_compte(self, nb_compte):
        self.__nb_compte = nb_compte
        
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_solde(self, solde):
        self.__solde = solde
    
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Le compte numéro {self.get_nb_compte()} appartient à {self.get_prenom()} {self.get_nom()} et possède {self.get_solde()} euros.")
        
    def afficherSolde(self):
        print(f"Le compte numéro {self.get_nb_compte()} possède {self.get_solde()} euros.")

    def versement(self, montant):
        self.set_solde(self.get_solde() + montant)
        print(f"Le compte numéro {self.get_nb_compte()} possède maintenant {self.get_solde()} euros.")
    
    def retrait(self, montant):
        if self.get_decouvert() or montant <= self.get_solde():
            self.set_solde(self.get_solde() - montant)
            print(f"Le compte numéro {self.get_nb_compte()} possède maintenant {self.get_solde()} euros.")
        else:
            print("Vous ne pouvez pas retirer plus que ce que vous avez sur votre compte.")
    
    def agios(self, taux):
        if self.get_solde() < 0:
            agios = self.get_solde() * taux
            self.set_solde(self.get_solde() - agios)
            print(f"Des agios de {agios} euros ont été appliqués au compte numéro {self.get_nb_compte()}.")
    
    def virement(self, compte_destinataire, montant):
        if montant <= self.get_solde():
            self.set_solde(self.get_solde() - montant)
            compte_destinataire.set_solde(compte_destinataire.get_solde() + montant)
            print(f"Virement de {montant} euros effectué du compte numéro {self.get_nb_compte()} vers le compte numéro {compte_destinataire.get_nb_compte()}.")
        else:
            print("Vous n'avez pas suffisamment de fonds pour effectuer ce virement.")
        
        
bibi = CompteBancaire(123456789, "Bibi", "Nice", 1000, True)
decouvert = CompteBancaire(987654321, "Decouvert", "Nice", -100, False)
print(bibi.afficher())
bibi.versement(500)

bibi.virement(decouvert, 100)
decouvert.afficherSolde()
