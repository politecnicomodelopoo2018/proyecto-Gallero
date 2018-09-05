from BD import DB

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    mail = None

    def registrarse(self):
        DB().run("INSERT INTO usuario(idusuario,nombre,apellido,contraseña,mail)" +
                 "VALUES (" + str(self.idUsuario) + ",'" + self.nombreUsuario + "','" + self.apellidoUsuario + "','" +
                 self.contrasenia + "','" + self.mail + "');")

    def cambiarContrasenia(self):
        DB().run("UPDATE Usuario SET contraseña = '" + self.contrasenia + "' WHERE idusuario = " + str(self.idUsuario) + ";")

    @staticmethod
    def getUsuarios ():
        listaUsuarios = []

        cursor = DB().run("SELECT * FROM Usuario")

        for item in cursor:
            unUsuario = Usuario()
            unUsuario.idUsuario = item['idusuario']
            unUsuario.nombreUsuario = item['nombre']
            unUsuario.apellidoUsuario = item['apellido']
            unUsuario.contrasenia = item['contraseña']
            unUsuario.mail = item['mail']

            listaUsuarios.append(unUsuario)

        return listaUsuarios
