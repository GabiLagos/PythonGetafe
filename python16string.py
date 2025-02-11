print("Como usamos los METHODS (funciones) de la clase STRING)")
texto = "PrimeroPython"
 #Vamos prbando métodos y vemos que devuelven

print ("La variable original es Primero Python ") 
print("upper   ", texto.upper())
print("replace  ", texto.replace("o", "@"))
print("letra 0:  ", texto[0] )
print("Longitud (len)", len(texto))
print("find y: ", texto.find("y"))
print("find Z: ", texto.find("Z"))
print("find P con sobrecarga", texto.find("P",1))
print("rfind P", texto.rfind("P"))
print("startswith A", texto.startswith ("A"))
print("endswith n", texto.endswith ("n"))
print("isdigit", texto.isdigit())
print("isdigit", texto.isdigit())
print("isalpha", texto.isalpha())
print("isalnum", texto.isalnum())  

# A esto se le llama "slicing"
print("recuperar la posicion 3 en adelante:", texto[2:]) 
print("recuperar desde la posicion 3 hasta la 5:", texto[2:5])

#Podemos recorrer cada caracter en un texto
print("recorrer cada letra del un texto:")
for i in range(len(texto)):
    letra =texto[i]
    print("posicion ", i, ":", letra)
    
print("vamos a comprobar si lo se introduce es un número")   
print("Introduzca un número") 
aux= input() #definimos una variable auxiliar para luego evaluarla
if (aux.isdigit()):
    print ("Esto si es un numero") #no funcionará con números negativos
else:
    print("Esto no es un número") 




