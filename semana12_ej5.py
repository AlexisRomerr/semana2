while True:
    decidir = int(input("Seleccione (1=suma, 2=resta, 3=multi, 4=div): "))
    if 1 <= decidir <= 4:
        break
    print("Opción inválida, intente de nuevo.")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if decidir == 1:
    resultado = num1 + num2
    print("Resultado de la suma:", resultado)
elif decidir == 2:
    resultado = num1 - num2
    print("Resultado de la resta:", resultado)
elif decidir == 3:
    resultado = num1 * num2
    print("Resultado de la multiplicación:", resultado)
elif decidir == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado de la división:", resultado)
    else:
        print("Error: no se puede dividir entre cero")
