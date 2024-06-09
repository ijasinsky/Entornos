num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

if num1 > num2:
    print(f"El número {num1} és major que el número {num2}.")
elif num1 < num2:
    print(f"El número {num2} és major que el número {num1}.")
else:
    print("Els dos números són iguals.")