print ("Bienvenido Al Programa De La Criba De Eratóstenes.")

limite = int(input("Introduce Hasta Que Número Quieres Calcular Los Primos: "))

l = list(range(limite))

for i in range(2, limite):
	if l[i] != -1:
		print (i)    
	for h in range(i, limite, i):
		l[h] = -1

print ("Ahí Lo Llevas :-P")
