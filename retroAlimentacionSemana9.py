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
# print(comprobarDecadas)

# Si la cadema de texto tiene numeros
siTieneNumero = "Ever 2026"
## si este texto tiene numero -> True
## isnumeric -> es un espacio en la memoria
## isnumeric()-> dentro de la funcion

respuesta = siTieneNumero.isnumeric()
# print(respuesta)

## isnumeric como numeros que van a estar ejecutandose desde una
## cadena de texto


isLowerCase1 = "Ella se fue, me abandono y destrozo mi corazon"
minusculas = isLowerCase1.islower()
# print("Solo minusculas: ", minusculas)

isUpperCase = "Cristiano Leo Son"
mayusculas = isUpperCase.isupper()
# print("Solo mayusculas: ", mayusculas)

fraseIconica = "Soltala Erika"
respuesta = fraseIconica.isupper()
# print(respuesta)

respuesta = fraseIconica.upper().isupper()
# print(respuesta)

respuesta = fraseIconica.title().istitle()
print(fraseIconica, respuesta)

## cuando una funcion retorna algo (tipo de datos)
## string -> espacio de memoria diferentes al de un espacio numerico
## int
## float
## Decimal
## Boolean

# string -> E v e r -> lista o un array

print(Serie)
Serie = "Chapulin Colorado"
# print(Serie)

controlarEspacio = Serie.isspace()
# print(controlarEspacio)

## metodos de busqueda

tema = "En el bosque de china la chinita se perdio  "
#  E n e l b o s q u e  d  e  c  h  i  n  a  l  a  c  h  i  n  i  t  a  s  e  p  e  r  d  i  o
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
# siempre parte desde el 0 al ultimo numero
temaf = tema.find("se")
# print(temaf)


temaf = tema.upper().rfind("BOSQUE")
# print(temaf)

poema = """Ella amará a otro hombre.
Yo voy lejos, andando hacia el olvido.
Y puede suceder que alguien me nombre,
pero ella fingirá no haber oído.

Ella amará a otro hombre:
el tiempo pasa y el amor finaliza,
y es natural que lo que fue una brasa
acabe convirtiéndose en ceniza."""

contador = poema.count("i")
contador = poema.startswith("Ella")
contador = poema.endswith("ceniza.")

poemaModificado = poema.replace("Ella", "Lupita").replace("amará", "floow")
print(poemaModificado)
