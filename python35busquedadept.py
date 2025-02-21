import oracledb
connection = oracledb.connect (user='system', password='oracle', dsn='localhost/xe')
print("Conectado a BBDD")
consulta=connection.cursor() 
print("Buscamos el departamento 10")
sql="select * from dept where dept_no=10" 
consulta.execute(sql)
row=consulta.fetchone()
print(row)
nombre=row[1]
localidad=row[2]
print(nombre, ",", localidad)
#hasta aqui hemos realizado una consulta donde, internamente, le decimos que departamento queremos buscar y el dato existe

#ahora buscamos algo que NO existe
print("=========================================================")
print("Buscamos el departamento 110")
sql="select * from dept where dept_no=110" 
consulta.execute(sql)
row=consulta.fetchone()
if (not row):
    print("No existe el departamento")
else:
    nombre=row[1]
    localidad=row[2]
    print(nombre, ",", localidad)
print("=========================================================")
    
#ahora pedimos al usuario que indique el departamento
print("Introduzca el número de departamento que busca")
depar=input()
sql="select * from dept where dept_no="+depar
consulta.execute(sql)
row=consulta.fetchone()
if (not row):
    print("No existe el departamento que busca")
else:
    nombre=row[1]
    localidad=row[2]
    print("El departamento",depar, "corresponde a ", nombre, "en", localidad)

consulta.close() 
connection.close() 
print("Fin de Acceso la BBDD")