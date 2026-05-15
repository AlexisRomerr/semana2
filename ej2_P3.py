from decimal import Decimal

total = Decimal("0")

while True:
    try:
        precios = Decimal(input("Ingrese el precio del producto. 0 para salir: "))
        if precios == 0:
            break
        total += precios

    except ValueError:
        print("Advertencia: Debe ingresar un numero válido")

    except:
        print("Entrada inválida")

print(f"Total acumulado: ${total}")
