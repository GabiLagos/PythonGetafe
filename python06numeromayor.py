print("Ejemplo de numero mayor")
print("Ingresa el primer numero")
numero1 = int(input())

print("Ingresa el segundo numero")
numero2 = int(input())


if (numero1 > numero2):
    print("El numero " + str(numero1) + " es mayor que" + str(numero2))

elif (numero1==numero2):
    print("Los numeros son iguales")
else:
    print("El numero " + str(numero2) + " es mayor que" + str(numero1) )

print("FIN")

