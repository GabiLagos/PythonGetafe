print("Practica Validacion ISBN")
print("Introduzca el ISBN")
isbn= input() 
if (isbn.isdigit() and len(isbn)==10):
    longitud=len(isbn)
    contador=0
    suma=0

    # while (contador != longitud):
    #     num=int(isbn[contador])
    #     suma= suma+num*contador
    #     contador=contador+1
    # print("la suma de los digitos de su ISBN es:", suma)  
    
    for i in range(longitud):
        letra=isbn[i]
        num=int(letra)
        op=num*(i+1)
        suma=suma+op
    if (suma%11==0):
        print("el ISBN es valido y la suma es ", suma)
    else:
        print("el ISBN no es valido")
         
else:
    print("No es un número")