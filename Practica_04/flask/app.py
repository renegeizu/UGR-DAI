#./flask/app.py

from pymongo import MongoClient

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo

@app.route('/mongo')
def mongo():
    val = db.samples_friends.find()  # Encontramos los documentos de la coleccion "samples_friends"

    return val[0]['name']
