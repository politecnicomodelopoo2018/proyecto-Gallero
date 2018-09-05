from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("Prueba.html")

if __name__ == "__main__":
    app.run(debug=True)