import random

def burbuja(lista):
	for i in range(len(lista)):
		for h in range(i, len(lista) - 1):
			if (lista[h] > lista[h+1]):
				aux = lista[h]
				lista[h] = lista[h + 1]
				lista[h + 1] = aux

def burbujaMejorada(lista):
	for i in range(len(lista)):
		cambio = False
		for h in range(i, len(lista) - 1):
			if (lista[h] > lista[h+1]):
				aux = lista[h]
				lista[h] = lista[h + 1]
				lista[h + 1] = aux
				cambio = True        
		if not cambio:
			return

def reemplazo(lista):
	for i in range(len(lista) - 1):
		currentPos = i    
		for h in range(i + 1, len(lista)):
			if (lista[h] < lista[currentPos]):
				currentPos = h  
			aux = lista[i]
			lista[i] = lista[currentPos]
			lista[currentPos] = aux

def mergeSort(lista):
	listaTrabajo = list(lista)
	mergeSort2(lista, 0, len(lista) - 1, listaTrabajo)

def mergeSort2(lista, i1, i2, listaTrabajo):  
	if (i1 == i2):
		return
	medio = (int)((i1 + i2) / 2)
	mergeSort2(lista, i1, medio, listaTrabajo)
	mergeSort2(lista, medio + 1, i2, listaTrabajo)
	punt1 = i1
	punt2 = medio + 1
	puntB = i1
	while ( (punt1 <= medio) and (punt2 <= i2) ): 
		if (lista[punt1] < lista[punt2]):
			listaTrabajo[puntB] = lista[punt1]
			punt1 += 1
		else:
			listaTrabajo[puntB] = lista[punt2]
			punt2 += 1
		puntB += 1
	for i in range(punt1, medio + 1):
		listaTrabajo[puntB] = lista[i]
		puntB += 1   
	for i in range(punt2, i2 + 1):
		listaTrabajo[puntB] = lista[i]
		puntB += 1
	for i in range(i1, i2 + 1):
		lista[i] = listaTrabajo[i]

def generaListaAleatoria():
	tamanioLista = 10000;
	lista = []
	for i in range(tamanioLista):
		lista.append(random.randint(0, 10000000)); 
	return lista
