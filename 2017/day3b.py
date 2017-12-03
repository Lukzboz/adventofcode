import math

input = 277678
startX = 10
startY = 10
line = 1
nextValue = 0

arr = [ [ 0 for y in range(startX * 2 + 1) ] for x in range(startY * 2 + 1) ]
arr [startX][startY] = 1

def getVal (arr, indexX, indexY):
	sum = 0
	for i in range (-1, 2):
		for j in range (-1, 2):
			if (i != 0 or j != 0):
				sum+= arr[indexX + i][ indexY + j]
	return sum


while nextValue <= input:
	startX += 1
	startY += 1
	for i in range(0, 4):
		for j in range (0, line * 2):
			if i == 0:
				startY -= 1
			elif i == 1:
				startX -= 1
			elif i == 2:
				startY += 1
			elif i == 3:
				startX += 1
			nextValue = getVal(arr, startX, startY)
			arr[startX][startY] = nextValue
			if nextValue > input:
				break 
		if nextValue > input:
			break 
	line += 1

print(nextValue)

