# Promedio de notas
# Con while, permite ingresar notas hasta que el usuario escriba -1.
# Usa if para ignorar notas inválidas (menores a 0 o mayores a 10).
# Luego usa for para recorrer las notas válidas y calcular el promedio.

notas = []
while True:
    nota = float(input("Ingrese su nota (-1 para cerrar): "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)

if len(notas) > 0:
    suma = 0
    for n in notas:
        suma += n
    promedio = suma / len(notas)
    print("Promedio de notas válidas:", promedio)
