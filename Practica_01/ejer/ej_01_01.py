import random

numeroAdivinar = random.randint(1, 100)
numero = -1
iteraciones = 0
maxIntentos = 10;

print ("Bienvenido Al Wonderfuloso Juego De Adivinar Un Número")

while (numero != numeroAdivinar) and (iteraciones < maxIntentos):
	leido = input("Adivina Un Número Entre 1 Y 100 (Te Quedan %i Intentos)... " % (maxIntentos - iteraciones))
	numero = int(leido)
	if (numero < 1) or (numero > 100):
		print ("Tu Eres Tonto, El Número Tiene Que Estar Entre 1 Y 100.")
	elif (numero < numeroAdivinar):
		print ("El Número Buscado Es Mayor Que %i." % (numero))
	elif (numero > numeroAdivinar):
		print ("El Número Buscado El Menor Que %i." % (numero))
	else:
		print ("Felicidades, El Número Buscado Era El %i." % (numeroAdivinar))
	iteraciones += 1
 
if (iteraciones == maxIntentos):
	print ("Lo Siento, No Te Quedan Más Intentos. El Número Buscado Era El %i. Y tú Eres Un Poco Ceporro Por No Haberlo Adivinado." % (numeroAdivinar))    
