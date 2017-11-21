import re
screenX = 6
screenY = 50
file_ = open('day8_input.txt', 'r')
sum = 0
screen = [[0 for x in range(screenX)] for y in range(screenY)]
for line in file_:
	if line.find("rect") != -1:
		parts = re.split('[x ]', line.strip())
		for i in range (0, int(parts[1])):
			for j in range (0, int(parts[2])):
				screen[i][j] = 1
	elif line.find("column") != -1:
		lineNums = re.findall('\d+', line)
		column = [0 for x in range(screenX)]
		y = int(lineNums[0])
		for key, val in enumerate(screen[y]):
			newK = (key + int(lineNums[1])) % screenX
			column[newK] = val
		screen[y] = column
	elif line.find("row") != -1:
		lineNums = re.findall('\d+', line)
		row = [0 for y in range(screenY)]
		x = int(lineNums[0])
		for i in range(0, screenY):
			newK = (i + int(lineNums[1])) % screenY
			row[newK] = screen[i][x]
		for i in range(0, screenY):
			screen[i][x] = row[i]
for i in range(0, screenX):
	newLine = ""
	for j in range(0, screenY):
		sum += screen[j][i]
		if screen[j][i] == 1:
			newLine += '#'
		else:
			newLine += ' '
	print newLine

print(sum)