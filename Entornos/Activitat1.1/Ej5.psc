Algoritmo Ej5
	Escribir "Introduce el primer número:"
    Leer num1
    Escribir "Introduce el segundo número:"
    Leer num2
    Escribir "Introduce el tercer número:"
    Leer num3
    Si num1 < 0 Entonces
        resultado <- num1 * num2 * num3
        Escribir "El resultado del producto es:", resultado
    Sino
        resultado <- num1 + num2 + num3
        Escribir "El resultado de la suma es:", resultado
    FinSi
FinAlgoritmo
