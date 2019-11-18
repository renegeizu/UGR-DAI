#./flask/app.py

import time
import os
import random

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
	im.save("static/" + nombreFicheroPPM + ".png")

# Limpieza de Cache
def clean_cache(cache_dir, timespan):
    limit = time.time() - timespan
    for f in os.listdir(cache_dir): # Lista de Entradas de un Directorio
        file_path = os.path.join(cache_dir, f) #  Creo la Ruta del Archivo
        if os.path.getmtime(file_path) < limit: # Compruebo la Fecha de Modificacion
            os.remove(file_path) # Borro el Archivo
            print("Removing %s"%file_path)

def color():
	list = ['red', 'green', 'blue', 'yellow', 'orange', 'gray', 'black', 'white']
	return random.sample(list, 1)[0]

def rect():
    return 	"""
    			<rect x="{}", y="{}", height="{}", width="{}" fill="{}" />
    		""".format(random.uniform(0, 800), random.uniform(0, 600), random.uniform(0, 600), random.uniform(0, 800), color())

def circle():
    return 	"""
    			<circle r="{}", cx="{}", cy="{}", fill="{}" />
    		""".format(random.uniform(0, 120), random.uniform(0, 800), random.uniform(0, 600), color())

def generateSVG():
	list = [rect, circle]
	return 	"""
				<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
			""" + random.sample(list, 1)[0]() + """</svg>"""

#################
# Funciones Web #
#################

# Un Hola Mundo! en Flask
@app.route('/')
def hello_world():
	return	'''
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        				<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
						<link rel="icon" type="image/png" href="/static/icon.png">
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
					</head>
					<body>
						<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
							<a class="navbar-brand" href="#">Practica 02</a>
							<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
								<span class="navbar-toggler-icon"></span>
							</button>
							<div class="collapse navbar-collapse" id="navbarNav">
								<ul class="navbar-nav">
									<li class="nav-item active">
										<a class="nav-link" title="Un Hola Mundo! en Flask" href="#">Ejercicio 01<span class="sr-only">(current)</span></a>
									</li>
									<li class="nav-item">
										<a class="nav-link" title="Sirviendo Contenidos Estaticos" href="/static">Ejercicio 02</a>
									</li>
									<li class="nav-item">
										<a class="nav-link" title="Manejo de URLs" href="/url/Fairy_Tail">Ejercicio 03</a>
									</li>
									<li class="nav-item">
										<a class="nav-link" title="Creando Imagenes Dinamicas [Binarias]" href="/imgbin">Ejercicio 04</a>
									</li>
									<li class="nav-item">
										<a class="nav-link" title="Creando Imagenes Dinamicas [Vectoriales]" href="/imgvec">Ejercicio 04</a>
									</li>
									<li class="nav-item">
										<a class="nav-link" title="Ejemplo de Error" href="/stop">Error 404</a>
									</li>
								</ul>
							</div>
						</nav>
						<div class="container">
							<div class="abs-center">
								<br/>
								<h1 class="text-primary">Hello, World!</h1>
							</div>
						</div>
					</body>
				</html>
			'''

# Sirviendo contenidos estáticos (imágenes, hojas de estilo, etc)
@app.route('/static')
def content_static():
	return	'''
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link href="/static/style.css" rel="stylesheet" type="text/css" />
						<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        				<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
						<link rel="icon" type="image/png" href="/static/icon.png">
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
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
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link href="/static/style.css" rel="stylesheet" type="text/css" />
						<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        				<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
						<link rel="icon" type="image/png" href="/static/icon.png">
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
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
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link href="/static/error-style.css" rel="stylesheet" type="text/css" />
						<link rel="icon" type="image/png" href="/static/icon.png">
						<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
						<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
						<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
					</head>
					<body class="error-body">
						<div class="container">
    						<div class="row">
        						<div class="col-md-12">
            						<div class="error-template">
                						<h1>Oops!</h1>
                						<h2>404 Not Found</h2>
                						<div class="error-details">Sorry, an error has occured, Requested page not found!</div>
                						<div class="error-actions">%s</div>
            						</div>
        						</div>
    						</div>
						</div>
					</body>
				</html>
			''' % (error)

# Creando Imágenes Dinámicas [Binarias]
@app.route('/imgbin', methods=["GET"])
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
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link rel="icon" type="image/png" href="/static/icon.png">
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
					</head>
					<body><img src="/static/%s.png"/></body>
				</html>
			''' % arguments["nombre"]


# Creando Imágenes Dinámicas [Vectoriales]
@app.route('/imgvec')
def content_imgvec():
	img_svg = generateSVG()
	with open("image.svg", "w") as f:
		f.write(img_svg)
	return	'''
				<!DOCTYPE html>
				<html>
					<head>
						<title>Practica 02</title>
						<link rel="icon" type="image/png" href="/static/icon.png">
						<meta charset="UTF-8">
  						<meta name="description" content="Practica 02 - DAI">
  						<meta name="keywords" content="HTML, CSS, XML, JavaScript">
  						<meta name="author" content="Rafael Bailón Robles">
  						<meta name="viewport" content="width = device-width, initial-scale = 1.0">
					</head>
					<body>%s</body>
				</html>
			''' % img_svg

###############
# Main Method #
###############

if __name__ == '__main__':
	# Ayuda para depuracion | Mostrar Errores
	app.run(debug = True)
