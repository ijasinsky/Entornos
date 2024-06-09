num = int(input("Introdueix un número per calcular el seu factorial: "))

if num < 0:
    print("No es pot calcular el factorial d'un número negatiu.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} és: {factorial}")