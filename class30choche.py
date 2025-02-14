class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False
    
    def __init__(self):
        self.marca = "Audi" 
    
    def __str__(self): #define que quiero que aparezca cuando hago print(persona) estando un programa.py
        return self.marca +" "+ self.modelo 
    
    def arrancar (self):
        self.estado = True
        print ("Coche arrancado")
    
    
    def acelerar(self):
        if (self.estado == False):
            print ("El coche no está arrancado. Debe arrancar antes")
        else:
            self.velocidad += 20
        print ("Velocidad actual ", self.velocidad)
    
    def frenar(self):
        if (self.estado == False):
            print ("El coche no está arrancado. Debe arrancar antes")
        else:
            if (self.velocidad == 0):
                print ("El está detenido")
            else:
                self.velocidad -= 10
        print ("Velocidad actual ", self.velocidad)
        
    def getVelocidadMaxima(self):
        print ("velocidad máxima Coche: 140 km/h")
        return 140
        