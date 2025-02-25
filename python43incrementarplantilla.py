import oracledb

print("Incrementar salario plantilla/hospital")
print("Introduzca ID de hospital")
idhopsital =int(input())
print("Introduzca incremento salaraila")
incremento =int(input())
connection= oracledb.connect(user='system', password='oracle', dsn='localhost/xe')

sqlupdate = "update plantilla set salario = salario +:p1 where hospital_cod=:p2"

cursor=connection.cursor()
cursor.execute(sqlupdate, (incremento,idhopsital))
registros=cursor.rowcount
print(f"Registros modificados: {registros}")
connection.commit()
cursor.close()

sqlselect="select apellido, funcion, salario from plantilla where hopital_cod=:p1"
cursor=connection.cursor()
cursor.execute(sqlselect, (idhopsital,))
for ape, fun, sal in cursor:
    print(f"Apellido:{ape}, Funcion: {fun}, Salario:{sal}")
cursor.close()
connection.close()
print ("Fin conexion a BBDD")