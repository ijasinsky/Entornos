num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

suma = num1 + num2
resta = num1 - num2
producte = num1 * num2
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "Indefinit (divisió per zero)"

print(f"La suma és: {suma}")
print(f"La resta és: {resta}")
print(f"El producte és: {producte}")
print(f"La divisió és: {divisio}")