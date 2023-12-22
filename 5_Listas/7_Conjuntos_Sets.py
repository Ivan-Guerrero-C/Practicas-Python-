paises = {"Venezuela", "Colombia", "Ecuador", "Peru"}
print(paises)
lista = [1, 2, 3]
print(lista)

print(len(paises))
paises.add("Argentina")
print(paises)
paises.remove("Colombia")
print(paises)

a = {1, 2}
b = {3, 4}

c = a|b
print(c)

S = [{0, 1}, {2, 5, 9}, {1, 3, 4, 5}, {5, 6, 7, 8}]
Sn = set()
for s in S:
    Sn = Sn|s
print(Sn)

d = {4, 7}
e = {6, 8, 7}
x = d&e
print(x)

T = [{0, 1, 5}, {1, 2, 5, 9}, {1, 2, 3, 4, 5}, {2, 5, 6, 7, 8}]
Sn = T[0]
for s in T:
    Sn = Sn&s
print(Sn)

r = d - e
print(r)
r = e - d
print(r)