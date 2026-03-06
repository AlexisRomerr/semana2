Algoritmo Parcial01_ej1
	Definir nota Como Entero
	
	Repetir 
	Escribir "Ingrese la nota del estudiante (del 0 al 10)"
	Leer nota
	
	Si nota < 0 o nota > 10 Entonces
		Escribir "Solo se aceptan notas del 0 al 10"
	FinSi
	
Hasta Que nota >= 0 Y nota <= 10

	Si nota >= 6 Entonces 
	Escribir "Esta aprobado"
FinSi

Si nota <= 4 Entonces
	Escribir "Esta reprobado"
FinSi

Si nota = 5 Entonces
	
Escribir "Necesita recuperación"
FinSi

Escribir "Su nota es " , nota
FinAlgoritmo
