import re
import operator

file_ = open('day4_input.txt', 'r')
sum = 0
chars = {}
for line in file_:
	lineChars = list(re.match('[a-z\-]+', line).group(0))
	lineNum = int(re.search(r'\d+', line).group(0))
	lineTestString = re.search(r'\[\w+\]', line).group(0)
	for char in lineChars:
		if char != '-':
			try:
				chars[char] += 1
			except KeyError:
				chars[char] = 1
	
	sortedChars = sorted(chars.items())
	sortedChars = sorted(sortedChars, key=operator.itemgetter(1), reverse=True)
	topFive = sortedChars[:5]
	yes = 0
	for char in topFive:
		if lineTestString.find(char[0]) != -1:
			yes = yes + 1
	if yes == 5:
		sum = sum + lineNum
	chars = {}
print(sum)