print("Practica de Operadores Relacionales")
print("Introduce el primer numero")
num1 = int(input())
print("Introduce el segundo numero")
num2 = int(input())
print("Introduce el tercer numero")
num3 = int(input())

mayor = 0
menor = 0
intermedio = 0


if (num1 >= num2 and num1 >= num3):
    mayor = num1
    if (num2 > num3):
        intermedio = num2
        menor = num3
    elif (num3 > num2):
        intermedio = num3
        menor = num2
        
    
if (num2 >= num1 and num2 >= num3):
    mayor = num2
    if (num1 >= num3):
        intermedio = num1
        menor = num3
    elif (num3 >= num1):
        intermedio = num3
        menor = num1
        
    
if (num3 > num1 and num3 > num2):
    mayor = num3
    if (num1 >= num2):
        intermedio = num1
        menor = num2
    elif (num2 >= num1):
        intermedio = num2
        menor = num1

    
    
print("El numero mayor es ", mayor)
print("El numero intermedio es ", intermedio)
print("El numero menor es ", menor)
print("La media entre el numero mayor y el menor es ", (mayor + menor)/2)
print("Fin de la practica")