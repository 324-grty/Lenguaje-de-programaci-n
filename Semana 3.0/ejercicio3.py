#​Estaciones del año: Pide el número de un mes y di a qué estación pertenece (ej: 1, 2, 12 = Invierno). usando switch-case.
def estacion_del_año(numero):
    switcher = {
        1: "Invierno",
        2: "Invierno",
        3: "Primavera",
        4: "Primavera",
        5: "Primavera",
        6: "Verano",
        7: "Verano",
        8: "Verano",
        9: "Otoño",
        10: "Otoño",
        11: "Otoño",
        12: "Invierno"
    }
    return switcher.get(numero, "Número inválido, por favor ingresa un número del 1 al 12.")
try:
    numero = int(input("Ingresa un número del 1 al 12: "))
    estacion = estacion_del_año(numero)
    print(estacion)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")