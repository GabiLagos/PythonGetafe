import oracledb
connection=oracledb.connect(user='system', password='oracle', dsn='localhost/xe')
print("Conectados a BBDD")
print("========================================================")
print("Introduzca el turno que desea buscar: T, M o N")
turno=input()
sql="select * from plantilla where turno= '" + turno + "'"
consulta=connection.cursor()
consulta.execute(sql)
row= consulta.fetchone()

if(not row):
    print("No existe ese turno, elija entre M, T o N")
else:
    print("Los empleados de turno "+turno+" son:") 
    print("========================================================") 
    for fila in consulta:
        apellido=fila[3]
        funcion=fila[4]
        print(apellido, funcion)
print("========================================================")        
consulta.close()
connection.close()
print("Fin de conexion a BBDD")