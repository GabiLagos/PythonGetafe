print("Practica Validacion de Mail")
print("Introduzca su e-mail")
mail=input()
punto=mail.find(".")
arroba=mail.find("@")

#aqui comienza la validación
num=int(mail.find("@"))
if (mail.find("@")==-1):
    print("Esta direccion de e-mail no contiene @")
elif (mail.find(".")==-1):
    print("Esta direccion de e-mail no contiene .")
elif (mail.find("@")==0):
    print("El arroba no puede estar al comienzo de su e-mail")
elif (punto>arroba):
    print("No puede haber un . depues de @")
elif (mail.find("@")!=mail.rfind("@")):
    print("Solo puede haber una @")
elif ()

else:
    print("Continuemos...")



