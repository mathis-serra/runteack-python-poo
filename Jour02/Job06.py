class Commande:
    
    def __init__(self, nb_commande, liste, statut):
        self.__nb_commande = nb_commande
        self.__liste = liste
        self.__statut = statut 
    
    def get_nb_commande(self):
        return self.__nb_commande
    
    def get_liste(self):
        return self.__liste
    
    def get_statut(self):
        return self.__statut 
    
    def set_nb_commande(self, nb_commande):
        self.__nb_commande = nb_commande 
        
    def set_liste(self, liste):
        self.__liste = liste 
        
    def set_statut(self, statut):
        self.__statut = statut 
        
    def ajouter_plat(self, nom_plat, prix_plat, statut_plat):
        self.__liste[nom_plat] = {'prix': prix_plat, 'statut': statut_plat}
        
    def annuler_commande(self):
        self.__liste = {}
        
    def __calculer_total(self):
        total = 0
        for plat, details in self.get_liste().items():
            total += details['prix']
        return total
            
            
    
    def afficher_commande(self):
        noms_plats = list(self.get_liste().keys())
        total = self.__calculer_total()
        print(f"Numéro de commande : {self.get_nb_commande()}, Plats: {', '.join(noms_plats)}, Prix: {total}, Statut: {self.get_statut()}")
    
    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * taux_tva / 100
        return tva

couscous = Commande(1, {}, "en cours")

couscous.ajouter_plat("couscous", 10, "en cours")
couscous.afficher_commande()
