print("Conexion a Oracle")
import oracledb
connection = oracledb.connect (user='system', password='oracle', dsn='localhost/xe')
print ("Conectados!!!!")
#Una vez conectados podemos lanzar una consulta. Estas se ejecutan mediante un objeto llamado cursor
# cursor=connection.cursor(), este sirve para consulta de seleccion o de accion y tendra metodos para ejecutar las consultas
sql="select * from dept" #creo una variable para las consultas que quiero hacer, notese que no lleva ;

consulta=connection.cursor() #el resultado de la consulta estará en la variable consulta

consulta.execute(sql) #aplicamos el metodo execute

fila = consulta.fetchone() # recupero la 1ra fila y avanzo a la siguiente, fetchone recpera solo una fila
print (fila)               # imprimo la 1ra file
fila = consulta.fetchone() # recupera la 2da fila y avanzo a la siguiente
print (fila)               # imprimo la 2da fila
fila = consulta.fetchone() # recupera la 3ra fila y avanzo a la siguiente
print (fila)               # imprimo la 3ra filafila = consulta.fetchone()
fila = consulta.fetchone() 
print (fila)  
fila = consulta.fetchone() #cuando llega al final de la tabla, cuandp ya no hay informacion, nos da none como resultado
print (fila) 
print ("=================================================================")
consulta.close() #cierro la consulta
connection.close() #cierro la coneccion
print ("Consulta y Coneccion cerradas")
