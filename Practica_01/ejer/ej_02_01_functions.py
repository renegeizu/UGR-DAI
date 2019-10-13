import copy

def printBoard(board):
	for y in range(len(board[0])):
		r = ""
		for x in range(len(board)):
			if (board[x][y] == 0):
				r += " "
			else:
				r += "*"
		print(r)
    
def cargaFichero(nombreFichero):
	fich = open(nombreFichero,'r')
	lines = fich.readlines()
	fich.close()
	height = len(lines) + 2
	width = len(lines[0].strip()) + 2
	board = [[0 for x in range(height)] for x in range(width)]
	for y in range(len(lines)):
		for x in range(len(lines[0].strip())):
			if (lines[y][x] == '0'):
				board[x + 1][y + 1] = 0
			else:
				board[x + 1][y + 1] = 1 
	return board
  
def iteracion(board):
	newBoard = copy.deepcopy(board)
	for x in range(1, len(board) - 1):
		for y in range(1, len(board[0]) - 1):
			celulasVivasAlrededor = board[x-1][y-1] + board[x][y-1] + board[x+1][y-1] + board[x-1][y] + board[x+1][y] + board[x-1][y+1] + board[x][y+1] + board[x+1][y+1];
			if (board[x][y] == 0):
				if (celulasVivasAlrededor == 3):
					newBoard[x][y] = 1
				else:
					newBoard[x][y] = 0
			if (board[x][y] == 1):
				if ((celulasVivasAlrededor == 2) or (celulasVivasAlrededor == 3)):
					newBoard[x][y] = 1
				else:
					newBoard[x][y] = 0
	for x in range(1, len(board) - 1):
		for y in range(1, len(board[0]) - 1):
			board[x][y] = newBoard[x][y]
