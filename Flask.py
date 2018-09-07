from flask import Flask, render_template
app = Flask(__name__)

@app.route("/login")
def iniciar():
    return render_template("login.html")
@app.route("/registro")
def rergistro():
    return render_template("registro.html")
if __name__ == "__main__":
    app.run(debug=True)