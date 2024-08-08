
from flask import Flask, render_template

app = Flask(__name__)
#endpoint o ruta
@app.route("/inicio")
def inicio():
    return "Hola mundo desde el backend"

@app.route("/contacto")
def contacto():
    return "Introduciendo HTML desde el Servidor"

@app.route("/contacto2")
def contacto2():
    return render_template("contacto.html")

# se pregunta por el proceso principal
if __name__=="__main__":
    app.run(debug=True)