# Suma acumulativa con límite
# Con while, pide números hasta que la suma supere 100.
# Usa if para ignorar números negativos.
# Luego usa for para mostrar todos los números válidos ingresados.

suma = 0
numeros = []

while suma <= 100:
    num = int(input("Ingrese un número: "))

    if num < 0:
        continue

    numeros.append(num)
    suma += num


print("Números válidos ingresados:")
for n in numeros:
    print(n)

print("Suma total:", suma)
