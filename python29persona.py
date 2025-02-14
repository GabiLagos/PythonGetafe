from class29persona import Persona 
print ("PRUEBA CLASE PERSONA")
 #crear nueva persona
persona1 = Persona()
print(persona1.pais)

persona2 = Persona ()
print (persona2.pais)

persona1.pais="España"
persona1.birthyear=1973
persona1.primernombre="Loreto"
persona1.primerapellido="Lagos"


print (persona1.getNombreCompleto(), "tiene", persona1.getEdad(), "años y vive en " + persona1.pais)
print("=======================================================")
print(persona1)
print("=======================================================")
print(persona1.getDescripcion)