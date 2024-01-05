""" def multiplicacion(numero):
    numero *= 2
    print(numero)
    
n = 10
multiplicacion(n) """

a = [10, 50, 100]
def multiplicacion(numeros):
    for i in range(0, len(numeros)):
        numeros[i] *= 2
    return numeros

b = multiplicacion(a)
print(b)