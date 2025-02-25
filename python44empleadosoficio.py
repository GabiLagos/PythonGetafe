import oracledb
connection= oracledb.connect(user='system', password='oracle', dsn='localhost/xe')
#print("Introduzca el codigo del oficio que busca")
#oficio_cod =input()

print("-------------Buscador Oficio Empleados---------------")

selectoficio ="select distinct oficio from emp"
cursor = connection.cursor()
cursor.execute(selectoficio)
cont = 1
listaoficios=[]

for row in cursor:
    print(f"{cont} = {row[0]}")
    listaoficios.append(row[0])
    cont=cont+1
cursor.close()
print ("Seleccione una opcion de la lista")
opcion= int(input())
oficio= listaoficios[opcion-1]

sqlempleado = "select * from emp where oficio= :p1"
cursor = connection.cursor()
cursor.execute(sqlempleado, (oficio,) )
for row in cursor:
    print (row)
    
cursor.close()
connection.close()
print("Fin de conexion a BBDD")
