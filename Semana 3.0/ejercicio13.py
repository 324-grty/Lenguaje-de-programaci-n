#Tipos de suscripción: Pide un número 
# (1: Plan Básico Q.9, 2: Plan Estándar Q.15, 3: Plan Premium Q.20) y muestra los beneficios.usando solo switch-case.
def tipo_de_suscripcion(numero):
    switcher = {
        1: "Plan Básico Q.9: Acceso a contenido limitado.",
        2: "Plan Estándar Q.15: Acceso a contenido estándar y calidad HD.",
        3: "Plan Premium Q.20: Acceso ilimitado a todo el contenido en calidad Ultra HD."
    }
    return switcher.get(numero, "Número inválido, por favor ingresa un número del 1 al 3.")
try:
    numero = int(input("Ingresa un número del 1 al 3 para seleccionar tu plan de suscripción: "))
    beneficios = tipo_de_suscripcion(numero)
    print(beneficios)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")
    