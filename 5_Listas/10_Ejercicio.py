lista1 = [{2,5,89.3,"hola"},{96,1.2,6,"adios"},{"hora",7,9,96,1.3},{"adios",2,1.2}]
lista2 = [{1.2,"Venezuela",2},{"hola",96,8},{42,6.9,96,3,"hora"},{12,89.3,8,45,"te"}]

#Primera lista

lis1 = []
lis2 = []

for i in lista1:
    for x in i:
        lis1.append(x)
        """ print(lis1) """
        
for i in lista2:
    for x in i:
        lis2.append(x)
        """ print(lis2) """
        
nuevo1 = lis1+lis2
print(nuevo1)

num1 = set(lis1)
num2 = set(lis2)
num3 = num1|num2
num4 = num1&num2
print(num3)
print(num4)