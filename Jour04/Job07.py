import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self, nb_cartes):
        if nb_cartes > len(self.paquet):
            raise ValueError("Not enough cards in the deck.")
        
        cartes_distribuees = []
        for _ in range(nb_cartes):
            cartes_distribuees.append(self.paquet.pop())
        
        return cartes_distribuees


jeu = Jeu()
jeu.melanger_paquet()
main_joueur = jeu.distribuer_cartes(2)
main_croupier = jeu.distribuer_cartes(2)


