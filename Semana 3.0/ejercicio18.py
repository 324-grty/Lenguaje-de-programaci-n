#Clasificación de vehículos: Pide el número de ruedas
#  (2, 4, 6, 18) y di qué tipo de vehículo podría ser.

def clasificacion_vehiculo(ruedas):
    switcher = {
        2: "Motocicleta",
        4: "Coche",
        6: "Camioneta",
        18: "Camión"
    }
    return switcher.get(ruedas, "Número inválido, por favor ingresa un número de ruedas válido (2, 4, 6, 18).")
try:
    ruedas = int(input("Ingresa el número de ruedas del vehículo: "))
    tipo_vehiculo = clasificacion_vehiculo(ruedas)
    print(f"Un vehículo con {ruedas} ruedas podría ser: {tipo_vehiculo}")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")