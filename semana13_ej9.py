# Juego de adivinar número
# Genera un número secreto.
# Con while, permite intentos hasta acertar.
# Usa if para dar pistas (mayor o menor).
# Luego usa for para mostrar todos los intentos realizados.

num_correcto = 3
ganaste = True
i = 0
intentos = []

while ganaste and i < 10:
    num = int(input("Adivine un número del 1 al 10: "))
    intentos.append(num)
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

print("Total de intentos:", len(intentos))
print("Intentos realizados:", intentos)
