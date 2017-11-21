import re

def workOnPattern (pattern, part):
	sum = 0
	insidePattern = re.search("\((\d+)x(\d+)\)", part)
	while insidePattern != None:
		sumX = workOnPattern(insidePattern, part[(insidePattern.end(2) + 1):insidePattern.end(2) + 1 + int(insidePattern.group(1))])
		#sumX += pattern.start(1) - 1
		sum += sumX * int(pattern.group(2))
		part = part[insidePattern.end(2) + 1 + int(insidePattern.group(1)):]
		insidePattern = re.search("\((\d+)x(\d+)\)", part)
	return sum + (len(part) * int(pattern.group(2)))


file_ = open('day9b_input.txt', 'r')
sum = 0
unzipped = ""
for line in file_:
	line = line.strip()
	
	pattern = re.search("\((\d+)x(\d+)\)", line)
	while pattern != None:
		sum += pattern.start(1) - 1
		line = line[(pattern.end(2) + 1):]
		part = line[:int(pattern.group(1))]
		sum += workOnPattern(pattern, part)
		line = line[int(pattern.group(1)):]
		pattern = re.search("\((\d+)x(\d+)\)", line)
	
	sum += len(line)
print(sum)
