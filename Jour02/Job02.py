class Livre:
    
    def __init__(self, title, autor, pages):
        self.__tilte = title
        self.__autor = autor
        self.__pages = pages
        if self.__pages <= 0:
            self.__pages = "Impossible value"
    
    def getTitle(self):
        return self.__tilte
    
    def getAutor(self):
        return self.__autor
    
    def getPages(self):
        return self.__pages
    
    def setTitle(self, title):
        self.__title = title
    
    def setAutor(self, autor):
        self.__title = autor
    
    def setPages(self, pages):
        self.__title = pages
        
my_book = Livre("gregory", "benoit", 30)

print(my_book.getTitle())
print(my_book.getAutor())
print(my_book.getPages())






   

    
    
