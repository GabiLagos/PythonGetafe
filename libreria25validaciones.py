def validarIsbn(isbn):
    if isbn.isdigit() and len(isbn) == 10:
        longitud = len(isbn)
        suma = 0

        for i in range(longitud):
            num = int(isbn[i])
            op = num * (i + 1)
            suma += op
        
        if (suma % 11 == 0):
            respuesta=1
        else:
            respuesta=0
            
    else:
        respuesta=0
        
    return respuesta

def validarDni(dni):
    op1 = dni - int(dni/23)*23
    # otra manera, usando la funcion resto op1= dni%23

    if (op1 == 0):
        letra= "T"
    elif (op1 == 1):  
        letra= "R"
    elif (op1 == 2):
        letra= "W"
    elif (op1 == 3):
        letra= "A"
    elif (op1 == 4):
        letra= "G"
    elif (op1 == 5):
        letra= "M"
    elif (op1 == 6):
        letra= "Y"
    elif (op1 == 7):
        return "F"
    elif (op1 == 8):
        letra= "P"
    elif (op1 == 9):
        letra= "D"
    elif (op1 == 10):
        letra= "X"
    elif (op1 == 11):
        letra= "B"
    elif (op1 == 12):
        letra= "N"
    elif (op1 == 13):
        reletra= "J"
    elif (op1 == 14):
        letra= "Z"
    elif (op1 == 15):
        reletra= "S"
    elif (op1 == 16):
        letra= "Q"
    elif (op1 == 17):
        letra= "V"
    elif (op1 == 18):
        letra= "H"
    elif (op1 == 19):
        reletra= "L"
    elif (op1 == 20):
        letra= "C"
    elif (op1 == 21):
        letra= "K"
    elif (op1 == 22):
        letra= "E"
    elif (op1 == 23):
        letra= "T"
    return letra