class Tache:
    
    
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut
        
    def get_titre(self):
        return self.titre
    
    def get_description(self):
        return self.description
    
    def get_statut(self):
        return self.statut
    
    def set_titre(self, titre):
        self.titre = titre
        
    def set_description(self, description):
        self.description = description
        
    def set_statut(self, statut):
        self.statut = statut
        

class ListeDeTaches:
    
    def __init__(self):
        self.taches = []
        
    def ajouterTache(self, tache):
        self.taches.append([tache.get_titre(), tache.get_description(), tache.get_statut()])
        
    def supprimerTache(self, tache):
        self.taches.remove([tache.get_titre(), tache.get_description(), tache.get_statut()])
        
    def marquerCommeFinie(self, tache):
        if tache.get_statut() == "Fini":
            print(f"La tâche '{tache.get_titre()}' est maintenant finie.")
    
    def afficherListe(self, ):
        return self.taches
    
    
    #filter et parceque il y a une faute dans le sujet de l'exercice          
    
    
    def filterListe(self, statut):
        for tache in self.taches:
            if tache[2] == statut:
                print(tache[0])
            
    


tache1 = Tache("Tache 1", "manger", "Fini")
tache2 = Tache("Tache 2", "boire", "En cours")
tache3 = Tache("Tache 3", "lire", "Fini")


liste = ListeDeTaches()

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

liste.supprimerTache(tache3)

liste.marquerCommeFinie(tache1)

tache2.set_statut("Fini")

print(liste.afficherListe())
