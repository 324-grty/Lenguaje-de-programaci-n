#Calculadora básica: Pide dos números y luego un tercer número (1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir). usando switch-case.
def calculadora(num1, num2, operacion):
    switcher = {
        1: num1 + num2,
        2: num1 - num2,
        3: num1 * num2,
        4: num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    return switcher.get(operacion, "Operación inválida, por favor ingresa un número del 1 al 4.")
try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    operacion = int(input("Ingresa la operación (1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir): "))
    resultado = calculadora(num1, num2, operacion)
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")
