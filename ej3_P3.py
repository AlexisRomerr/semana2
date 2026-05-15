i = 0
lecturas = []

while i < 5:
    temperaturas = int(input("Ingrese lecturas de temperatura: "))
    lecturas.append(temperaturas)
    i += 1

for temp in lecturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Critico"
            print(estado)
