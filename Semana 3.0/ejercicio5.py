#​Conversor de números a romano: Pide un número del 1 al 10 y muestra su equivalente en romano. usando switch-case.
def numero_a_romano(numero):
    switcher = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"
    }
    return switcher.get(numero, "Número inválido, por favor ingresa un número del 1 al 10.")
try:
    numero = int(input("Ingresa un número del 1 al 10: "))
    romano = numero_a_romano(numero)
    print(f"El número {numero} en romano es: {romano}")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")
    