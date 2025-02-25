import oracledb
connection=oracledb.connect(user='system', password='oracle', dsn='localhost/xe')

print ("-----------EMPLEADOS TURNO-----------")
selecturno="select distinct turno from plantilla"
cursor=connection.cursor()
cursor.execute(selecturno)
cont=1
listaturnos=[]
for row in cursor:
    print(f"{cont} = {row[0]}")
    listaturnos.append(row[0])
    cont=cont+1
cursor.close

print ("Seleccione opcion de la lista")
opcion= int(input())
turno= listaturnos[opcion-1]
print("==========================================================")

sqlplantilla="select * from plantilla where turno =:p1"
cursor=connection.cursor()
cursor.execute(sqlplantilla, (turno,))
for row in cursor:
    print (row)
    
cursor.close()
connection.close()
print("==========================================================")
print ("Fin de conexion BBDD")