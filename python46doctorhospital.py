import oracledb
connection= oracledb.connect(user='system', password='oracle', dsn='localhost/xe')

print("----------- Insertar Nuevo Doctor en Hospital ------------")
#pido los datos que introduce el usuario
print("Introduzca el apellido del nuevo doctor")
apellido=input()
print("Introduzca la especialidad del nuevo doctor")
especialidad=input()
print("Introduzca el salario del nuevo doctor")
salario=int(input())

#pido el hospital
selecthospital="select nombre, hospital_cod from hospital order by 1"
cursor=connection.cursor()
cursor.execute(selecthospital)
cont=1
listahospital=[]
for row in cursor:
    print(f"{cont} = {row[0]}")
    listahospital.append(row[1])
    cont=cont+1
cursor.close()
print ("Seleccione una opcion de la lista")
opcion= int(input())
hospital= listahospital[opcion-1]
print("el hospital que ha escogido es ", row[0],"con codigo:", row[1])
print("==========================================================")


#obtener el codigo del doctor: el proximo al numero maximo disponible
sqlmaxdoc_no="select max(doctor_no)+1 from doctor"
cursor=connection.cursor()
cursor.execute(sqlmaxdoc_no)
row=cursor.fetchone()
doc_no=row[0]
print (doc_no)
cursor.close()


#insertamos todos los datos anteriores: codigo hospital, numero de doctor, apellido, espcialidad y salario
sqlinsertdoctor = "insert into doctor values (:p1, :p2, :p3, :p4, :p5)"
cursor=connection.cursor()
cursor.execute(sqlinsertdoctor,(hospital, doc_no, apellido, especialidad, salario))
cursor.close()

registro=cursor.rowcount
print(f"Doctores insertados:{registro}")
connection.commit()
cursor.close
connection.close()
print("Finde conexion a la BBDD")


