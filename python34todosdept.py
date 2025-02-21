print("Recorrer toda la tabla a la vez")
import oracledb
connection = oracledb.connect (user='system', password='oracle', dsn='localhost/xe')
print ("Conectados!!!!")
sql="select * from dept" 
consulta=connection.cursor() 
consulta.execute(sql)

#usamos un bucle FOR para recorrer todas la filas de la tabla dept a la vez
print("=============================================")
print("Recorro toda la tabla con todas sus columnas")
for fila in consulta:
    print (fila)
#para ver los datos de una de las columnas, la primera es 0. Hay que ejecutar la conulta otra vez
print("=============================================")
print ("Ver solo una las columnas")
consulta.execute(sql)
for fila in consulta:
    print (fila[0])
    
print("=============================================")
print ("Otra sintaxis, definimos una variable por cada columna")
consulta.execute(sql)
for numero, nombre, localidad  in consulta: # se define una variable por cada columna
    print (numero, ":", nombre, ", ", localidad) # asi puedo decirle como quiero imprimirlo

consulta.close() 
connection.close() 

print("Fin de Acceso a la BBDD")