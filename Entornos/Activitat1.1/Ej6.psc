Algoritmo Ej6
	Escribir "Introduce un n�mero:"
    Leer num
    Si num <= 0 Entonces
        Escribir "Error: El n�mero debe ser mayor que 0."
    Sino
        cuadrado <- num * num
        Escribir "El cuadrado de ", num, " es: ", cuadrado
        Escribir "La ra�z cuadrada de ", num, " es: ", raiz(num)
    FinSi
FinAlgoritmo
