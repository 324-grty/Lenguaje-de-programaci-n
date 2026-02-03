#​Paridad y signo: Pide un número y elige una opción
#  (1: Verificar si es par, 2: Verificar si es positivo/negativo). usando switch-case.
def paridad_o_signo(numero, opcion):
    switcher = {
        1: "El número es par." if numero % 2 == 0 else "El número es impar.",
        2: "El número es positivo." if numero > 0 else "El número es negativo." if numero < 0 else "El número es cero."
    }
    return switcher.get(opcion, "Opción inválida, por favor ingresa 1 o 2.")
try:
    numero = float(input("Ingresa un número: "))
    opcion = int(input("Elige la opción (1: Verificar si es par, 2: Verificar si es positivo/negativo): "))
    resultado = paridad_o_signo(numero, opcion)
    print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")
    