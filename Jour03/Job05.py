class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 10
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige 10 points de dégâts.")


class Jeu:
    def choisirNiveau(self):
        niveau = input("Choisissez le niveau de difficulté (facile, moyen, difficile): ")
        return niveau

    def lancerJeu(self):
        niveau = self.choisirNiveau()
        if niveau == "facile":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)
        elif niveau == "moyen":
            joueur = Personnage("Joueur", 75)
            ennemi = Personnage("Ennemi", 75)
        elif niveau == "difficile":
            joueur = Personnage("Joueur", 50)
            ennemi = Personnage("Ennemi", 100)
        else:
            print("Niveau invalide. Veuillez choisir un niveau valide.")
            return

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

        if joueur.vie <= 0:
            print("Vous avez perdu.")
        else:
            print("Vous avez gagné.")

perso = Personnage("Joueur", 100)
jeu = Jeu()
jeu.lancerJeu()
