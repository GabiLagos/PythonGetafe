#METODOS RETURN, EJECUTAN Y DEVULVEN INFORMACION
def convertirMayusculas(texto):
    return texto.upper()


def convertirMinusculas(texto):
    return texto.lower()


def concatenar(texto1,texto2):
    concatenacion=texto1+texto2
    return concatenacion

def mostrarMenu():
    print("Seleccione una opcion del menu")
    print("1. Convertir Mayúsculas")
    print("2. Convertir Minúsculas")
    print("3. Concatenar")

#---------------------------------------------------
#PROGRAMA PPAL
print("Metodos Return")
print("Introduzca un texto")
valor = input()
mostrarMenu()
opcion = int(input())
if (opcion==1):
    resultado=convertirMayusculas(valor)
    
elif (opcion==2):
    resultado=convertirMinusculas(valor)
else:
    print("ingrese otra palabra")
    valor2=input()
    resultado=concatenar(valor,valor2)

print(resultado)
    
print("Fin del programa")