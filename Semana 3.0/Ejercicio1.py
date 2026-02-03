#​Día de la semana: Pide un número del 1 al 7 y muestra el nombre del día (1=Lunes, etc.) utilizando switch-case.
def dia_de_la_semana(numero):
    switcher = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return switcher.get(numero, "Número inválido, por favor ingresa un número del 1 al 7.")
try:
    numero = int(input("Ingresa un número del 1 al 7: "))
    dia = dia_de_la_semana(numero)
    print(dia)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")


