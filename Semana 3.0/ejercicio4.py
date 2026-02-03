#​Días del mes: Pide el número de un mes y muestra cuántos días tiene 
#(ignora años bisiestos). usando switch-case.
def dias_del_mes(numero):
    switcher = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return switcher.get(numero, "Número inválido, por favor ingresa un número del 1 al 12.")
try:
    numero = int(input("Ingresa un número del 1 al 12: "))
    dias = dias_del_mes(numero)
    meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
    if isinstance(dias, int):
        print(f"{meses[numero]} tiene {dias} días.")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")
