file_ = open('day1.txt', 'r')


for line in file_:
	last = -1
	first = -1
	sum = 0
	line = line.strip();
	for num in list(line):
		num = int(num)
		if (last == -1):
			first = num;
		
		if (last == num):
			sum = sum + last
		
		last = num;

	if (first == last):
		sum = sum + last
	print(sum)

file_.close()