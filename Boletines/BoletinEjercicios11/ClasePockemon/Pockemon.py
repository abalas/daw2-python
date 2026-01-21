class Pokemon:
    TIPOS_VALIDOS = {
        "Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno",
        "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho",
        "Fantasma", "Dragón"
    }

    def __init__(self, codigo, nombre, tipos, evolucion=None):
        # Validar código
        if not (1 <= codigo <= 151):
            raise ValueError("El código debe estar entre 1 y 151")

        # Validar tipos
        if not isinstance(tipos, (list, tuple)) or len(tipos) not in (1, 2):
            raise ValueError("Un Pokémon debe tener uno o dos tipos")

        for t in tipos:
            if t not in Pokemon.TIPOS_VALIDOS:
                raise ValueError(f"Tipo inválido: {t}")

        self._codigo = codigo
        self._nombre = nombre
        self._tipos = tipos
        self._evolucion = evolucion  # Puede ser otro objeto Pokémon o None

    # Getters
    def get_codigo(self):
        return me._codigo

    def get_nombre(self):
        return self._nombre

    def get_tipos(self):
        return self._tipos

    def get_evolucion(self):
        return self._evolucion

    # Método para evolucionar
    def evolucionar(self):
        if self._evolucion is None:
            print(f"{self._nombre} no puede evolucionar.")
            return self
        else:
            print(f"{self._nombre} está evolucionando a {self._evolucion.get_nombre()}!")
            return self._evolucion


# ---------------------- EJEMPLO DE USO ----------------------

# Creamos cadena de evolución: Charmander -> Charmeleon -> Charizard

charizard = Pokemon(6, "Charizard", ["Fuego", "Volador"])
charmeleon = Pokemon(5, "Charmeleon", ["Fuego"], evolucion=charizard)
charmander = Pokemon(4, "Charmander", ["Fuego"], evolucion=charmeleon)

nuevo = charmander.evolucionar()
nuevo = nuevo.evolucionar()
nuevo = nuevo.evolucionar()  # Charizard ya no evoluciona
