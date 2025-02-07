print("Ejemplo de positivos o negativos")
print("Ingresa un numero")
numero = int(input())
if (numero > 0):
    print("El numero ", str(numero), " es positivo")
#else:
#    if(numero == 0):
#        print("El 0 no es ni positivo ni negativo" )
#    else:print("El numero ", str(numero), " es negativo")

#Otra manera es con la funcion elif, esto nos permite preguntar por multiples condicionales

elif (numero<0):
    print("El numero ", str(numero), " es negativo)")
else:
    print("El 0 no es ni positivo ni negativo" )

print("FIN")
