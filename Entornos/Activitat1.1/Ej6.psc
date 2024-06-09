Algoritmo Ej6
	Escribir "Introduce un número:"
    Leer num
    Si num <= 0 Entonces
        Escribir "Error: El número debe ser mayor que 0."
    Sino
        cuadrado <- num * num
        Escribir "El cuadrado de ", num, " es: ", cuadrado
        Escribir "La raíz cuadrada de ", num, " es: ", raiz(num)
    FinSi
FinAlgoritmo
