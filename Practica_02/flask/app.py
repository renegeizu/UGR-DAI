#./flask/app.py

import time
from PIL import Image
from flask import Flask
from flask import request

app = Flask(__name__)

####################
# Funciones Utiles #
####################

def pintaMandelbrot(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPPM):
	xa = x1
	xb = x2
	ya = y1
	yb = y2
	maxIt = iteraciones
	imgx = ancho
	imgy = int(abs (y2 - y1) * ancho / abs(x2 - x1))
	im = Image.new('RGB', (imgx, imgy), color = 'black')
	for y in range(imgy):
		zy = y * (yb - ya) / (imgy - 1)  + ya    
		for x in range(imgx):
			zx = x * (xb - xa) / (imgx - 1)  + xa
			z = zx + zy * 1j
			c = z
			for i in range(maxIt):
				if abs(z) > 2.0:
					break 
			z = z * z + c
			i = maxIt - i
			col = (i%10*25, i%16*16, i%8*32)  
			im.putpixel((x, y), col)
	im.save("static/" + nombreFicheroPPM + ".png");

#################
# Funciones Web #
#################

# Un Hola Mundo! en Flask
@app.route('/')
def hello_world():
	return	'''
					<html>
						<head>
							<title>Practica 02</title>
						</head>
						<body>
							<h1>Hello, World!</h1>
							<ul>
								<li><a href="#">Ejercicio 01 (Un Hola Mundo! en Flask)</a></li>
								<li><a href="/static">Ejercicio 02 (Sirviendo Contenidos Estaticos)</a></li>
								<li><a href="/url/Fairy_Tail">Ejercicio 03 (Manejo de URLs)</a></li>
								<li><a href="/imgbin">Ejercicio 04 (Creando Imagenes Dinamicas [Binarias])</a></li>
								<li><a href="/imgvec">Ejercicio 04 (Creando Imagenes Dinamicas [Vectoriales])</a></li>
								<li><a href="/stop">Error 404</a></li>
							</ul>
						</body>
					</html>
				'''

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

# Creando Imágenes Dinámicas [Binarias]
@app.route('/imgbin')
def content_imgbin():
	arguments = {
		"x1": -2.0,
		"x2": 1.0,
		"y1": -1.5,
		"y2": 1.5,
		"imgx": 400,
		"maxIt": 255,
		"nombre": "mandelbrot"
	}
	for arg in arguments.keys():
		if request.args.get(arg, ""):
			arguments[arg] = float(request.args.get(arg, ""))
	pintaMandelbrot(arguments["x1"], arguments["y1"], arguments["x2"], arguments["y2"], arguments["imgx"], arguments["maxIt"], arguments["nombre"])
	return	'''
					<html>
						<head>
							<title>Practica 02</title>
						</head>
						<body><img src="/static/%s.png"/></body>
					</html>
				''' % arguments["nombre"]


# Creando Imágenes Dinámicas [Vectoriales]
@app.route('/imgvec')
def content_imgvec():
	return 'Bye, World!'

###############
# Main Method #
###############

if __name__ == '__main__':
	# Ayuda para depuracion | Mostrar Errores
	app.run(debug = True)
