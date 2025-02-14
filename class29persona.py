# A CREAR UNA NUEVA CLASE
 
class Persona: #buena practica, las palabras comienzan con mayúscula
    primernombre = ""
    segundonombre = ""
    primerapellido = ""
    segundoapellido = ""
    email = ""
    birthyear = 0
    pais = ""
    descripcion = ""
    
    def __init__(self):
        self.pais = "Francia" #cuando se cree una persona, por defecto tendrá como país Francia
    
    def __str__(self): #define que quiero que aparezca cuando hago print(persona) estando un programa.py
        return self.primernombre +" "+ self.primerapellido +" "+ self.pais
    
    def getNombreCompleto(self):
        return self.primernombre + " " + self.segundonombre + " " + self.primerapellido + " " + self.segundoapellido
    
    def getEdad(self):
        return 2025 - self.birthyear
    
    def getDescripcion(self, desc):
        return self.primernombre + self.primerapellido + self.descripcion