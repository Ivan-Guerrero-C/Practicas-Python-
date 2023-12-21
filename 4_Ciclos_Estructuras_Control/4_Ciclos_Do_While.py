a = False
while not a:
    b = input("Introduzca un color Primario: ")
    a = b.lower() in ["amarillo", "azul", "rojo"]
    if not a:
        print("'{0}' no es un color primario".format(b))
print("'{0}' es un color primario".format(b))