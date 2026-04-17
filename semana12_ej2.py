edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad invalida")
elif edad < 18:
    print("Usted es menor de edad")
elif edad >= 18 and edad < 60:
    print("Usted es mayor de edad")
elif edad >= 60 and edad < 80:
    print("Usted es un adulto mayor")
elif edad >= 80 and edad <= 100:
    print("Usted es un anciano")
else:
    print("Usted es el diablo o hackeo la vida")
