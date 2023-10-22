num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 < 0:
    resultado = num1 * num2 * num3
else:
    resultado = num1 + num2 + num3

print(f"El resultado es: {resultado}")