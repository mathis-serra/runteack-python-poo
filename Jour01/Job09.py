class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA sur le produit: {self.TVA}, Prix TTC :{self.CalculerPrixTTC()}"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Produit 1", 100, 20)
produit2 = Produit("Produit 2", 30.0, 10)

# Affichage des informations initiales
print("Informations initiales des produits :", produit1.afficher(), "\n", produit2.afficher())



# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouveau Produit 1")
produit1.modifierPrixHT(60.0)

produit2.modifierNom("Nouveau Produit 2")
produit2.modifierPrixHT(35.0)

# Affichage des nouvelles informations des produits
print("\nInformations des produits après modification :", produit1.afficher(), "\n", produit2.afficher())


