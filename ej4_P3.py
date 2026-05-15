for numero in range(1, 51):
    if numero == 42:
        print("Amenaza detectada en registro 42. Proceso detenido.")
        break

    elif numero % 3 == 0:
        continue

    else:
        print(f"Procesando registro ID: {numero}")
