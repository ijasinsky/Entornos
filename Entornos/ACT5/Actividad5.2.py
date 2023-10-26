val1 = float(input("Escriba el primer valor: "))
val2 = float(input("Escriba el secundo valor: "))

if val1 >= val2:
    res1 = val1 / val2
    print(f"El resultado es: {res1}")

elif val1 < val2:
    res2 = val2 / val1
    print(f"El resultado es: {res2}")