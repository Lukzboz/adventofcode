file_ = open('day1b.txt', 'r')


for line in file_:
	last = -1
	first = -1
	sum = 0
	line = line.strip();
	input = list(line);
	half = len(input) / 2
	for i in range (0, half - 1):
		if (input[i] == input[half + i]):
			sum = sum + int(input[i]) * 2
	print(sum)

file_.close()