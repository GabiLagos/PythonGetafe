print ("Practica Día de Nacimiento")
print("Ingresa tu dia de nacimiento")
dia = int(input())
print("Ingresa tu mes de nacimiento en munero, si es enero escribe 1, si es febrero escribe 2, etc")
mes = int(input())
print("Ingresa tu año de nacimiento, por ejemplo 1990")
year = int(input())

if (mes == 1):
    mes = 13 
    year=year-1
elif (mes == 2):
    mes = 14 
    year = year-1
    
op1 = int ((mes + 1)*(3/5))
op2 = int (year/4)
op3 = int (year/100)
op4 = int (year/400)
op5 = dia + (mes*2) + year + op1 + op2 - op3 + op4 + 2
op6 = int (op5/7)
op7 = op5 - op6*7

if (op7== 0):
    print("Naciste en Sabado")
elif (op7 == 1):   
    print("Naciste en Domingo")
elif (op7 == 2):
    print("Naciste en Lunes")
elif (op7 == 3):
    print("Naciste en Martes")  
elif (op7 == 4):
    print("Naciste en Miercoles")
elif (op7 == 5):
    print("Naciste en Jueves")
elif (op7 == 6):
    print("Naciste en Viernes")

print("Fin de la practica")


   #tambien funcionaria si usara trunc en vez de int 
    