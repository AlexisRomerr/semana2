Algoritmo bucle
		
		Definir contador Como Entero
		Escribir " numero del 0 al 100 "
		Leer numeroEntrada
		contador = 0
		resultado = 0
		anterior = 0
		sumar = 0
		
		Mientras contador < numeroEntrada
			
		
			anterior = resultado
			contador = contador + 1
			resultado = contador + anterior

		
			Escribir "resultado es " , contador ," + ", anterior , " = " , resultado
		FinMientras
		
		Escribir "passwoord "
		Leer pass
	
		mientras pass <> "nombre de ella + fecha especial"
			Escribir "Romper bucle infinito 1 si 2 no"
			Leer respuesta
		
			
			si respuesta == "si"
				pass = "nombre de ella + fecha especial"
			FinSi
			FinMientras
		Escribir "final "
FinAlgoritmo
