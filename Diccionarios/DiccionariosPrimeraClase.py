dict1={"nombre": "Jose Maria", "edad":57, "activo":True}
dict2= dict(color="azul", modelo="Caddy", submodelo="Outdooor", motor=2.0)
print(dict1)
print(dict2)
dict3={24: "Charcuteria Manolo", 26: "Medias Puri", 28: "Bar el Torrezno"}
print(dict3)

print(dict3[26])
print(dict2["modelo"])
print(dict2.get("motor", "Esa clave no existe"))

for elemento in dict3:
    print(elemento)

for elemento in dict3:
    print(elemento, dict3[elemento])

print(list(dict2.keys()))
print(list(dict2.values()))
print(list(dict2.items()))

dict3[30]="Peluquería Canina el galgo"
print(list(dict3.items()))
dict4={"activo":False, "dni": "28777666X", "telefono": 655443322}
dict1.update(dict4)
print(list(dict1.items()))

#dct1.clear()
print(dict1)
calor = dict1.pop("edad")
print(dict1)
valor = dict1.popitem()