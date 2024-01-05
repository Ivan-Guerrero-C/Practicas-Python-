def regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        regresiva(numero)
    else:
        print("Numero fuera de Rango")
        
regresiva(0)