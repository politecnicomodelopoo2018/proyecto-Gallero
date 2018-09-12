from BD import DB

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    mail = None

    def registrarse(self):
        DB().run("INSERT INTO usuario(idusuario,nombre,apellido,contrasenia,mail)" +
                 "VALUES (" + str(self.idUsuario) + ",'" + self.nombreUsuario + "','" + self.apellidoUsuario + "','" +
                 self.contrasenia + "','" + self.mail + "');")

    def cambiarContrasenia(self):
        DB().run("UPDATE usuario SET contrasenia = '" + self.contrasenia + "' WHERE idusuario = " + str(self.idUsuario) + ";")

    @staticmethod
    def getUsuarios ():
        listaUsuarios = []

        cursor = DB().run("SELECT * FROM usuario")

        for item in cursor:
            unUsuario = Usuario()
            unUsuario.idUsuario = item['idusuario']
            unUsuario.nombreUsuario = item['nombre']
            unUsuario.apellidoUsuario = item['apellido']
            unUsuario.contrasenia = item['contrasenia']
            unUsuario.mail = item['mail']

            listaUsuarios.append(unUsuario)

        return listaUsuarios
