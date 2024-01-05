tasaDiabs1 = 10
tasaDiadls2 =20

def bsxDls():
    bolivares=float(input("Ingrese el valor que desea convertir a dolares: "))
    conver1 = bolivares * tasaDiabs1
    print("Su total en dolares es: ", conver1)

def dlsxBs():
    dolares = float(input("Ingrese el valor que desea convertir a bolivares: "))
    conver2 = dolares * tasaDiadls2
    print("Su total en bolivares es: ", conver2)
    
def menu():
    while True:
        print("!Bienvenido al sistema cambiario¡")
        print("Que operacion desea realizar: ")
        print("1. Cambiar Bolivares a Dolares")
        print("2. Cambiar dolares a bolivares")
        print("3. Salir")
        convertidor =input("Seleccion la opcion que desea")
        
        if convertidor == 1:
            bsxDls()
        elif convertidor == 2:
            dlsxBs()
        elif convertidor == 3:
            print("Gracias por su tiempo.") 
        else:
            print("Seleccione una opcion correcta")
        
menu()