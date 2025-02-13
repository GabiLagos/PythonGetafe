import libreria25validaciones

print("Introduzca el ISBN a validar")
isbn = input()
validacion= libreria25validaciones.validarIsbn(isbn)

if (validacion==1):
    print("EL ISBN es valido")
elif (validacion==0):
    print("El ISBN no es valido")
    
print("========================================================")    
    
print("Introduzca su DNI")
dni = int(input())
validacion= libreria25validaciones.validarDni(dni)
print("Su letra es ", validacion)