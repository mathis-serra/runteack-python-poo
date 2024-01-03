class Student:
    
    
    def __init__(self, nom, prenom, nb_etudiant):
        self.__nom = nom
        self.__prenom = prenom 
        self.__nb_etudiant = nb_etudiant
        self.__nb_credit = 0 
        self.__level = self.__studentEval
        
    
    def __studentEval(self):
        if self.__nb_credit >= 90:
            return "Excellent"
        elif self.__nb_credit >= 80:
            return "Très Bien"
        elif self.__nb_credit >= 70:
            return "Bien"
        elif self.__nb_credit >= 60:
            return "Passable"
        else : 
            return "Insuffisant"
    
    def get_nom(self):
        return self.__nom       
    def get_prenom(self):
        return self.__prenom       
    def get_nb_etudiant(self):
        return self.__nb_etudiant       
    def get_nb_credit(self):
        return self.__nb_credit 
    def get_level(self):
        self.__studentEval()
        return self.__level
    def set_nom(self, nom):
        self.__nom = nom 
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def set_nb_etudiant(self, nb_etudiant):
        self.__nb_etudiant = nb_etudiant 
    def set_nb_credit(self, nb_credit):
        self.__nb_credit = nb_credit
        self.__level =self.__studentEval()
        
    def add_credits(self, nb_credit):
        if nb_credit <= 0: 
            self.__nb_credit = "impossible"
        else:
            self.__nb_credit += nb_credit
            self.__level = self.__studentEval()
            
    def studentInfo(self):
        print(f"l'etudiant {etudiant.get_prenom()} {etudiant.get_nom()}, numero {etudiant.get_nb_etudiant()} a {etudiant.get_nb_credit()} credits, il a un niveau :{etudiant.get_level()}")

etudiant = Student("Doe", "Jonh", 145)

etudiant.add_credits(30)
etudiant.add_credits(30)
etudiant.add_credits(30)


etudiant.studentInfo()     