num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
num3 = float(input("Introdueix el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"El número {num1} és el major.")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} és el major.")
else:
    print(f"El número {num3} és el major.")