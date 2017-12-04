import re

file_ = open('day4.txt', 'r')

sum = 0
for line in file_:
	row = re.split('\s+', line.strip())
	valide = 1
	for i in range(0, len(row)):
		for j in range(i + 1, len(row)):
			if (sorted(row[i]) == sorted(row[j])):
				valide = 0;
				break;
		if (valide == 0):
			break;
	sum += valide
print(sum)

file_.close()