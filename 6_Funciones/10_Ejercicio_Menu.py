clientes = []

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    dni = input("Ingrese el DNI del cliente: ")
    cliente = {"nombre": nombre, "apellido": apellido, "dni": dni}
    clientes.append(cliente)
    print("Cliente agregado correctamente.")

def mostrar_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido: {cliente['apellido']}")
        print(f"DNI: {cliente['dni']}")
        print("")

def menu():
    while True:
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()