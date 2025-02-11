print("Ejemplo de Bucles")
#aqui comenzamos el bucle while
print("WHILE")
#siempre necesitamos una variable pra la condicion del bucle, en este caso contador
contador= 0
while (contador <=9):
     print("Contando... ", contador)
     contador = contador + 1
     
     
#aqui comezamos en bucle for
print ("FOR")
for i in range(5):
     print("Valor de i (contador) es ", i)

#note que ambos bucles comienzan en 0 y van incrementandose, pero puedo indicar que comiencen en otro numero
print ("FOR comenzando en otro numero distinto de 0")
for i in range(3,13):
     print ("El valor de i es: ", i)

print ("Fin del Programa")
