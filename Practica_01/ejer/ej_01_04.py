fich = open('ej_01_04_in.txt','r')
line = fich.readline()
fich.close()
n = int(line)
fib1 = 1
fib2 = 1

for i in range(n - 2):
	aux = fib2
	fib2 = fib2 + fib1
	fib1 = aux

fich = open('ej_01_04_out.txt','w')
fich.write('%d' % (fib2)) 
fich.close() 
   
print ("El Numero %d De La Sucesión De Fibonacci Es %d. El Resultado Se Ha Grabado En El Fichero ej_01_04_out.txt" % (n, fib2))
