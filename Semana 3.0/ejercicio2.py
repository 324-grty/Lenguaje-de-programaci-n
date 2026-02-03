#Mes del año: Pide un número del 1 al 12 y muestra el nombre del mes.
def mes_del_año(numero):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return meses.get(numero, "Número inválido, por favor ingresa un número del 1 al 12.")
try:
    numero = int(input("Ingresa un número del 1 al 12: "))
    mes = mes_del_año(numero)
    print(mes)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")