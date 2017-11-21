import re
file_ = open('day9_input.txt', 'r')
sum = 0
unzipped = ""
for line in file_:
	line = line.strip()
	pattern = re.search("\((\d+)x(\d+)\)", line)
	while pattern != None:
		unzipped += line[0:(pattern.start(1) - 1)]
		line = line[(pattern.end(2) + 1):]
		part = line[:int(pattern.group(1))]
		for i in range(0, int(pattern.group(2))):
			unzipped += part
		line = line[int(pattern.group(1)):]
		pattern = re.search("\((\d+)x(\d+)\)", line)
		
	unzipped += line
print(unzipped)
print(len(unzipped))