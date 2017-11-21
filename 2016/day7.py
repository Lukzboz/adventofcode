import re

def searchForPattern(heystack):
	for i in range(0, (len(heystack) - 3)):
		if heystack[i] == heystack[i+3]:
			if heystack[i] != heystack[i+1]:
				if heystack[i+1] == heystack[i+2]:
					return True
	return False

file_ = open('day7_input.txt', 'r')
sum = 0

for line in file_:
	parts = re.split('[\[\]]', line.strip())
	i = 1
	tls = False
	for part in parts:
		if i % 2 == 1 and searchForPattern(part):
			tls = True
		elif i % 2 == 0 and searchForPattern(part):
			tls = False
			break
		i = i + 1
	if tls:
		sum = sum + 1

print(sum)

