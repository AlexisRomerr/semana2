Algoritmo Parcial01_ej9
	
	Definir num Como Entero
	Definir positiv Como Logico
	
	Escribir "Ingrese un numero divisible entre 3 o 5"
	Leer num
	
	Si num % 3 = 0 O num % 5 = 0 Entonces
		positiv = Verdadero
		Escribir "Su valor es ", positiv
		
	SiNo
			positiv = Falso
			Escribir "Su valor es ", positiv
	FinSi
	
FinAlgoritmo
