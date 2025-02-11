print("Conjerura de Collatz")
print("Introduzcs un cualquier numero entero positivo")
num = int(input())

while (num != 1):
    if (num%2==0):
        num = num/2
    else:
        num = num*3 + 1
    print (int(num))
    
print("Fin de Programa")