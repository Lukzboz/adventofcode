import re

file_ = open('day2b.txt', 'r')

sum = 0
for line in file_:
	row = map(int, re.split('\s+', line.strip()))
	
	for num in row:
		for div in row:
			if (num != div and num % div == 0):
				sum = sum + num / div
	
print(sum)

file_.close()