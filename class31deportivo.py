from class30choche import Coche
class Deportivo (Coche):
    def turbo(self):
        self.velocidad += 120
        print("Activado turbo!!!")
        print ("La velocidad es ", self.velocidad)
    def acelerar(self):
        if (self.estado == False):
            print ("El coche no está arrancado. Debe arrancar antes")
        else:
            self.velocidad += 60
        print ("Acelerando  ", self.marca + " a "+ str(self.velocidad))
    def getVelocidadMaxima(self):
        return super().getVelocidadMaxima()+ 100
    