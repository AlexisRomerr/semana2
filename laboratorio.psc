    Algoritmo laboratorioo
		
		
		Definir dividendo, divisor Como Entero
		Definir valido Como Logico
		Definir total Como Real
		
		valido = Falso
		
		
		Escribir "Ingrese 2 valores que no sean negativos para poder dividirlos"
		
		Repetir 
			Escribir "Ingrese el dividendo"
			Leer dividendo 
			
			Si NO (dividendo < 0) Entonces
				valido = Verdadero
			Sino
				Escribir "No se aceptan números negativos"
				valido = Falso
			FinSi
			
		Hasta Que valido = Verdadero
		
		valido = Falso
		
		Repetir
			
			Escribir "Ingrese el divisor" 
			Leer divisor 
			
			Si NO  (divisor < 0 O divisor = 0) Entonces
				
				valido = Verdadero
				
			Sino
				Escribir "No se aceptan números negativos ni cero"
				valido = falso
			FinSi
			
			
		Hasta Que  valido = Verdadero
		
		Si NO (dividendo < 0) Y  NO (divisor <= 0) Entonces

			total = dividendo / divisor
			
		FinSi 
		
		Escribir "Números validos, el resultado es ", total 
		
		
		
		
		
		
		
FinAlgoritmo


