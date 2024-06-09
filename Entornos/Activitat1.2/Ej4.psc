Algoritmo Ej4
	CLAVE_CORRECTA <- "eureka"
	intentos <- 0
	acertado <- Falso
	Mientras intentos < 3 y no acertado Hacer
		Escribir "Introduce la clave:"
		Leer clave
		Si clave = CLAVE_CORRECTA Entonces
			Escribir "Clave correcta. Has accedido."
			acertado <- Verdadero
		Sino
			intentos <- intentos + 1
			Escribir "Clave incorrecta. Intentos restantes:", 3 - intentos
		FinSi
	FinMientras
	Si no acertado Entonces
		Escribir "Has agotado los 3 intentos."
	FinSi
FinAlgoritmo
