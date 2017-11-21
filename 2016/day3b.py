import re

file_ = open('day3b_input.txt', 'r')
num = 0
i = 0
num1 = [0] * 3
num2 = [0] * 3
num3 = [0] * 3
for line in file_:
	#rect = map(int, line.strip().split('[ ]+'))
	rect = map(int, re.split('\s+', line.strip()))
	num1[i] = rect[0]
	num2[i] = rect[1]
	num3[i] = rect[2]
	if i == 2:
		num1 = sorted(num1)
		num2 = sorted(num2)
		num3 = sorted(num3)
		if (num1[0] + num1[1] > num1[2]):
			num = num + 1
		if (num2[0] + num2[1] > num2[2]):
			num = num + 1
		if (num3[0] + num3[1] > num3[2]):
			num = num + 1
		i = 0
	else:
		i = i + 1
print(num)