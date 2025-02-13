print("LISTAS CON PYTHON")
#lista de nombres, se crean con corchetes y comienzan en la posicion 0 en terminan en len
listadenumeros = [12,34,567,12,91, 56, 92, 33]
longitud = len(listadenumeros)

print("Numero 0 de mi lista es:", listadenumeros[0])
    
listadenombres = ["José", "Andrea", "Diana", "Juan", "Daniel", "María"]
print ("El nombre el la posicion 2 es:", listadenombres[2])

#METODOS DE LAS LISTAS:
#recorrer todo los nombres de las listas
for i in range(len(listadenombres)):
    print("En la posicion", i, "esta el nombre:", listadenombres[i])

# append: un nuevo elemento al final de la lista
listadenombres.append("Gabi")
print ("nombre 2", listadenombres[2])

#insert(), crea un nuevo elemento en una posocion determinada de la lista
listadenombres.insert(3, "Infiltrado")
print("Nombre 3 es:", listadenombres[3])

#remove(), elimina un elemento de la lista en una posicion dada
listadenombres.remove("Juan")
for i in range(len(listadenombres)):
    print("En la posicion", i, "esta el nombre:", listadenombres[i])
    

#pop(), elimina un elemento por su posicion
listadenombres.pop(1)
for i in range(len(listadenombres)):
    print("En la posicion", i, "esta el nombre:", listadenombres[i])
    
#del NO es un metodo es una funcion!! hace lo mismo que pop (que es un metodo), 
# pero con del podemos hacwer slicing
del listadenombres[0:3]
for i in range(len(listadenombres)):
    print("En la posicion", i, "esta el nombre:", listadenombres[i])

# #clear, borra todo el contenido de una lista, la deja vacia
# listadenombres.clear()
# for i in range(len(listadenombres)):
#     print("En la posicion", i, "esta el nombre:", listadenombres[i])

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print("Andrea" in nombre) #Preguntamos si el elemento Andrea existe en la lista
print("Pepito" in nombre) #Preguntamos si el elemento Pepito existe en la lista

print("--------------LISTAS-------------")
print("ORDENANDO LISTAS ASCENDENTE DE NUMEROS")
notas= [1,10,6,7,4,9]
for i in range(len(notas)):
    print("En la posicion", i, "ela nota es:", notas[i])
notas.sort()
print("Nota más baja:",notas[0])
print("Segunda nota más baja:",notas[1])
for i in range(len(notas)):
    print("En la posicion", i, "ela nota es:", notas[i])
print("ORDENANDO LISTAS DESCENDENTE")
notas.sort(reverse=True)
for i in range(len(notas)):
    print("En la posicion", i, "ela nota es:", notas[i])
    
print("ORDENANDO LISTAS ASCENDENTE DE PALABRAS")
notas= [1,10,6,7,4,9]
for i in range(len(listadenombres)):
    print("En la posicion", i, "ela nota es:", listadenombres[i])
listadenombres.sort()
print("Nota más baja:",listadenombres[0])
print("Segunda nota más baja:",listadenombres[1])
for i in range(len(listadenombres)):
    print("En la posicion", i, "ela nota es:", listadenombres[i])
print("ORDENANDO LISTAS DESCENDENTE")
listadenombres.sort(reverse=True)
for i in range(len(listadenombres)):
    print("En la posicion", i, "ela nota es:", listadenombres[i])
    

