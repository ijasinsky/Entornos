dia = int(input("Introdueix el dia: "))
mes = int(input("Introdueix el mes: "))

data_valida = True

if mes < 1 or mes > 12:
    data_valida = False
elif dia < 1 or dia > 31:
    data_valida = False
elif mes in [4, 6, 9, 11] and dia > 30:
    data_valida = False
elif mes == 2:
    if dia > 29:
        data_valida = False
if data_valida:
    print("La data és correcta.")
else:
    print("La data és incorrecta.")