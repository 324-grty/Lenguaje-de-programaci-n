#​Sistema de notas: Pide una nota numérica (1-10) y muestra el rango 
# (1-4: Insuficiente, 5-6: Suficiente, 7-8: Notable, 9-10: Sobresaliente).usando solo switch-case.
def rango_nota(nota):
    switcher = {
        1: "Insuficiente",
        2: "Insuficiente",
        3: "Insuficiente",
        4: "Insuficiente",
        5: "Suficiente",
        6: "Suficiente",
        7: "Notable",
        8: "Notable",
        9: "Sobresaliente",
        10: "Sobresaliente"
    }
    return switcher.get(nota, "Número inválido, por favor ingresa una nota del 1 al 10.")
try:
    nota = int(input("Ingresa una nota del 1 al 10: "))
    rango = rango_nota(nota)
    print(f"La nota {nota} corresponde a: {rango}")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")