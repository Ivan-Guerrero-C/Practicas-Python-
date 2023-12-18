estaciones = input("Que estacion del año desea saber (o)Otoño, (i)Invierno, (p)Primavera, (v)Verano: ")
if estaciones == "o":
    print("Se encuentra en Otoño: ")
    otono = int(input("Indique en que mes se encuentra (En valor numerico): "))
    if otono == 3:
        print("Estamos en comienzo de estacion")
    elif otono == 4:
        print("Estamos a mitad de la estacion")
    elif otono ==5:
        print("Estamos a final de estacion")
    else:
        print("Porfavor indique un numero correspondiente")
elif estaciones == "i":
    print("Se encuentra en invierno")
    invierno = int(input("Indique en que mes se encuentra (En valor numerico): "))
    if invierno == 6:
        print("Estamos en comienzo de estacion")
    elif invierno == 7:
        print("Estamos a final de la estacion")
    else:
        print("Porfavor indique un numero correspondiente")
elif estaciones == "p":
    print("Se encuentra en primavera")
    primavera = int(input("Indique en que mes se encuentra (En valor numerico): "))
    if primavera == 9:
        print("Estamos en comienzo de estacion")
    elif primavera == 10:
        print("Estamos a mitad de la estacion")
    elif primavera == 11:
        print("Estamos a final de estacion")
    else:
        print("Porfavor indique un numero correspondiente")
elif estaciones == "v":
    print("Estamos en verano")
    verano = int(input("Indique en que mes se encuentra (En valor numerico): "))
    if verano == 12:
        print("Estamos en comienzo de estacion")
    elif verano == 1:
        print("Estamos a mitad de la estacion")
    elif verano == 2:
        print("Estamos a final de estacion")
    else:
        print("Porfavor indique un numero correspondiente")
else:
    print("Porfavor Indique un valor correcto")