class GestorTareas:
    def __init__(self):
        self.tareas = {}

    def agregarTarea(self, identificador, titulo, prioridad):
        if identificador in self.tareas:
            print(f"Error: ID {identificador} ya existente")
            return

        self.tareas[identificador] = {
            "titulo": titulo,
            "prioridad": prioridad,
            "completada": False
        }

        print(f"Tarea '{titulo}' (ID: {identificador}) añadida.")

    def eliminarTarea(self, identificador):
        if identificador not in self.tareas:
            print(f"Error: No se encontró una tarea con ID {identificador}.")
            return

        titulo = self.tareas[identificador]["titulo"]
        del self.tareas[identificador]
        print(f"Tarea con ID {identificador} ('{titulo}') eliminada.")

    def marcarComoCompletada(self, identificador):
        if identificador not in self.tareas:
            print(f"Error: No se encontró una tarea con ID {identificador}.")
            return

        self.tareas[identificador]["completada"] = True
        titulo = self.tareas[identificador]["titulo"]
        print(f"Tarea ID {identificador} '{titulo}' marcada como completada.")

    def mostrarTareasCompletadas(self):
        print("LISTADO DE TAREAS:")
        hay = False

        for id_tarea, datos in self.tareas.items():
            if datos["completada"]:
                print(f"[{id_tarea}] {datos['titulo']} (Prioridad: {datos['prioridad']})")
                hay = True

        if not hay:
            print("No hay tareas completadas.")

    def mostrarTareasNoCompletadas(self):
        print("LISTADO DE TAREAS:")
        hay = False

        for id_tarea, datos in self.tareas.items():
            if not datos["completada"]:
                print(f"[{id_tarea}] {datos['titulo']} (Prioridad: {datos['prioridad']})")
                hay = True

        if not hay:
            print("No hay tareas no completadas.")


gestor = GestorTareas()

gestor.agregarTarea("P10", "Comprar billetes", 5)
gestor.agregarTarea("D055", "Completar retos de Duolingo", 2)

gestor.marcarComoCompletada("D055")
gestor.mostrarTareasCompletadas()
gestor.mostrarTareasNoCompletadas()
