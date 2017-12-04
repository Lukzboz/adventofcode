import re
file_ = open('day2_input.txt', 'r')

register = { 'a' : 0, 'b' : 0, 'c' : 1, 'd' : 0 }
i = 0

with open('day12_input.txt', 'r') as f:
    lines = f.readlines()

while i < len(lines):
	command = re.split('\s+', lines[i].strip())
	#print (command)
	
	if (command[0] == 'cpy') :
		#copy
		try:
			register[command[2]] = int(command[1])
		except ValueError:
			register[command[2]] = register[command[1]]
	elif (command[0] == 'inc') :
		#add 1
		register[command[1]] += 1
	elif (command[0] == 'dec') :
		#sub 1
		register[command[1]] -= 1
	elif (command[0] == 'jnz') :
		#goto
		try:
			if (int(command[1]) != 0) :
				i = i + int(command[2])
				continue
		except ValueError:
			if (register[command[1]] != 0) :
				i = i + int(command[2])
				continue
	i += 1
	print(register)
	
print(register)