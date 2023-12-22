lista = [1,2,3,4,5,1,6,7,9,4,5,1,8,4,1,5]

repetidos = []

for x in lista:
    if lista.count(x) == 1:
        repetidos.append(x)
        
print(repetidos)