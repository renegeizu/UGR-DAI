import time
from ej_02_01_functions import *

board = cargaFichero('ej_02_01.txt')
    
printBoard(board);

while True:
	time.sleep(0.3)
	iteracion(board);
	printBoard(board);   
