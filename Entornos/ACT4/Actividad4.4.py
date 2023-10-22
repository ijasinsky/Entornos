num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Comparar los números para encontrar el mayor
if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor de los tres números.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor de los tres números.")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es el mayor de los tres números.")
else:
    print("Los números son iguales o hay números repetidos.")