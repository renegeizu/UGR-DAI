import sys
import re

line = "sdfFFG S"

def apellidoInicial(string):
	a = re.compile(r'([A-Za-z]+) ([A-Z])')
	return a.match(string)

def email(string):
	a = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b')
	return a.match(string)

def tarjetaCredito(string):
	a = re.compile(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})')
	return a.match(string)

while True:
	print ("\nIntroduce Un Texto... ")
	leido = sys.stdin.readline()  
	if apellidoInicial(leido):
		print ("SI Es Un Apellido Inicial")
	else:
		print ("NO Es Un Apellido Inicial")
	if email(leido):
		print ("SI Es Un Email")
	else:
		print ("NO Es Un Email") 
	if tarjetaCredito(leido):
		print ("SI Es Un Número De Tarjeta")
	else:
		print ("NO Es Un Número De Tarjeta") 
