num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
num3 = float(input("Introdueix el tercer número: "))

if num1 < 0:
    producte = num1 * num2 * num3
    print(f"El producte dels tres números és: {producte}")
else:
    suma = num1 + num2 + num3
    print(f"La suma dels tres números és: {suma}")