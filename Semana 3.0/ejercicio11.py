#Cajero automático: Define un saldo inicial.
# El usuario elige (1: Ver saldo, 2: Depositar, 3: Retirar).
cajero_automatico = 1000.0  # Saldo inicial
def cajero(saldo, opcion, cantidad=0):
    switcher = {
        1: f"Tu saldo actual es: Q{saldo:.2f}",
        2: f"Has depositado: Q{cantidad:.2f}. Nuevo saldo: Q{saldo + cantidad:.2f}",
        3: f"Has retirado: Q{cantidad:.2f}. Nuevo saldo: Q{saldo - cantidad:.2f}" if cantidad <= saldo else "Error: Fondos insuficientes."
    }
    return switcher.get(opcion, "Opción inválida, por favor ingresa 1, 2 o 3.")
try:
    opcion = int(input("Elige una opción (1: Ver saldo, 2: Depositar, 3: Retirar): "))
    if opcion == 1:
        resultado = cajero(cajero_automatico, opcion)
        print(resultado)
    elif opcion == 2:
        cantidad = float(input("Ingresa la cantidad a depositar: "))
        resultado = cajero(cajero_automatico, opcion, cantidad)
        print(resultado)
        cajero_automatico += cantidad  # Actualizar saldo
    elif opcion == 3:
        cantidad = float(input("Ingresa la cantidad a retirar: "))
        resultado = cajero(cajero_automatico, opcion, cantidad)
        print(resultado)
        if "Error" not in resultado:
            cajero_automatico -= cantidad  # Actualizar saldo
    else:
        print("Opción inválida, por favor ingresa 1, 2 o 3.")
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")