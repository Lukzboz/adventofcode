import math

input = 277678

root = math.ceil(math.sqrt(input))
if (root % 2) == 0:
	root = root + 1

minSteps = int((root - 1) / 2);
inputInRow = input - math.pow(root-2, 2)
sideSteps = minSteps - (inputInRow % (minSteps * 2))
if (sideSteps < 0):
	sideSteps *= -1

print (minSteps + sideSteps)