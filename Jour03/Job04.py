class Joueur:
    
    def __init__(self, nom, numero, position, nb_but, passes_d, carton_jaunes, cartons_rouge):
        

        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = nb_but
        self.passes_d = passes_d
        self.carton_jaunes = carton_jaunes
        self.cartons_rouge = cartons_rouge
    
    def get_nom(self):
        return self.nom
    
    def get_numero(self):
        return self.numero
    
    def get_position(self):
        return self.position
    
    def get_nb_but(self):
        return self.nb_but
    
    def get_passes_d(self):
        return self.passes_d
    
    def get_carton_jaunes(self):
        return self.carton_jaunes
    
    def get_cartons_rouge(self):
        return self.cartons_rouge
    
    def set_nom(self, nom):
        self.nom = nom
        
    def set_numero(self, numero):
        self.numero = numero
    
    def set_position(self, position):
        self.position = position
    
    def set_nb_but(self, nb_but):
        self.nb_but = nb_but
    
    def set_passes_d(self, passes_d):
        self.passes_d = passes_d
    
    def set_carton_jaunes(self, carton_jaunes):
        self.carton_jaunes = carton_jaunes
    
    def set_cartons_rouge(self, cartons_rouge):
        self.cartons_rouge = cartons_rouge
    
    def marquerUnBut(self):
        self.nb_but += 1
        print(f"Le joueur {self.get_nom()} a marqué un but !") 
        
    def effectuerUnePasseDecisive(self):
        self.set_passes_d(self.get_passes_d() + 1)
        print(f"Le joueur {self.get_nom()} a effectué une passe Decisive !")
    
    def prendreUnCartonJaune(self): 
        self.set_carton_jaunes(self.get_carton_jaunes() + 1)
        print(f"Le joueur {self.get_nom()} a pris un carton jaune !")
    
    def prendreUnCartonRouge(self):
        self.set_cartons_rouge(self.get_cartons_rouge() + 1)
        print(f"Le joueur {self.get_nom()} a pris un carton rouge !")
        
    def afficherStatistiques(self):
        print(f"Le joueur {self.get_nom()} a marqué {self.get_nb_but()} buts, a effectué {self.get_passes_d()} passes décisives, a pris {self.get_carton_jaunes()} cartons jaunes et a pris {self.get_cartons_rouge()} cartons rouges.")
    
class Equipe:
    
    
    def __init__(self, nom, liste_joueurs):
        self.nom = nom
        self.liste_joueurs = liste_joueurs
        
        
    def get_nom(self):
        return self.nom
    
    def get_liste_joueurs(self):
        return self.liste_joueurs
    
    def set_nom(self, nom):
        self.nom = nom
    
    def set_liste_joueurs(self, liste_joueurs):
        self.liste_joueurs = liste_joueurs
    
    def ajouterJoueur(self, joueur):
        self.get_liste_joueurs().append(joueur)
        print(f"Le joueur {joueur.get_nom()} a été ajouté à l'équipe {self.get_nom()}.")
        
    def afficherStatistiquesJoueurs(self):
        for joueur in self.get_liste_joueurs():
            joueur.afficherStatistiques()
            
    def mettreAJourStatistiquesJoueurs(self, nom, nb_but, passes_d, carton_jaunes, cartons_rouge):
        for joueur in self.get_liste_joueurs():
            if joueur.get_nom() == nom:
                joueur.set_nb_but(nb_but)
                joueur.set_passes_d(passes_d)
                joueur.set_carton_jaunes(carton_jaunes)
                joueur.set_cartons_rouge(cartons_rouge)
                print(f"Les statistiques du joueur {joueur.get_nom()} ont été mises à jour.")

neymar = Joueur("Neymar", 10, "Attaquant", 567, 308, 45, 12)
messi = Joueur("Messi", 30, "Attaquant", 678, 345, 67, 23)
cristiano = Joueur("Cristiano", 7, "GOAT", 789, 456, 89, 34)
ramos = Joueur("Ramos", 4, "Défenseur", 12, 1, 190, 50)
terStengen = Joueur("Ter Stegen", 1, "Gardien", 0, 1, 5, 2)
navas = Joueur("Navas", 1, "Gardien", 0, 1, 5, 2)
barca = Equipe("Barca", [neymar, messi, terStengen])
real = Equipe("Real", [ramos, cristiano, navas])

real.ajouterJoueur(neymar)
real.afficherStatistiquesJoueurs()

barca.mettreAJourStatistiquesJoueurs("Neymar", 568, 309, 46, 13)
barca.afficherStatistiquesJoueurs()