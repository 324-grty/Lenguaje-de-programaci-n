"solicitar al usuario su edad y determinar su año de "
"nacimiento"

name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)
current_year = 2026
birth_year = current_year - int(age)
print(f"Hola {name}, naciste en el año {birth_year}.")
