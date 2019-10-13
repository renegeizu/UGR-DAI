#./flask/app.py

import time
from PIL import Image
from flask import Flask
from flask import request

app = Flask(__name__)

# Un Hola Mundo! en Flask
@app.route('/')
def hello_world():
	return 'Hello, World!'

# Sirviendo contenidos estáticos (imágenes, hojas de estilo, etc)
@app.route('/static')
def content_static():
	return	'''
					<html>
						<head>
							<title>Practica 02</title>
							<link href="/static/style.css" rel="stylesheet" type="text/css" />
						</head>
						<body>
							<header id="pageHeader"><center><h3>Gray Fullbuster</h3></center></header>
							<article id="mainArticle"><center><img src="/static/img.jpg"/></center></article>
							<nav id="mainNav">
								<strong>Fairy Tail</strong>
								<ul>
									<li>Natsu Dragneel</li>
									<li>Gray Fullbuster</li>
									<li>Lucy Heartfilia</li>
									<li>Erza Scarlet</li>
									<li>Wendy Marvell</li>
									<li>Gajeel Redfox</li>
								</ul>
							</nav>
						</body>
					</html>
				'''

# Manejo de URLs
@app.route('/url/<dato>/')
def content_url(dato):
	return	'''
					<html>
						<head>
							<title>Practica 02</title>
							<link href="/static/style.css" rel="stylesheet" type="text/css" />
						</head>
						<body>
							<header id="pageHeader"><center><h3>Gray Fullbuster</h3></center></header>
							<article id="mainArticle"><center><img src="/static/img.jpg"/></center></article>
							<nav id="mainNav">
								<strong>Fairy Tail</strong>
								<ul>
									<li>Natsu Dragneel</li>
									<li>Gray Fullbuster</li>
									<li>Lucy Heartfilia</li>
									<li>Erza Scarlet</li>
									<li>Wendy Marvell</li>
									<li>Gajeel Redfox</li>
								</ul>
							</nav>
							<footer id="pageFooter"><strong>Informacion Proporcionada:</strong> %s</footer>
						</body>
					</html>
				''' % (dato)

# Error 404
@app.errorhandler(404)
def error_404(error):
	return	'''
					<html>
						<head>
							<title>Practica 02</title>
						</head>
						<body>%s</body>
					</html>
				''' % (error)

# Creando Imágenes Dinámicas [binarias]
@app.route('/imgbin')
def content_imgbin():
	arguments = {
		"x1": -2.5,
		"x2": 1.0,
		"y1": 1.0,
		"y2": -1,
		"imgx": 400,
		"maxIt": 255,
		"nombre": "sin_titulo.ppm"
	}
	for arg in arguments.keys():
		if request.args.get(arg, ""):
			arguments[arg] = float(request.args.get(arg, ""))
	imgy = int(abs (arguments["y2"] - arguments["y1"]) * arguments["imgx"] / abs(arguments["x2"] - arguments["x1"]));
	im = Image.new('RGB', (arguments["imgx"], imgy), color = 'black')
	for y in range(imgy):
		zy = y * (arguments["y2"] - arguments["y1"]) / (imgy - 1)  + arguments["y1"]   
		for x in range(arguments["imgx"]):
			zx = x * (arguments["x2"] - arguments["x1"]) / (arguments["imgx"] - 1)  + arguments["x1"]
			z = zx + zy * 1j
			c = z
		for i in range(arguments["maxIt"]):
			if abs(z) > 2.0:
				break 
			z = z * z + c
		i = arguments["maxIt"] - i
		col = (i%10*25, i%16*16, i%8*32)  
		im.putpixel((x, y), col)
	im.save("/static/" + arguments["nombre"]);
	return	'''
					<img src="/static/%s"/>
				''' % arguments["nombre"]


# Creando Imágenes Dinámicas [Vectoriales]
@app.route('/imgvec')
def content_imgvec():
	return 'Bye, World!'

if __name__ == '__main__':
	# Ayuda para depuracion | Mostrar Errores
	app.run(debug = True)
