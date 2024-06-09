clau_correcta = "eureka"
intents = 3

for i in range(intents):
    clau = input("Introdueix la clau: ")
    if clau == clau_correcta:
        print("Clau correcta! Has encertat.")
        break
    else:
        print("Clau incorrecta.")
else:
    print("Has esgotat els 3 intents.")