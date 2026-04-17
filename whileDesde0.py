print("El while siempre lleva una orden logica")
# > < != and or not

i = 0

while i < 27:
    print(f"Mes abril fecha {i}")
    i += 1


num_correcto = 3
ganaste = True
i = 0

while ganaste and i < 10:
    num = int(input("Adivine un número del 1 al 10: "))
    i += 1

    if num < 1 or num > 10:
        print("Número no válido")
    elif num == num_correcto:
        print("¡Ganaste!")
        ganaste = False
    else:
        print("Intenta de nuevo")

if ganaste:
    print("Perdiste, se acabaron los intentos.")

# version del ing
detener = True
numeroSecreto = 15
intentos = 0

while detener:

    if intentos > 10:
        break
    numero = int(input("Adivina el numero del 1 al 20: "))
    if numero < 0 and numero > 20:
        print("Numero no valido")
    elif numero == numeroSecreto:
        print("Lo lograste")
        detener = False
    intentos += 1
