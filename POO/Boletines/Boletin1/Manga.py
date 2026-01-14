"""Queremos implementar una clase para gestionar nuestra colección de mangas con las
siguientes características:
- Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
getters para todos ellos y setter para el título en castellano (por si originalmente no lo
sabemos y luego lo queremos añadir) y para el número por el que va la colección.
- Queremos, además, poder actualizar los números que tenemos y saber que números nos
faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
vamos comprando (permitiendo una entrada variable de argumentos para cuando
compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
la colección.
- Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
ellos repetido debería de advertirnos
- También necesitaremos un método que nos permita eliminar un número (lo hemos perdido,
etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos"""
class Manga:

    GENEROS_VALIDOS = { "shonen", "sojo", "seinen", "josei", "komodo", "yuri", "spokon", "isekai", "hentai"}

    def __init__(self, mangaka, tituloEnJapones, tituloEnEspaniol, ultimoNumero):
        self._mangaka = mangaka
        self._tituloEnJapones = tituloEnJapones
        self._tituloEnEspaniol = tituloEnEspaniol
        self._ultimoNumero = ultimoNumero

    def get_mangaka(self):
        return self._mangaka

    def get_tituloEnJapones(self):
        return self._tituloEnJapones

    def get_tituloEnEspaniol(self):
        return self._tituloEnEspaniol

    def get_ultimoNumero(self):
        return self._ultimoNumero

    #Unico setter
    def set_tituloEnEspaniol(self, tituloEnEspaniol):
        self._tituloEnEspaniol = tituloEnEspaniol

    def __str__(self):
        return (f"""------- {self._tituloEnJapones} -------
        Mangaka: {self._mangaka}
        Titulo en español: {self._tituloEnEspaniol}
        Ultimo numero de la colleccion = {self._ultimoNumero}
                """)


manga1 = Manga("Ito Natamura","Bokuno hero academy", "Academia heroe", 200)
print(manga1)
manga1.set_tituloEnEspaniol("caca")
print(manga1)
