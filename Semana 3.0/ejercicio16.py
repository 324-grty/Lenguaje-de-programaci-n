#Piedra, Papel o Tijera: El usuario ingresa 1, 2 o 3. Usa match-case para 
# determinar qué eligió y compararlo contra un valor fijo. 

def piedra_papel_tijera(eleccion_usuario):
    match eleccion_usuario:
        case 1:
            return "Has elegido Piedra."
        case 2:
            return "Has elegido Papel."
        case 3:
            return "Has elegido Tijera."
        case _:
            return "Número inválido, por favor ingresa 1, 2 o 3."
try:
    eleccion_usuario = int(input("Ingresa tu elección (1: Piedra, 2: Papel, 3: Tijera): "))
    resultado = piedra_papel_tijera(eleccion_usuario)
    print(resultado)
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")