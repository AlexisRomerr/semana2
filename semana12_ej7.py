while True:
    monto = int(input("Ingrese el monto de la compra: "))
    if monto > 0:
        break
    else:
        print("Ingrese un monto mayor que 0.")


if monto > 100:
    porcentaje = 20
    descuento = monto * 0.20
elif monto >= 50:
    porcentaje = 10
    descuento = monto * 0.10
else:
    porcentaje = 0
    descuento = 0

total = monto - descuento


print("Monto normal:", monto, "dolares")
print("Se aplica un descuento del", porcentaje, "%")
print("Descuento de:", descuento, "dolares")
print("Su total:", total, "dolares")
