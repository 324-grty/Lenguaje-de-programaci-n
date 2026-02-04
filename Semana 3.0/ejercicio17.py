#​Direcciones de brújula: Pide un ángulo 
# (0, 90, 180, 270) y muestra el punto cardinal correspondiente. usando solo switch-case.
def punto_cardinal(angulo):
    switcher = {
        0: "Norte",
        90: "Este",
        180: "Sur",
        270: "Oeste"
    }
    return switcher.get(angulo, "Ángulo inválido, por favor ingresa uno de los siguientes valores: 0, 90, 180, 270.")
try:
    angulo = int(input("Ingresa un ángulo (0, 90, 180, 270): "))
    direccion = punto_cardinal(angulo)
    print(direccion)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")