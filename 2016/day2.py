file_ = open('day2_input.txt', 'r')
location = 5

for line in file_:
	for char in list(line):
		if char == 'U':
			if location - 3 > 0:
				location = location - 3
		elif char == 'D':
			if location + 3 < 10:
				location = location + 3
		elif char == 'L':
			if (location - 1) % 3 != 0:
				location = location - 1
		elif char == 'R':
			if location % 3 != 0:
				location = location + 1
	print(location)

file_.close()