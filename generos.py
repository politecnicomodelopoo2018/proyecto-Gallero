from usuarios import Usuario
from BD import DB

class Genero(object):
    idGenero = None
    nombreGenero = None

    @staticmethod
    def getGeneros():
        listaGeneros = []

        cursor = DB().run("SELECT * FROM Genero")

        for item in cursor:
            unGenero = Genero()
            unGenero.idGenero = item['id_Genero']
            unGenero.nombreGenero = item['nombreGenero']

            listaGeneros.append(unGenero)

        return listaGeneros