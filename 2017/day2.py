import re

file_ = open('day2.txt', 'r')

sum = 0
for line in file_:
	row = map(int, re.split('\s+', line.strip()))
	max = row[0]
	min = row[0]
	
	for num in row:
		if num > max:
			max = num
		if num < min:
			min = num
	
	sum = sum + max - min
print(sum)

file_.close()