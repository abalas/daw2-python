from datetime import datetime

# --------------------------
# Clase Nota
# --------------------------
class Nota:
    def __init__(self, titulo, descripcion, color):
        self.titulo = titulo
        self.descripcion = descripcion
        colores_validos = ["amarillo", "verde", "blanco", "cyan"]
        if color.lower() in colores_validos:
            self.color = color.lower()
        else:
            self.color = "blanco"  # color por defecto si no es válido
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # fecha actual

    def __str__(self):
        # Representación bonita de la nota usando f-strings
        return (f"📝 Título: {self.titulo}\n"
                f"📄 Descripción: {self.descripcion}\n"
                f"🎨 Color: {self.color}\n"
                f"📅 Fecha de creación: {self.fecha}\n"
                f"{'-'*40}")

# --------------------------
# Clase GestorNotas
# --------------------------
class GestorNotas:
    def __init__(self):
        self.notas = []  # lista donde se almacenan todas las notas

    def crearNota(self, titulo, descripcion, color):
        nota = Nota(titulo, descripcion, color)
        self.notas.append(nota)
        print(f"✅ Nota '{titulo}' creada correctamente.\n")

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                self.notas.remove(nota)
                print(f"🗑️ Nota '{titulo}' eliminada.\n")
                return
        print(f"⚠️ No se encontró la nota con título '{titulo}'.\n")

    def listarNotas(self):
        if not self.notas:
            print("📭 No hay notas para mostrar.\n")
        else:
            print("📋 Listado de notas:\n")
            for nota in self.notas:
                print(nota)  # utiliza el __str__ de la clase Nota

# --------------------------
# Pruebas
# --------------------------
if __name__ == "__main__":
    # Creamos el gestor
    gestor = GestorNotas()

    # Creamos algunas notas
    gestor.crearNota("Comprar comida", "Leche, huevos, pan", "amarillo")
    gestor.crearNota("Estudiar Python", "Repasar clases de OOP", "verde")
    gestor.crearNota("Recordatorio", "Llamar al médico", "cyan")

    # Listamos todas las notas
    gestor.listarNotas()

    # Eliminamos una nota
    gestor.eliminarNota("Estudiar Python")

    # Listamos nuevamente
    gestor.listarNotas()
