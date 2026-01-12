"""1. Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos
- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo pero podría ser de dos. Nunca mas
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos un método que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona."""

class Pokemon:
    TIPOS_VALIDOS = {
        "Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno",
        "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho",
        "Fantasma", "Dragón"
    }

    def __init__(self, codigo, nombre, tipos, evolucion=None):
        if not (1 <= codigo <= 151):
            raise ValueError("El código debe estar entre 1 y 151")

        if not (1 <= len(tipos) <= 2):
            raise ValueError("Un Pokemon debe tener uno o dos tipos")

        if not all(tipo in self.TIPOS_VALIDOS for tipo in tipos):
            raise ValueError("Tipo de Pokemon no válido")

        self._codigo = codigo
        self._nombre = nombre
        self._tipos = tuple(tipos)
        self._evolucion = evolucion

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_tipos(self):
        return self._tipos

    def get_evolucion(self):
        return self._evolucion

    def evolucionar(self):
        if self._evolucion is None:
            raise Exception(f"{self._nombre} no puede evolucionar")
        return self._evolucion

    def __str__(self):
        tipos = " / ".join(self._tipos)
        return f"{self._nombre} (#{self._codigo}) - {tipos}"

