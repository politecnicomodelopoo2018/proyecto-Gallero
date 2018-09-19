from BD import DB

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    mail = None

    def registrarse(self):
        DB().run("INSERT INTO Usuario(id_Usuario,nombreUsuario,apellidoUsuario,contrasenia,mail) VALUES (NULL,'" + self.nombreUsuario + "','" + self.apellidoUsuario + "','" +
                 self.contrasenia + "','" + self.mail + "');")

        for item in Usuario.getUsuarios():
            if item.mail == self.mail:
                self.idUsuario = item.idUsuario

    def cambiarContrasenia(self):
        DB().run("UPDATE usuario SET contrasenia = '" + self.contrasenia + "' WHERE id_Usuario = " + str(self.idUsuario) + ";")

    @staticmethod
    def getUsuarios ():
        listaUsuarios = []

        cursor = DB().run("SELECT * FROM Usuario")

        for item in cursor:
            unUsuario = Usuario()
            unUsuario.idUsuario = item['id_Usuario']
            unUsuario.nombreUsuario = item['nombreUsuario']
            unUsuario.apellidoUsuario = item['apellidoUsuario']
            unUsuario.contrasenia = item['contrasenia']
            unUsuario.mail = item['mail']

            listaUsuarios.append(unUsuario)

        return listaUsuarios

    @staticmethod
    def getUsuarioPorId(id):
        unUsuario = Usuario()

        cursor = DB().run("SELECT * FROM Usuario WHERE id_Usuario = " + str(id) + ";")

        dict = cursor.fetchone()

        unUsuario.idUsuario = dict['id_Usuario']
        unUsuario.nombreUsuario = dict['nombreUsuario']
        unUsuario.apellidoUsuario = dict['apellidoUsuario']
        unUsuario.contrasenia = dict['contrasenia']
        unUsuario.mail = dict['mail']

        return unUsuario

    @staticmethod
    def idUsuarioPorMail(mail):
        for item in Usuario.getUsuarios():
            if item.mail == mail:
                return item.idUsuario
        return
