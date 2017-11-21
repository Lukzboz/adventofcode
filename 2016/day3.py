import re

file_ = open('day3_input.txt', 'r')
num = 0

for line in file_:
	#rect = map(int, line.strip().split('[ ]+'))
	rect = map(int, re.split('\s+', line.strip()))
	rect = sorted(rect)
	if (rect[0] + rect[1] > rect[2]):
		num = num + 1
print(num)