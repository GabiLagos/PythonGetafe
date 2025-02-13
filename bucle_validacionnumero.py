def pedir_numero():
    while True:
        entrada = input("Por favor, ingresa un número: ")
        if entrada.isdigit():  # Verifica si la entrada es un número entero positivo
            return int(entrada)  # Convierte la entrada a entero y la devuelve
        else:
            print("Esto no es un número, intente de nuevo.")  # Mensaje de error

# Llamar a la función
numero_valido = pedir_numero()
print(f"Has ingresado el número: {numero_valido}")

