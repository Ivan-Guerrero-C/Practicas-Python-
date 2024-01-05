""" def argumentos_indeterminados(*args): #Para que reconozca toods los parametros enviados
    for arg in args:
        print(arg)
        
argumentos_indeterminados(1, "cubiwelt", [2, 4, 5, 6, 8, 10], 4.5) """

def nombre_indeterminados(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

nombre_indeterminados(n=5, c="Hola", l=[1,2,3,4,5])