from conexionoracle47eliminarenfermos import conexionOracleEnfermos

print ("Probando clases de Oracle: Enfermos")
print("Elija 1 para eliminar apellido o 2 para cambiar una iscripcion")
opcion=int(input())
if (opcion==1):#creamos un objeto connection para ejecutar la eliminacion del enfermo
    print ("Introduzca una inscripcion")
    inscripcion=int(input())
    connection= conexionOracleEnfermos()
    eliminados=connection.eliminarEnfermo(inscripcion) 
    print (f"Enfermos elimininados:{eliminados}")
    print ("Fin de Eliminacion")
else:#creamos otro objeto connection para hacer la modificacion del apellido del enfermo
    print("Introduzca una inscripcion")
    inscripcion=int(input())
    print("Cual es el nuevo apellido del paciente?")
    apellido= input()
    connection = conexionOracleEnfermos()
    cambiados = connection.modificarEnfermo(apellido, inscripcion)
    print (f"Enfermos actualizados:{cambiados}")
    print ("Fin de la Actualizacion")

