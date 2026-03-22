frase = input("Ingrese una frase: ")

conteo = frase.count("a")
if conteo > 0:
    print("La letra 'a' aparece ", conteo, "veces en la frase")
else:
    print("La letra 'a' no aparece en la frase")
