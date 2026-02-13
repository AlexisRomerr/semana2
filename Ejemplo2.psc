Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroCuenta, cantidadSaliente, Saldo, preguntar  Como Entero
	
	cuentaDeAhorro= 1000
	
	numeroCuenta=12345
	
	
	Escribir "Bienvenido"
	Escribir "Actividad que desea realizar"
	Escribir "1 para consultar"
	Escribir "2 para extraer dinero de la cuenta de ahorro"
	
	Escribir "Escriba la actividad que desea realizar" 
	Leer preguntar
	
	
	
	SI preguntar == 1
		Escribir "Escriba el numero de cuenta a operar" 
		Leer preguntar
		
		si preguntar == numeroCuenta
			Escribir "Su saldo es " , cuentaDeAhorro
			
			
		FinSi
	FinSi
	
	SI preguntar == 2
		Escribir "Escriba el numero de cuenta a operar" 
		Leer preguntar
		
		si preguntar == numeroCuenta
			Escribir "Escriba el monto a extraer "
			Leer preguntar
			
			si preguntar <= cuentaDeAhorro
				Saldo = cuentaDeAhorro - preguntar
				Escribir "Procesando"
				Escribir "Su saldo actual es de " , Saldo
			FinSi
		FinSi
	FinSi
FinAlgoritmo
