import math

num = float(input("Introdueix un número: "))

if num <= 0:
    print("Error: El número introduït és 0 o menor que 0.")
else:
    quadrat = num ** 2
    arrel_quadrada = math.sqrt(num)
    print(f"El quadrat del número és: {quadrat}")
    print(f"L'arrel quadrada del número és: {arrel_quadrada}")