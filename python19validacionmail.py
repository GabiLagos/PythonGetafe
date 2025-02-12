print("Practica Validacion de Mail")
print("Introduzca su e-mail")
mail=input()

#aqui comienza la validación

num=int(mail.find("@"))
#que contenga @
if (mail.find("@")==-1 or mail.count("@")==0):        
    print("Esta direccion de e-mail no contiene @")
#que contenga un punto "."
elif (mail.find(".")==-1):
    print("Esta direccion de e-mail no contiene .")
#que no tenga @ ni al inicio ni al final
elif(mail.startswith("@")==True or mail.endswith("@")==True):
    print("El arroba no puede estar ni al inicion ni al final")
#que no tenga . ni al inicio ni al final
elif(mail.startswith(".")==True or mail.endswith(".")==True):
    print("El punto no puede estar ni al inicion ni al final")
elif(mail[0]== "." or mail.endswith(".")==True):
    print("El punto no puede estar ni al inicion ni al final")
#que solo haya @ una vez
elif (mail.find("@")!=mail.rfind("@") or mail.count("@")>1 ):
    print("Solo puede haber una @")
#que no haya un "." despues de @
elif (mail.find("@")>mail.rfind(".") ):
    print("Debe haber un . depues de @")
#que el dominio tenga 2 o 3 caracteres
else:
    ultimopunto=mail.rfind(".") #nos ubicamos en el punto antes del dominio
    dominio=mail[ultimopunto+1:] #recuperamos en dominio
    longdominio=len(dominio) #longitud del dominio
    if(longdominio>=2 and longdominio<=3):
        print("Su e-mail es correcto")
    else:
        print("El dominio de su e-mail de tener 2 o 3 caracteres")
    
    
print("Fin del Programa")



