#​Cálculo de impuestos: Pide el salario y el tipo de empleado 
# (1: Público 10%, 2: Privado 15%, 3: Independiente 8%).usando solo switch-case.
def calcular_impuesto(salario, tipo_empleado):
    switcher = {
        1: 0.10,
        2: 0.15,
        3: 0.08
    }
    tasa_impuesto = switcher.get(tipo_empleado, None)
    if tasa_impuesto is None:
        return "Número inválido, por favor ingresa un tipo de empleado del 1 al 3."
    impuesto = salario * tasa_impuesto
    return f"El impuesto para un salario de Q{salario} como empleado tipo {tipo_empleado} es: Q{impuesto:.2f}"
try:
    salario = float(input("Ingresa tu salario: Q"))
    tipo_empleado = int(input("Ingresa el tipo de empleado (1: Público, 2: Privado, 3: Independiente): "))
    resultado = calcular_impuesto(salario, tipo_empleado)
    print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa números válidos.")