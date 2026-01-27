#Solicitar al usuario su edad y determinar si es mayor de edad o menor,
#  si tiene exactamente la mayoria de edad, decirle: Ya es hora de sacar dpi
age=int(input("¿Cual es la edad?: "))

if (age > 18):
    print("Eeres mayor de edad: ")
elif (age < 18):
    print("Eres menor de edad: ")
else:
    print("Tienes que sacar ya tu DPI: ")