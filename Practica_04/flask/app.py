#./flask/app.py

from flask import Flask, render_template, request, session, url_for, redirect
from pickleshare import *
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo

####################
# Funciones Utiles #
####################



#################
# Funciones Web #
#################

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/mongo')
def mongo():
    val = db.samples_pokemon.find({"id" : 4})
    return val[0]["name"]

@app.route("/db/buscar", methods=['GET'])
def db_buscar():
    try:
        pkmn = db.samples_pokemon.find({"id" : int(request.args.get("id"))})
        return render_template('index.html', name=pkmn[0]["name"], img=pkmn[0]["img"])
    except:
        return render_template('error.html')

@app.route("/db/editar", methods=['GET'])
def db_editar():
    try:
        db.samples_pokemon.update({"id" : int(request.args.get("id"))}, {"$set" : {"name" : str(request.args.get("name"))}})
        return redirect(url_for("index"))
    except:
        return render_template('error.html')

@app.route("/db/borrar", methods=['GET'])
def db_borrar():
    try:
        db.samples_pokemon.remove({"id" : int(request.args.get("id"))})
        return redirect(url_for("index"))
    except:
        return render_template('error.html')

@app.route("/user/login", methods=["POST"])
def user_login():
    session.clear()
    db = PickleShareDB('db_users')
    if(request.form["user"] in db.keys()):
        if(db[request.form["user"]] == request.form["pass"]):
            session["user"] = request.form["user"]
            session["pass"] = request.form["pass"]
    return redirect(url_for("index"))

@app.route("/user/logout", methods=["POST"])
def user_logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/user/registrar", methods=["POST"])
def user_registrar():
    db = PickleShareDB('db_users')
    db[request.form["user"]] = request.form["pass"]
    session["user"] = request.form["user"]
    session["pass"] = request.form["pass"]
    return redirect(url_for("index"))

@app.route("/user/modificar", methods=["POST"])
def user_modificar():
    db = PickleShareDB('db_users')
    db[session["user"]] = request.form["pass"]
    session["pass"] = request.form["pass"]
    return redirect(url_for("index"))

@app.route("/registrar")
def registrar_user():
    try:
        if(session["user"] is None):
            return render_template("registrar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("registrar.html")

@app.route("/modificar")
def modificar_user():
    try:
        if(session["user"] is not None):
            return render_template("modificar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("error.html")

@app.route("/editar")
def editar_pkmn():
    try:
        if(session["user"] is not None):
            return render_template("editar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("editar.html")

@app.route("/borrar")
def borrar_pkmn():
    try:
        if(session["user"] is not None):
            return render_template("borrar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("borrar.html")

# Error 404
@app.errorhandler(404)
def error_404(error):
	return	render_template("error.html")

app.secret_key = 'Super Secret Key'

if __name__ == '__main__':
    # Ayuda para depuracion | Mostrar Errores
    app.run(debug = True)
