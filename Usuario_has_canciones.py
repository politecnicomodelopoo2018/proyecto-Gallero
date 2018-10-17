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

    @staticmethod
    def getUhc(id):
        listaUhc = []

        cursor = DB().run("SELECT * FROM CancionesGuardadas WHERE Usuario_id_Usuario = "+str(id)+";")

        for item in cursor:
            unaCancion = Uhc()
            unaCancion.Usuario = item['Usuario_id_Usuario']
            unaCancion.Cancion = item['Canciones_id_canciones']

            if unaCancion not in listaUhc:
                listaUhc.append(unaCancion)

        return listaUhc