""" 
Crear un cajero automatico con python, que en principio tendra 1000$ de saldo
saldo en la cuenta ficticia, además deberá contener el siguiente menu:

1.- Ingresar dinero en cuenta.
2.- Retirar dinero de la cuenta.
3.- Mostrar dinero disponible.
4.- Salir

Las condiciones para este ejercicio, son la solicitud de datos al usuario,
actualizar el monto de la cuenta de acuerdo con la operacion a realizar.
"""

saldo = 1000

while True:
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar dinero")
    print("4. Salir")
    entrada = input("Por favor Ingrese lo que desea hacer: ")
    
    if entrada == "1":
        monto = float(input("Ingrese el monto que va depositar:"))
        saldo += monto
        print("Dinero depositado exitosa")
    elif entrada == "2":
        monto = float(input("Porfavor ingrese el monto que desea retirar:"))
        saldo -= monto
        print("Dinero retirado exitosamente")
    elif entrada == "3":
        print(f"Su dinero es {saldo}$")
    elif entrada == "4":
        print("Gracias por utilizar nuestro cajero")
        break
    else:
        print("Porfavor ingrese el valor correcto")