from usuarios import Usuario
from BD import DB
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def iniciar():
    return render_template("login.html")

@app.route("/registro",  methods=['GET', 'POST'])
def rergistro():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("nombre")
        unUsuario.apellidoUsuario = request.form.get("apellidos")
        unUsuario.mail = request.form.get("mail")
        unUsuario.contrasenia = request.form.get("contrasenia")

        for item in Usuario().getUsuarios():
            if item.mail == unUsuario.mail or item.nombreUsuario == unUsuario.nombreUsuario:
                return render_template("registro.html")

        unUsuario.registrarse()

        return render_template("home.html")


    return render_template("registro.html")

DB().setconnection('localhost','root','alumno','mydb')


if __name__ == "__main__":
    app.run(debug=True)

