#PRACTICA METODOS: CALCULADORA

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def mostrarMenu():
    print("Bienvenido a mi calculadora, seleccione una operacion del menu")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    
    

#--------------------------------------------------------------

mostrarMenu()
opcion=int(input())
if (opcion!=1):
    if(opcion!=2):
        if(opcion!=3):
            if(opcion!=4):
                print("La opcion no es válida")
            else:
                print("Introduzca el primer numero")
                dig1=int(input())
                print("Introduzca el segundo numero")
                dig2=int(input())
            
                if (opcion==1):
                    resultado= suma(dig1,dig2)
            
                elif(opcion==2):
                    resultado= resta(dig1,dig2)
                
                elif(opcion==3):
                    resultado= mult(dig1,dig2)
            
                print (resultado)
    
print("Fin de Programa")
