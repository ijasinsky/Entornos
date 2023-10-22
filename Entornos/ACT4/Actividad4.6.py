import math

numero = float(input("Por favor, ingresa un número: "))

if numero <= 0:
    print("Error: El número debe ser mayor que 0")
else:
    cuadrado = numero**2
    raiz_cuadrada = math.sqrt(numero)
    
    print(f"El cuadrado de {numero} es: {cuadrado}")
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")