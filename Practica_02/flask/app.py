#./flask/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
	# Ayuda para depuracion | Mostrar Errores
	app.run(debug = True)
