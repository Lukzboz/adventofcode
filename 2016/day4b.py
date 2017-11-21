import re
import operator

file_ = open('day4b_input.txt', 'r')
sum = 0

for line in file_:
	lineChars = list(re.match('[a-z\-]+', line).group(0))
	lineNum = int(re.search(r'\d+', line).group(0))
	offset = lineNum % 26
	name = ""
	for char in lineChars:
		if char != '-':
			uni = ord(char) + offset
			if uni > 122:
				name = name + chr(uni - 26)
			else:
				name = name + chr(uni)
		else:
			name = name + " "
	if name.find("north") != -1:
		print(lineNum)
		print(name)
