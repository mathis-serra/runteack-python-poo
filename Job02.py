class Operation:
    
    
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3
    
    def set_nombre1(self, nombre1):
        self.nombre1 = nombre1
       
    def get_nombre1(self):
        return self.nombre1
    
    def set_nombre2(self, nombre2):
        self.nombre2 = nombre2
    
    def get_nombre2(self):
        return self.nombre2
    


nombre = Operation()
print(f"la valeur de nombre1 est {nombre.get_nombre1()}")
print(f"la valeur de nombre2 est {nombre.get_nombre2()}")
      
