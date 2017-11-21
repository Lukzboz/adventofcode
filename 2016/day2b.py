file_ = open('day2b_input.txt', 'r')
x = 3
y = 1
pad = {}

pad[1,3] = 1
pad[2,2] = 2
pad[2,3] = 3
pad[2,4] = 4
pad[3,1] = 5
pad[3,2] = 6
pad[3,3] = 7
pad[3,4] = 8
pad[3,5] = 9
pad[4,2] = 'A'
pad[4,3] = 'B'
pad[4,4] = 'C'
pad[5,3] = 'D'
for line in file_:
	for char in list(line):
		if char == 'U':
			try:
				pad[x-1,y]
				x = x - 1
			except KeyError:
				pass
		elif char == 'D':
			try:
				pad[x+1,y]
				x = x + 1
			except KeyError:
				pass
		elif char == 'L':
			try:
				pad[x,y-1]
				y = y - 1
			except KeyError:
				pass
		elif char == 'R':
			try:
				pad[x,y+1]
				y = y + 1
			except KeyError:
				pass
	print(pad[x,y])
file_.close()