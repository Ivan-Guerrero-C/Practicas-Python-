colorBase = input("Seleccione color base: ROjo(r), Azul(a):")
if colorBase == "r":
    colorSecundario = input("Seleccione un color Secundario: Verde(v), Amarillo(am):")
    if colorSecundario == "v":
        print("La mezcla del color rojo y verde es Amarillo")
    else:
        print("La mezcla del color rojo y amarillo es anaranjado")
elif colorBase == "a":
    colorSecundario = input("Seleccione un color secundario: Amarillo(am), Rojo(r):")
    if colorSecundario == "am":
        print("La Mezcla de azul y amarilllo es verde")
    else:
        print("La mezcla de azul y rojo es morado")
else:
    print("EL color no se encuentra asignado, intente de nuevo ¡")
