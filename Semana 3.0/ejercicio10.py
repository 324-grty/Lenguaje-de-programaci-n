#Calculadora de potencia/raíz: Pide un número y elige (1: Elevar al cuadrado, 2: Raíz cuadrada) usando switch-case.
def potencia_o_raiz(numero, opcion):
    switcher = {
        1: f"El número elevado al cuadrado es: {numero ** 2}",
        2: f"La raíz cuadrada del número es: {numero ** 0.5}" if numero >= 0 else "No se puede calcular la raíz cuadrada de un número negativo."
    }
    return switcher.get(opcion, "Opción inválida, por favor ingresa 1 o 2.")
try:
    numero = float(input("Ingresa un número: "))
    opcion = int(input("Elige la opción (1: Elevar al cuadrado, 2: Raíz cuadrada): "))
    resultado = potencia_o_raiz(numero, opcion)
    print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")