from usuarios import Usuario
from BD import DB
from flask import *
from canciones import Cancion
from comentarios import Comentario
from Usuario_has_canciones import Uhc
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index ():
    return redirect("/home")

@app.route("/home")
def home():
    if 'userid' in session:
        redirect("/logeado")
    return render_template("home.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        for item in Usuario.getUsuarios():
            if item.mail == request.form.get('Inputmail') and item.contrasenia == request.form.get('Inputpassword'):
                session['userid'] = Usuario.idUsuarioPorMail(request.form.get('Inputmail'))
                return redirect("/logeado")

    return render_template("login.html")

@app.route("/logeado", methods=['GET','POST'])
def logeado():
    if 'userid' not in session:
        return redirect("/login")
    return render_template("logeado.html", Usuario=Usuario.getUsuarioPorId(session['userid']), Canciones=Cancion.getCanciones(), misCanciones=Uhc.getUhc(session['userid']))


@app.route("/registro",  methods=['GET', 'POST'])
def rergistro():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("Inputnombre")
        unUsuario.apellidoUsuario = request.form.get("Inputapellido")
        unUsuario.mail = request.form.get("Inputmail")
        unUsuario.contrasenia = request.form.get("Inputcontrasenia")

        for item in Usuario.getUsuarios():
            if item.mail == unUsuario.mail or item.nombreUsuario == unUsuario.nombreUsuario:
                return render_template("registro.html")

        unUsuario.registrarse()

        return render_template("home.html")
    return render_template("registro.html")

@app.route("/subir_cancion",  methods=['GET', 'POST'])
def subida_cancion():
    if request.method == 'POST':
        unaCancion = Cancion()
        unaCancion.nombreCancion = request.form.get("nueva cancion")
        unaCancion.letra = request.form.get("pepe")
        unaCancion.Genero = request.form.get("genero")

        unaCancion.subida_cancion()

    return render_template("subir_cancion.html")



@app.route("/ver_letra")
def ver_letra():
    if 'userid' not in session:
        return redirect("/login")

    miCancion = Cancion.getCancion(int(request.args.get("id")))

    return render_template('ver_letra.html', cancion=miCancion, usuario=session['userid'], comentarios=Comentario.getComentarioscanciones(miCancion.idCancion))

@app.route("/logueo_editar_letra")
def logueo_editar_letra():
    if 'userid' not in session:
        return redirect("/login")

    idcancion = request.args.get("idCancion")
    cancion = Cancion()
    cancion.getCancion(idcancion)

    return render_template("logueo_editar_letra.html", cancion=cancion)

@app.route("/ComentarioCancion",methods=['GET','POST'])
def agregarComentarioCancion():

    miCancion = Cancion.getCancion(int(request.form.get("id")))

    if request.method == 'POST':
        unComentario = Comentario()

        unComentario.cancion = miCancion
        unComentario.contenido = request.form.get("inputComment")

        for item in Usuario.getUsuarios():
            if item.idUsuario == session['userid']:
                unComentario.Usuario = item

        unComentario.altaComentarioCancion()

    return redirect("/ver_letra?id="+str(miCancion.idCancion))

@app.route("/logout")
def logout():
    session.pop('userid', None)
    return redirect('/home')

@app.route("/GuardarUhc",methods=['GET','POST'])
def GuardarUhc():
    UnUsuario = request.args.get("Usuario")
    UnaCancion = request.args.get("Cancion")
    UnUhc = Uhc()
    UnUhc.AgregarUhc(UnUsuario, UnaCancion)
    return redirect("/logeado")

DB().setconnection('localhost','root','alumno','mydb')


if __name__ == "__main__":
    app.run(debug=True)

# ALTA, BAJA Y MODIFICACION DE CANCIONES SOLO LOS ADMINISTRADORES VAN A PODER DE ALTA CANCIONES
# FAVORITOS listo
# COMENTARIOS listo
# LOGIN USANDO SESSION  listo




