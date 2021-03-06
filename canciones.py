from BD import DB
from generos import Genero

class Cancion(object):
    idCancion = None
    nombreCancion = None
    letra = None
    Genero = None

    @staticmethod
    def getCanciones():
        listaCanciones = []

        cursor = DB().run("SELECT * FROM Canciones")

        for item in cursor:
            unaCancion = Cancion()
            unaCancion.idCancion = item['id_canciones']
            unaCancion.nombreCancion = item['nombreCanciones']
            unaCancion.letra = item['Letra']

            for item2 in Genero.getGeneros():
                if item2.idGenero == item['Genero_id_Genero']:
                    unaCancion.Genero = item2

            listaCanciones.append(unaCancion)

        return listaCanciones

    def subida_cancion(self):
        DB().run( "INSERT INTO Canciones(id_canciones,nombre,letra,Genero_id_Genero) VALUES (NULL,'" + self.nombreCancion + "','" + self.letra + "','" +
            self.Genero + "');")


    @staticmethod
    def getCancion(id):
        cursor = DB().run("SELECT * FROM Canciones where id_canciones=" + str(id) + ";")

        dict = cursor.fetchone()

        unaCancion = Cancion()

        unaCancion.idCancion = dict['id_canciones']
        unaCancion.nombreCancion = dict['nombreCanciones']
        unaCancion.letra = dict['Letra']

        for item2 in Genero.getGeneros():
            if item2.idGenero == dict['Genero_id_Genero']:
                unaCancion.Genero = item2

        return unaCancion

    def UpdateCancion(self, idcancion, letranueva):
        DB().run("UPDATE Canciones SET Letra = ('%s') WHERE id_canciones = ('%s')" % (letranueva, idcancion))
