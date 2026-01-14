from abc import ABC, abstractmethod

# --------------------------
# Clase abstracta Persona
# --------------------------
class Persona(ABC):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @abstractmethod
    def __str__(self):
        pass  # cada subclase define cómo mostrar la persona


# --------------------------
# Clase Alumno
# --------------------------
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo=None, grupo=None):
        super().__init__(nombre, apellido, edad)
        self.ciclo = ciclo  # referencia a un objeto Ciclo
        self.grupo = grupo  # referencia a un objeto Grupo
        self.mayor_edad = edad >= 18

    def __str__(self):
        ciclo_nombre = self.ciclo.nombre if self.ciclo else "No asignado"
        grupo_nombre = self.grupo.nombre if self.grupo else "No asignado"
        return (f"Alumno: {self.nombre} {self.apellido}, Edad: {self.edad}, "
                f"{'Mayor de edad' if self.mayor_edad else 'Menor de edad'}, "
                f"Ciclo: {ciclo_nombre}, Grupo: {grupo_nombre}")


# --------------------------
# Clase Profesor
# --------------------------
class Profesor(Persona):
    DEPARTAMENTOS = ["Informática", "Empresa", "Inglés"]

    def __init__(self, nombre, apellido, edad, tutor=None, departamento=None):
        super().__init__(nombre, apellido, edad)
        self.tutor = tutor  # referencia a un objeto Grupo
        if departamento in Profesor.DEPARTAMENTOS:
            self.departamento = departamento
        else:
            self.departamento = "No asignado"

    def __str__(self):
        tutor_nombre = self.tutor.nombre if self.tutor else "Ninguno"
        return (f"Profesor: {self.nombre} {self.apellido}, Departamento: {self.departamento}, "
                f"Tutor de: {tutor_nombre}")


# --------------------------
# Clase Módulo
# --------------------------
class Modulo:
    def __init__(self, nombre, primer_ano=True, horas_semana=0, optativo=False):
        self.nombre = nombre
        self.primer_ano = primer_ano
        self.horas_semana = horas_semana
        self.optativo = optativo

    def __str__(self):
        ano = "1º" if self.primer_ano else "2º"
        return (f"Módulo: {self.nombre}, Año: {ano}, Horas/semana: {self.horas_semana}, "
                f"{'Optativo' if self.optativo else 'Obligatorio'}")


# --------------------------
# Clase Ciclo
# --------------------------
class Ciclo:
    def __init__(self, nombre, grado_medio=True):
        self.nombre = nombre
        self.grado_medio = grado_medio
        self.modulos = []  # lista de objetos Módulo

    def agregar_modulo(self, modulo):
        self.modulos.append(modulo)

    def __str__(self):
        tipo = "Grado Medio" if self.grado_medio else "Grado Superior"
        modulos_str = "\n  ".join([str(m) for m in self.modulos])
        return f"Ciclo: {self.nombre}, {tipo}\n  Módulos:\n  {modulos_str}"


# --------------------------
# Clase Grupo
# --------------------------
class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor=None):
        self.nombre = nombre
        self.ciclo = ciclo  # referencia a un objeto Ciclo
        self.curso = curso  # 1 o 2
        self.tutor = tutor  # referencia a un objeto Profesor
        self.alumnos = []  # lista de objetos Alumno

    def agregar_alumno(self, alumno):
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
            alumno.grupo = self
            print(f"✅ Alumno {alumno.nombre} agregado al grupo {self.nombre}.")
        else:
            print(f"⚠️ El alumno {alumno.nombre} ya está en el grupo {self.nombre}.")

    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            alumno.grupo = None
            print(f"🗑️ Alumno {alumno.nombre} eliminado del grupo {self.nombre}.")
        else:
            print(f"⚠️ El alumno {alumno.nombre} no está en el grupo {self.nombre}.")

    def __str__(self):
        tutor_nombre = self.tutor.nombre if self.tutor else "Ninguno"
        alumnos_str = "\n  ".join([f"- {a.nombre} {a.apellido}" for a in self.alumnos])
        return (f"Grupo: {self.nombre}, Curso: {self.curso}º, Ciclo: {self.ciclo.nombre}, "
                f"Tutor: {tutor_nombre}, Nº Alumnos: {len(self.alumnos)}\n"
                f"Alumnos:\n  {alumnos_str if alumnos_str else 'No hay alumnos'}")


# --------------------------
# Pruebas de funcionamiento
# --------------------------
if __name__ == "__main__":
    # Crear ciclos
    ciclo_dam = Ciclo("DAM", grado_medio=False)
    ciclo_daw = Ciclo("DAW", grado_medio=False)

    # Crear módulos
    modulo_prog = Modulo("Programación", primer_ano=True, horas_semana=6)
    modulo_bd = Modulo("Bases de Datos", primer_ano=True, horas_semana=4)
    modulo_redes = Modulo("Redes", primer_ano=False, horas_semana=5, optativo=True)

    # Agregar módulos a ciclos
    ciclo_dam.agregar_modulo(modulo_prog)
    ciclo_dam.agregar_modulo(modulo_bd)
    ciclo_dam.agregar_modulo(modulo_redes)

    # Crear grupo
    grupo_dam1 = Grupo("DAM1", ciclo=ciclo_dam, curso=1)

    # Crear profesor tutor
    profesor1 = Profesor("Laura", "García", 40, tutor=grupo_dam1, departamento="Informática")

    # Crear alumnos
    alumno1 = Alumno("Juan", "Pérez", 17, ciclo=ciclo_dam, grupo=grupo_dam1)
    alumno2 = Alumno("María", "López", 19, ciclo=ciclo_dam)
    alumno3 = Alumno("Carlos", "Sánchez", 18, ciclo=ciclo_dam)

    # Agregar alumnos al grupo
    grupo_dam1.agregar_alumno(alumno1)
    grupo_dam1.agregar_alumno(alumno2)
    grupo_dam1.agregar_alumno(alumno3)

    # Listar grupo
    print("\n--- Información del Grupo ---")
    print(grupo_dam1)

    # Eliminar un alumno
    grupo_dam1.eliminar_alumno(alumno2)

    # Listar nuevamente
    print("\n--- Información actualizada del Grupo ---")
    print(grupo_dam1)

    # Listar ciclos
    print("\n--- Información del Ciclo ---")
    print(ciclo_dam)

    # Listar profesor
    print("\n--- Información del Profesor ---")
    print(profesor1)
