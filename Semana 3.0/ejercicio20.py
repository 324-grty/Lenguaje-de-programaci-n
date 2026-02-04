#​Conversor de tiempo: Pide una cantidad en segundos 
# y permite elegir (1: a Minutos, 2: a Horas). usando switch-case.
def conversor_tiempo(segundos, opcion):
    switcher = {
        1: segundos / 60,    # Convertir a Minutos
        2: segundos / 3600   # Convertir a Horas
    }
    return switcher.get(opcion, "Operación inválida, por favor ingresa 1 o 2.")
try:
    segundos = int(input("Ingresa la cantidad de segundos: "))
    opcion = int(input("Elige la conversión (1: a Minutos, 2: a Horas): "))
    resultado = conversor_tiempo(segundos, opcion)
    if opcion == 1:
        print(f"{segundos} segundos son {resultado} minutos")
    elif opcion == 2:
        print(f"{segundos} segundos son {resultado} horas")
    else:
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")