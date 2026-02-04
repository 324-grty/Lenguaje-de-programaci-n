#​Código de error HTTP: El usuario ingresa un código 
#(200, 404, 500, 403) y el programa explica qué significa. usando switch-case.
def explicar_codigo_http(codigo):
    switcher = {
        200: "OK: La solicitud ha tenido éxito.",
        404: "Not Found: El servidor no ha encontrado nada que coincida con la URI solicitada.",
        500: "Internal Server Error: El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.",
        403: "Forbidden: El servidor entendió la solicitud, pero se niega a autorizarla."
    }
    return switcher.get(codigo, "Código inválido, por favor ingresa 200, 404, 500 o 403.")
try:
    codigo = int(input("Ingresa un código HTTP (200, 404, 500, 403): "))
    explicacion = explicar_codigo_http(codigo)
    print(explicacion)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")