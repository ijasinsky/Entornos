dia = float(input("Escriba el dia: "))
mes = float(input("Escriba el mes: "))

if (dia >= 1 and dia <= 31 and mes >=1 and mes <=12):
    print (f"Hoy es: {dia} / {mes}")
else:
    print ("Fecha invalida")

