diccionario = {
    "NBA": "National basketball Asociation",
    "FIFA": "Federacion Internacional de Futbol y Asociados",
    "MLB": "Major League Baseball"
}

print(diccionario.get("NBA"))
print(diccionario["NBA"])
diccionario["NBA"] = "BALONCESTO"
print(diccionario["NBA"])

for i in diccionario:
    print(diccionario[i])

for i in diccionario.values():
    print(i)
    
diccionario["FVF"] = "Federacion venezolana de futbol"
print(diccionario)