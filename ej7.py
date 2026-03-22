frase = input("Ingrese una frase que contenga minimo una vez la palabra Python: ")

if "Python" in frase or "python" in frase:
    frase_nueva = frase.replace("Python", "Programacion")
    frase_nueva = frase_nueva.replace("python", "programacion")
    print("Frase nueva:", frase_nueva)
else:
    print("La frase no contiene la palabra Python")
