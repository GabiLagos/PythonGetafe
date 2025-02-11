print("Practica de bucles, rango pares")
print ("Introduzca un numero de inicio")
inicio =int(input())
print("Introduzca un valor final")
final = int(input())

#realizamos un bucle desde inicio hasta final+1

for i in range(inicio, final+1):
    if(i%2==0):
        print(i)
    else:
        print("El número de valores no es par")
print("Fin de programa")