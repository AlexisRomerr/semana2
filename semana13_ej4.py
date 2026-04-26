# Suma de números impares
# Con while, pide números hasta que se ingrese 0.
# Usa if para sumar solo los números impares.
# Luego usa for para imprimir cada número impar ingresado.

suma = 0
impares = []
while True:
    n = int(input("Ingrese numeros (0 para cerrar): "))
    if n == 0:
        break

    if n % 2 != 0:
        impares.append(n)
        suma += n


for n in impares:
    print("Número impar ingresado:", n)


print("El resultado de la suma es:", suma)
