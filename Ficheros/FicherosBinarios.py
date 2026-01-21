import pickle

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# 1. Preparar los datos
gente = [Persona("Jose María"), Persona("Roberto")]

# 2. GUARDAR (Write Binary)
with open("datos.bin", "wb") as f:
    pickle.dump(gente, f)
    print("Objetos guardados correctamente.")

# 3. LEER (Read Binary)
try:
    with open("datos.bin", "rb") as f:
        leidos = pickle.load(f)
        for p in leidos:
            print(f"Persona recuperada: {p.nombre}")
except FileNotFoundError:
    print("El archivo no existe.")


# 1. Creamos los objetos y los guardamos en una lista
lista_personas = [Persona("Jose María"), Persona("Roberto"), Persona("Ana")]

# 2. GUARDAR: Guardamos la lista completa de una sola vez
with open("agenda.bin", "wb") as f:
    pickle.dump(lista_personas, f)

# 3. LEER: Recuperamos la lista completa de una sola vez
with open("agenda.bin", "rb") as f:
    datos_recuperados = pickle.load(f) # Aquí 'datos_recuperados' ya es la lista

# Mostramos el contenido
for p in datos_recuperados:
    print(f"Nombre: {p.nombre}")