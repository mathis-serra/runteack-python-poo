class Livre:
    
    def __init__(self, title, autor, pages):
        self.__tilte = title
        self.__autor = autor
        self.__pages = pages
        if self.__pages <= 0:
            self.__pages = "Impossible value"
        self.__disponible = True
    
    def get_title(self):
        return self.__tilte
    
    def get_autor(self):
        return self.__autor
    
    def get_pages(self):
        return self.__pages
    
    def get_disponible(self):
        return self.__disponible
    
    def set_title(self, title):
        self.__title = title
    
    def set_autor(self, autor):
        self.__title = autor
    
    def set_pages(self, pages):
        self.__title = pages
        
    def set_disponible(self, disponible):
        self.__disponible = disponible
    
    
    def verification(self):
        if self.get_disponible():
            return True 
        else:
            return False
        
    def emprunter(self):
        if self.verification():
            self.set_disponible(False)
    
    def rendre(self):
        if self.verification() == False:
            self.set_disponible(True)
        
my_book = Livre("gregory", "benoit", 30)

print(my_book.get_title())
print(my_book.get_autor())
print(my_book.get_pages())
my_book.emprunter()

my_book.rendre()
print(my_book.verification())
    
        
        
        
    