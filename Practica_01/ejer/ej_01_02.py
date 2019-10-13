from ej_01_02_functions import *
import time

lista1 = generaListaAleatoria()
lista2 = list(lista1)
lista3 = list(lista1)
lista4 = list(lista1)

start = time.process_time()
burbuja(lista1)
end = time.process_time()

print ("El Método De Burbuja Ha Tardado %f Segundos" % (end - start))

start = time.process_time()
burbujaMejorada(lista2)
end = time.process_time()

print ("El Método De Burbuja Mejorada Ha Tardado %f Segundos" % (end - start))

start = time.process_time()
reemplazo(lista3)
end = time.process_time()

print ("El Método De Reemplazo Ha Tardado %f Segundos" % (end - start))

start = time.process_time()
mergeSort(lista4)
end = time.process_time()

print ("El Método De MergeSort Ha Tardado %f Segundos" % (end - start))
