print("Ejemplo de librerias")
#Sintaxis con from

#Hay dos maneras de importar un libreria:
# from math import floor, ceil, trunc
import math


numero1= 20
numero2=3
division= numero1/numero2

#delcaramos variables para almecenar los valores

varFloor = math.floor(division)
varCeil = math.ceil(division)
varTrunc = math.trunc(division)

print("Redondeando hacia abajo, ", numero1,"/",numero2," = ", varFloor)
print("Redondeando hacia arriba, ", numero1,"/",numero2," = ", varCeil)
print("Truncado los decimales hacia abajo, ", numero1,"/",numero2," = ", varTrunc)



