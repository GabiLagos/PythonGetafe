import oracledb
connection= oracledb.connect(user='system', password='oracle', dsn='localhost/xe')
print("Conectados a DDBB")
print("========================================================")
consulta=connection.cursor()

print("Introduzca la inscripcion")
insc=input()
sql="select * from enfermo where inscripcion ="+insc
consulta.execute(sql)
fila=consulta.fetchone()

if (not fila):
    print("No existe esta persona")
    
else:
    apellido=fila[1]
    direccion=fila[2]
    print("El paciente",insc, "es", apellido, "domiciliad@ en:",direccion)
    
consulta.close()
connection.close()
print ("Fin de conexion a BBDD")