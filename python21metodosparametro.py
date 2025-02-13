print("EJEMPLO DE METODOS CON PARAMETROS")

def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs ", nombre )
    
def despedirse(nombre, dia):
    print("Un placer de verlo hoy", dia, " Mr/Mrs ", nombre)
    
#------------------------------------------------------------
name= "Fulanito"
dia= "miercoles"

saludar(name)
despedirse(name,dia)

print("Fin del Codigo")
