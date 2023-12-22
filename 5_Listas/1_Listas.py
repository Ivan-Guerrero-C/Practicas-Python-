lista = [2, 2.5, 'hola', 3.8, 5]
for i in lista:
    print(i)

print(lista[1])
print(lista[:3])
lista.append(8)
print(lista)

lista.extend([2, 4])
print(lista)

lista.append([2, 4])
print(lista)

lista.remove('hola')
print(lista)

a = lista.index(8)
print(a)

b = lista.count(2)
print(b)

lista.reverse()
print(lista)