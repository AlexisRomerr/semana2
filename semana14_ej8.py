# 8. Crear un programa que almacene 5 productos en un arreglo y mediante una función busque un producto específico ingresado por el usuario.

productos = []
ingresos = 0

while ingresos < 5:
    productos_user = input("Ingrese 5 productos: ")
    ingresos += 1
    productos.append(productos_user)


def buscar_producto():
    buscar = input("Ingrese el producto a buscar: ")
    for i in productos:
        if buscar.lower() == i.lower():
            print(f"Producto encontrado: {i.capitalize()}")
            return
    print("Producto no encontrado")


buscar_producto()
