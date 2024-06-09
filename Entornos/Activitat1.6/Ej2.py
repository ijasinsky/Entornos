valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

if valor1 > valor2:
    major = valor1
    menor = valor2
else:
    major = valor2
    menor = valor1

if menor != 0:
    divisio = major / menor
    print(f"La divisió del major pel menor és: {divisio}")
else:
    print("No es pot dividir per zero.")