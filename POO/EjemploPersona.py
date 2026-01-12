class Persona:
    def __init__(self, nombre: str, edad: int):
        # Atributos (convención: _ para "privados")
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self) -> str:
        return self._nombre

    # Getter para edad
    def get_edad(self) -> int:
        return self._edad

    # Método de ejemplo
    def presentarse(self) -> str:
        return f"Hola, me llamo {self._nombre} y tengo {self._edad} años"

if __name__ == "__main__":
    persona1 = Persona("Ana", 25)

    print(persona1.get_nombre())
    print(persona1.get_edad())
    print(persona1.presentarse())
