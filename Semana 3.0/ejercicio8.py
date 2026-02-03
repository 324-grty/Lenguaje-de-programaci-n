#Conversor de temperatura: El usuario ingresa grados Celsius y elige (1: a Fahrenheit, 2: a Kelvin). usando switch-case.
def conversor_temperatura(grados_celsius, opcion):
    switcher = {
        1: (grados_celsius * 9/5) + 32,  # Convertir a Fahrenheit
        2: grados_celsius + 273.15       # Convertir a Kelvin
    }
    return switcher.get(opcion, "Operación inválida, por favor ingresa 1 o 2.")
try:
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    opcion = int(input("Elige la conversión (1: a Fahrenheit, 2: a Kelvin): "))
    resultado = conversor_temperatura(grados_celsius, opcion)
    if opcion == 1:
        print(f"{grados_celsius}°C son {resultado}°F")
    elif opcion == 2:
        print(f"{grados_celsius}°C son {resultado}K")
    else:
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")