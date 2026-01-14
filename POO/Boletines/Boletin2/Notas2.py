from abc import ABC, abstractmethod
from datetime import datetime

# --------------------------
# Clase abstracta NotaBase
# --------------------------
class NotaBase(ABC):
    def __init__(self, titulo, descripcion, color=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.color = color if color else "blanco"

    @abstractmethod
    def __str__(self):
        pass  # cada subclase define cómo se muestra la nota

    @abstractmethod
    def confirmar_eliminacion(self):
        pass  # cada subclase decide si pide confirmación para borrar


# --------------------------
# Nota Normal
# --------------------------
class NotaNormal(NotaBase):
    def __init__(self, titulo, descripcion, color="blanco"):
        colores_validos = ["amarillo", "verde", "blanco", "cyan"]
        if color.lower() in colores_validos:
            super().__init__(titulo, descripcion, color.lower())
        else:
            super().__init__(titulo, descripcion, "blanco")

    def __str__(self):
        return (f"📝 Título: {self.titulo}\n"
                f"📄 Descripción: {self.descripcion}\n"
                f"🎨 Color: {self.color}\n"
                f"📅 Fecha de creación: {self.fecha}\n"
                f"{'-'*40}")

    def confirmar_eliminacion(self):
        # Las notas normales no piden confirmación
        return True


# --------------------------
# Nota Urgente
# --------------------------
class NotaUrgente(NotaBase):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, "rojo")  # siempre rojo

    def __str__(self):
        # Detalle que la distingue: ⚠️ y mayúsculas
        return (f"⚠️ URGENTE: {self.titulo.upper()} ⚠️\n"
                f"📄 {self.descripcion}\n"
                f"🎨 Color: {self.color}\n"
                f"📅 Fecha de creación: {self.fecha}\n"
                f"{'!'*40}")

    def confirmar_eliminacion(self):
        respuesta = input(f"¿Seguro que quieres eliminar la nota urgente '{self.titulo}'? (s/n): ")
        return respuesta.lower() == "s"


# --------------------------
# Gestor de notas
# --------------------------
class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNotaNormal(self, titulo, descripcion, color="blanco"):
        nota = NotaNormal(titulo, descripcion, color)
        self.notas.append(nota)
        print(f"✅ Nota normal '{titulo}' creada.\n")

    def crearNotaUrgente(self, titulo, descripcion):
        nota = NotaUrgente(titulo, descripcion)
        self.notas.append(nota)
        print(f"🚨 Nota urgente '{titulo}' creada.\n")

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                if nota.confirmar_eliminacion():
                    self.notas.remove(nota)
                    print(f"🗑️ Nota '{titulo}' eliminada.\n")
                else:
                    print(f"❌ Eliminación cancelada para '{titulo}'.\n")
                return
        print(f"⚠️ No se encontró la nota con título '{titulo}'.\n")

    def listarNotas(self):
        if not self.notas:
            print("📭 No hay notas para mostrar.\n")
        else:
            print("📋 Listado de notas (urgentes arriba):\n")
            # Primero las urgentes, luego las normales
            urgentes = [n for n in self.notas if isinstance(n, NotaUrgente)]
            normales = [n for n in self.notas if isinstance(n, NotaNormal)]
            for nota in urgentes + normales:
                print(nota)


# --------------------------
# Pruebas
# --------------------------
if __name__ == "__main__":
    gestor = GestorNotas()

    # Crear notas normales
    gestor.crearNotaNormal("Comprar comida", "Leche, huevos, pan", "amarillo")
    gestor.crearNotaNormal("Estudiar Python", "Repasar clases de OOP", "verde")

    # Crear nota urgente
    gestor.crearNotaUrgente("Pago de factura", "La factura vence hoy!")

    # Listar notas
    gestor.listarNotas()

    # Intentar eliminar nota urgente
    gestor.eliminarNota("Pago de factura")

    # Intentar eliminar nota normal
    gestor.eliminarNota("Comprar comida")

    # Listar nuevamente
    gestor.listarNotas()
