dias = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]

while True:
    num = int(input("Ingrese un número del 1 al 7 para saber el día de la semana: "))
    if 1 <= num <= 7:
        break
    else:
        print("Opción inválida, solo existen 7 días en la semana, intente de nuevo.")


for i, dia in enumerate(dias, start=1):
    if i == num:
        print("Es", dia)
