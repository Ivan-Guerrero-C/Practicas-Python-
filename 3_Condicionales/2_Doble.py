x = False
if x == True:
    print("X es un valor verdadero")
elif x == False:
    print("X tiene un valor falso")
else: 
    print("No se reconoce la variable")
    
ancho = int(input("Ingrese ancho de la tabla:"))
altura = int(input("Ingrese la altura de la tabla"))
grosor = int(input("Ingrese grosor de la tabla"))
area = ancho * altura
volumen = area * grosor 
print("El area de la tabla es:", area)
print("El volumen es capaz de resistir", volumen)

if area >= 10 and volumen >= 10:
    print("La tablas es capaz de resistir el peso")
elif area <= 10 or volumen <= 10:
    print("La tabla no podra resistir el peso")
else:
    print("Los datos suministrados son incorrectos")