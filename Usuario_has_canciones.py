from BD import DB

class Uhc (object):

    Usuario = None
    Cancion = None

    def SetUsuario(self, Usuario):
        self.Usuario = Usuario

    def SetCancion(self, Cancion):
        self.Cancion = Cancion

    def Insert(self):
        DB().run("INSERT INTO CancionesGuardadas (idCancionesGuardadas,Usuario_id_Usuario, Canciones_id_canciones) VALUES (NULL," + str(self.Usuario) + ","+ str(self.Cancion)+ ");")

    def AgregarUhc(self, Usuario, Cancion):
        self.SetUsuario(Usuario)
        self.SetCancion(Cancion)
        self.Insert()