print("Practica Tabla de Multiplicar")
print("Introduzca un numero")
num = int(input())
c=1
print("con WHILE")
while (c!=11):
    print(num, "*", c, "=", c*num)
    c=c+1
  
  
print ("con FOR")  

for c in range(1,11):
    print (num, "x", c, "=", c*num)
print("Fin del Programa")