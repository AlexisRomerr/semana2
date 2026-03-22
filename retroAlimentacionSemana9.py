Serie = "fullmetal alchemits"
## es arreglo es una variable que tiene adentro otra variable
## Listas.
## Arrays.-> se inia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones simpre van  a tener ()
# -------------------------------------------------------
## las funciones tienen un espacio
## Scope es dond reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
# saludo(Serie)
# saludo(fmaTemu)

fmaMayusculas = Serie.upper()
# saludo(fmaMayusculas)

FullmetalCapitalize = fmaMayusculas.swapcase().title()

# saludo(FullmetalCapitalize)

comparar1 = "Ever "
comparar2 = "Ever"

variableTemporal = comparar1.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
# print(comparar)

clasicas2005 = "Gasolina"
compararisAlpha = clasicas2005.isalpha()
# print(compararisAlpha, 2005)

letraCancion = "Lo que paso, paso, entre tu y yo."
decada = "10"

# isalnum verifica si la cadena solo tiene numeros y si es asi da True
# si tiene un solo espacio dara False tambien.

ejemplo = letraCancion.isalnum()
# print(ejemplo)

ejemplo = decada.isalnum()
# print(ejemplo)

comprobarDecadas = decada.isdigit()
print(comprobarDecadas)
