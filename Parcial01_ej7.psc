Algoritmo Parcial01_ej7
	
	Definir num1, num2, producto Como Entero
	Definir cociente Como Real
	
	Escribir "Ingrese un numero para sacar su producto y cociente"
	Leer num1
	
	Escribir "Ingrese otro numero para sacar su producto y cociente"
	Leer num2
	
	producto = num1 * num2
	Escribir "Su producto es: ", producto
	
	Si num2 <> 0 Entonces
	cociente = num1 / num2
	Escribir "Su cociente es: ", cociente
	
    SiNo 
		Escribir "No se puede dividir entre 0"
		
	FinSi
	
FinAlgoritmo
