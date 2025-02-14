from class30choche import Coche
from class31deportivo import Deportivo

coche1 = Coche()
coche1.modelo = "A30"
coche1.arrancar()
coche1.acelerar()
coche1.acelerar()
velcohe1=coche1.getVelocidadMaxima()
print("Velocidad de coche", velcohe1)

print ("==============")
depor1 = Deportivo()
depor1.arrancar()
depor1.turbo()
depor1.acelerar()
veldepor1= depor1.getVelocidadMaxima()
print("Velocidad de deportivo", veldepor1)
