#./flask/app.py

from flask import Flask, render_template, request, session, url_for, redirect
from pickleshare import *

app = Flask(__name__)

####################
# Funciones Utiles #
####################

def setAndClean():
    session["first_url"] = ''
    session["second_url"] = ''
    session["third_url"] = ''
    session["first_name"] = ''
    session["second_name"] = ''
    session["third_name"] = ''

def setVisitPages(url, name):
    try:
        if(session["first_name"] == name):
            session["first_url"] = session["second_url"]
            session["first_name"] = session["second_name"]
            session["second_url"] = session["third_url"]
            session["second_name"] = session["third_name"]
            session["third_url"] = url
            session["third_name"] = name
        elif(session["second_name"] == name):
            session["second_url"] = session["third_url"]
            session["second_name"] = session["third_name"]
            session["third_url"] = url
            session["third_name"] = name
        elif(session["third_name"] != name):
            session["first_url"] = session["second_url"]
            session["first_name"] = session["second_name"]
            session["second_url"] = session["third_url"]
            session["second_name"] = session["third_name"]
            session["third_url"] = url
            session["third_name"] = name
    except:
        setAndClean()

#################
# Funciones Web #
#################

@app.route("/")
def index():
    setVisitPages("/", "Pagina Principal")
    return render_template("index.html")

@app.route("/user/login", methods=["POST"])
def login():
    session.clear()
    db = PickleShareDB('db_users')
    if(request.form["user"] in db.keys()):
        if(db[request.form["user"]] == request.form["pass"]):
            session["user"] = request.form["user"]
            session["pass"] = request.form["pass"]
            setAndClean()
    return redirect(url_for("index"))

@app.route("/user/logout", methods=["POST"])
def logout():
    session.clear()
    setAndClean()
    return redirect(url_for("index"))

@app.route("/user/registrar", methods=["POST"])
def registro():
    db = PickleShareDB('db_users')
    db[request.form["user"]] = request.form["pass"]
    session["user"] = request.form["user"]
    session["pass"] = request.form["pass"]
    return redirect(url_for("index"))

@app.route("/user/modificar", methods=["POST"])
def modificar():
    db = PickleShareDB('db_users')
    db[session["user"]] = request.form["pass"]
    session["pass"] = request.form["pass"]
    return redirect(url_for("index"))

@app.route("/registrar")
def registrar():
    try:
        if(session["user"] is None):
            return render_template("registrar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("registrar.html")

@app.route("/modificar")
def editar():
    try:
        if(session["user"] is not None):
            return render_template("modificar.html")
        else:
            return render_template("error.html")
    except:
        return render_template("error.html")

@app.route("/erza")
def erza():
    setVisitPages("/erza", "Erza")
    return render_template("erza.html")

@app.route("/gray")
def gray():
    setVisitPages("/gray", "Gray")
    return render_template("gray.html")

@app.route("/juvia")
def juvia():
    setVisitPages("/juvia", "Juvia")
    return render_template("juvia.html")

@app.route("/natsu")
def natsu():
    setVisitPages("/natsu", "Natsu")
    return render_template("natsu.html")

# Error 404
@app.errorhandler(404)
def error_404(error):
	return	render_template("error.html")

app.secret_key = 'Super Secret Key'

if __name__ == '__main__':
    # Ayuda para depuracion | Mostrar Errores
    app.run(debug = True)
