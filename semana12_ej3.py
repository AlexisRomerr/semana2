nota = float(input("Ingrese su nota: "))

if 0 <= nota < 6:
    print("Usted ha reprobado")
elif 6 <= nota < 7:
    print("Usted ha aprobado")
elif 7 <= nota < 9:
    print("Su calificación es buena")
elif 9 <= nota <= 10:
    print("Su nota es excelente")
else:
    print("Nota inválida")
