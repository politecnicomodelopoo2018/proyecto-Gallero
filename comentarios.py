from BD import DB
from canciones import *
from usuario import *

class Comentario(object):

    idComentario = None
    descripcion = None
    Usuario = None
    cancion = None

    @staticmethod
    def getComentarioscanciones(id_canciones):
        listaComentarios = []

        cursor = DB().run("SELECT * FROM Comentario WHERE canciones_id_canciones = " + str(id_canciones) + ";")

        for item in cursor:
            unComentario = Comentario()
            unComentario.idComentario = item['idComentario']
            unComentario.descripcion = item['descripcion']

            for item2 in Pelicula.getPeliculas():
                if item2.idTitulo == item['Pelicula_idPelicula']:
                    unComentario.Pelicula = item2
            for item3 in Usuario.getUsuarios():
                if item3.idUsuario == item['Usuario_idUsuario']:
                    unComentario.Usuario = item3

            listaComentarios.append(unComentario)

        return listaComentarios


    def altaComentarioPelicula(self):
        c = DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '" + self.descripcion + "', " + str(self.Usuario.idUsuario) + "," + str(self.Pelicula.idTitulo) + ", NULL);")

        self.idComentario = c.lastrowid

    def altaComentarioCapitulo(self):
DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '" + self.descripcion + "', " + self.Usuario.idUsuario + ", NULL," + self.Capitulo.idCapitulo+");")