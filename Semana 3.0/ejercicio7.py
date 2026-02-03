#​Áreas de figuras: Pide al usuario elegir una figura 
# (1: Cuadrado, 2: Triángulo, 3: Círculo) y solicita los datos necesarios para calcular su área.
#usando switch-case.
import math
def area_de_figura(figura, dimensiones):
    switcher = {
        1: lambda lado: lado * lado,  # Área del cuadrado
        2: lambda base, altura: (base * altura) / 2,  # Área del triángulo
        3: lambda radio: math.pi * radio * radio  # Área del círculo
    }
    func = switcher.get(figura, None)
    if func:
        return func(*dimensiones)
    else:
        return "Número inválido, por favor ingresa 1, 2 o 3."
try:
    figura = int(input("Elige una figura (1: Cuadrado, 2: Triángulo, 3: Círculo): "))
    if figura == 1:
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = area_de_figura(figura, (lado,))
    elif figura == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = area_de_figura(figura, (base, altura))
    elif figura == 3:
        radio = float(input("Ingresa el radio del círculo: "))
        area = area_de_figura(figura, (radio,))
    else:
        area = "Número inválido, por favor ingresa 1, 2 o 3."
    print(f"El área es: {area}")
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")
    