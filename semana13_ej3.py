# Tabla de multiplicar filtrada
# Pide un número.
# Con for, genera su tabla del 1 al 10.
# Usa if para mostrar solo resultados mayores a 20.
# Repite con while hasta que el usuario escriba -1.

while True:

    n = int(
        input(
            "ingrese un numero para generar su tabla de multiplicar del 1 al 10. Ingrese -1 para cerrar: "
        )
    )

    if n == -1:
        break

    print(f"\nTabla del {n} (solo resultados > 20):")

    for i in range(1, 11):
        resultado = n * i
        if resultado > 20:
            print(f"{n} x {i} = {resultado}")
