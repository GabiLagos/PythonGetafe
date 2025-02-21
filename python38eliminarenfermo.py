import oracledb
connection=oracledb.connect(user="system", password="oracle", dsn="localhost/xe")
print ("Eliminar Enfermo")
print("Introduzca la inscripcion que desea borrar")
data=input()
sql="delete from enfermo where inscripcion = " + data

print (sql)
print ("================================================")
consulta=connection.cursor()
consulta.execute(sql)
afectados= consulta.rowcount
print ("Registro de los afectados ", afectados)
#Todavia no ha sido afectada la BBDD, hay que hacer commit o rollback

connection.commit()
# o
#connection.rollback()

consulta.close()
connection.close()
print("Fin de conexion a BBDD")