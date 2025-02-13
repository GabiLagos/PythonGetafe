print("TUPLAS EN PYTHON")
#Las tuplas no se pueden variar (append, insert, pop, del...)!!!
productos = ("Leche", "Cacao", "Avellanas","Azucar")
contarElementos = len(productos)
print ("Elementos de la tupla", contarElementos)

#BUCLE DE REFERNCIA, prod es la variable de referencia
for prod in productos:
    print (prod)