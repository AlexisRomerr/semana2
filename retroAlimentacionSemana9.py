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
saludo(Serie)
saludo(fmaTemu)

fmaMayusculas = Serie.upper()
saludo(fmaMayusculas)

FullmetalCapitalize = Serie.capitalize()
saludo(FullmetalCapitalize)
