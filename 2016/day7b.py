import re

def searchForPattern(heystack):
	patterns = []
	for i in range(0, (len(heystack) - 2)):
		if heystack[i] == heystack[i+2]:
			if heystack[i] != heystack[i+1]:
				pattern = heystack[i+1] + heystack[i] + heystack[i+1]
				patterns.append(pattern)
	return patterns

file_ = open('day7b_input.txt', 'r')
sum = 0

for line in file_:
	parts = re.split('[\[\]]', line.strip())
	i = 1
	patterns = []
	hyper = ""
	for part in parts:
		if i % 2 == 1:
			found = searchForPattern(part)
			for item in found:
				patterns.append(item)
		elif i % 2 == 0:
			hyper = hyper + " " + part
		i = i + 1
	for pattern in patterns:
		if hyper.find(pattern) != -1:
			sum = sum + 1
			break

print(sum)

