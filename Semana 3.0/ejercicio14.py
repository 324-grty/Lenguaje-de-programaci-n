#​Conversor de divisas: 
# Pide una cantidad en moneda local y elige (1: a Dólares, 2: a Euros, 3: a Libras).usando solo switch-case.
def conversor_divisas(cantidad_local, opcion):
    switcher = {
        1: cantidad_local / 24.0,  # Convertir a Dólares (suponiendo 1 USD = 24 moneda local)
        2: cantidad_local / 28.0,  # Convertir a Euros (suponiendo 1 EUR = 28 moneda local)
        3: cantidad_local / 33.0   # Convertir a Libras (suponiendo 1 GBP = 33 moneda local)
    }
    return switcher.get(opcion, "Operación inválida, por favor ingresa 1, 2 o 3.")
try:
    cantidad_local = int(input("Ingresa la cantidad en moneda local: "))
    opcion = int(input("Elige la conversión (1: a Dólares, 2: a Euros, 3: a Libras): "))
    resultado = conversor_divisas(cantidad_local, opcion)
    if opcion == 1:
        print(f"{cantidad_local} en moneda local son {resultado:.2f} USD")
    elif opcion == 2:
        print(f"{cantidad_local} en moneda local son {resultado:.2f} EUR")
    elif opcion == 3:
        print(f"{cantidad_local} en moneda local son {resultado:.2f} GBP")
    else:
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")