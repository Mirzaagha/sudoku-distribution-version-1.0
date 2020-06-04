import numpy as np
from random import randint
sudoku = np.arange(81).reshape(9, -1)
print(sudoku)
blocks = np.zeros((9,9),dtype=np.int)
iterator = 0
avoid = np.zeros((9),dtype=np.int)

while iterator < 81:
	key = 1
	x = iterator%9
	y = int(iterator/9)
	if y < 3:
		if x < 3:
			a = 0
		elif x < 6:
			a = 1
		else:
			a = 2
	elif y < 6:
		if x < 3:
			a = 3
		elif x < 6:
			a = 4
		else:
			a = 5
	else:
		if x < 3:
			a = 6
		elif x < 6:
			a = 7
		else:
			a = 8
	random = randint(1,9)
	for z in range(0,x):
		if sudoku[z][y] == random:
			key = 0
	if key:
		for z in range(0,y):
			if sudoku[x][z] == random:
				key = 0
	if key:
		if blocks[a][random - 1]:
			key = 0
	if key:
		sudoku[x][y] = random
		blocks[a][random - 1] = 1
		iterator = iterator + 1
		for t in range(0,9):
			avoid[t] = 0
	else:
		avoid[random - 1] = 1
	if avoid[0] and avoid[1] and avoid[2] and avoid[3] and avoid[4] and avoid[5] and avoid[6] and avoid[7] and avoid[8]: 
		for e in range(0,2):
			iterator = iterator - 1
			x = iterator%9
			y = int(iterator/9)
			if y < 3:
				if x < 3:
					a = 0
				elif x < 6:
					a = 1
				else:
					a = 2
			elif y < 6:
				if x < 3:
					a = 3
				elif x < 6:
					a = 4
				else:
					a = 5
			else:
				if x < 3:
					a = 6
				elif x < 6:
					a = 7
				else:
					a = 8
			blocks[a][sudoku[x][y] - 1] = 0
			sudoku[x][y] = 0
for y in range(9):
	for x in range(9):
		print(sudoku[x][y], end='  ')
	print()
