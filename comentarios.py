from BD import DB
from canciones import *
from usuarios import *

class Comentario(object):

    idComentario = None
    contenido = None
    Usuario = None
    cancion = None

    @staticmethod
    def getComentarioscanciones(id_canciones):
        listaComentarios = []

        cursor = DB().run("SELECT * FROM Comentario WHERE canciones_id_canciones = " + str(id_canciones) + ";")

        for item in cursor:
            unComentario = Comentario()
            unComentario.idComentario = item['idComentario']
            unComentario.contenido = item['contenido']

            for item2 in Cancion.getCanciones():
                if item2.idCancion == item['Canciones_id_canciones']:
                    unComentario.cancion = item2
            for item3 in Usuario.getUsuarios():
                if item3.idUsuario == item['Usuario_id_Usuario']:
                    unComentario.Usuario = item3

            listaComentarios.append(unComentario)

        return listaComentarios


    def altaComentarioCancion(self):
        c = DB().run("INSERT INTO Comentario(idComentario,contenido,Usuario_id_Usuario,Canciones_id_canciones) VALUES (NULL, '" + self.contenido + "', " + str(self.Usuario.idUsuario) + "," + str(self.cancion.idCancion) + ");")

