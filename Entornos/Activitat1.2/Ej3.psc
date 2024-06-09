Algoritmo Ej3
	Escribir "Introduce el día:"
	Leer dia
	Escribir "Introduce el mes:"
	Leer mes
	esValido <- Falso
	Si mes >= 1 y mes <= 12 Entonces
		Si (mes = 1 o mes = 3 o mes = 5 o mes = 7 o mes = 8 o mes = 10 o mes = 12) y (dia >= 1 y dia <= 31) Entonces
			esValido <- Verdadero
		FinSi
		Si (mes = 4 o mes = 6 o mes = 9 o mes = 11) y (dia >= 1 y dia <= 30) Entonces
			esValido <- Verdadero
		FinSi
		Si mes = 2 y (dia >= 1 y dia <= 28) Entonces
			esValido <- Verdadero
		FinSi
	FinSi
	Si esValido Entonces
		Escribir "La fecha es correcta."
	Sino
		Escribir "La fecha es incorrecta."
	FinSi
FinAlgoritmo
