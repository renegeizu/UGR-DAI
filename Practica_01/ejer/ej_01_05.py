import random

cadena = ""
tamanio = random.randint(4,8)

for i in range(tamanio):
	if (random.random() > 0.5) :
		cadena += "["
	else:
		cadena += "]"

print ("La Cadena Aleatoria Es %s" % (cadena))

cuenta = 0;

for i in range(len(cadena)):
	if (cadena[i] == "["):
		cuenta += 1
	else:
		cuenta -= 1
	if (cuenta < 0):
		print ("Hay Un Problema Con La Cadena En El Caracter %d." % (i)) 
		exit()

if (cuenta > 0):
	print ("¡Demasiados Corchetes Abiertos!")
else:
	print ("¡La Cadena Está Bien Formateada!")
  
