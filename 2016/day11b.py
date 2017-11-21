from __future__ import division
import math
import sys

def check4Pairs(floor):
	times = int(math.ceil(floor.bit_length()/2))
	for x in range(1, times):
		num = int(2**(x * 2 - 1) * 1.5)
		if (floor & num != num and floor & num != 0):
			return False
	return True

def check4ChipKills(floor):
	length = floor.bit_length()
	#is there a generator?
	num = 0
	for x in range (0, length, 2):
		num += 2**x
	if (floor & num == 0):
		#no generators -> allways save
		return True
	for x in range (0, length, 2):
		check = floor % 4
		floor = int(math.floor((floor / 4)))
		if (check == 2):
			#found an unprotected chip -> BURN IN HELL!
			return False
	#every chip is save YaY!
	return True

def rmElevator(floor):
	return floor - 2**(floor.bit_length() - 1)

def findItems(floor):
	found = []
	times = floor.bit_length() - 1
	for x in range (0, times):
		num = 2**x
		if num & floor != 0:
			found.append(num)
	return found

def findMoves(floor):
	result = []
	items = findItems(floor)
	for i in range(0, len(items)):
		for j in range(i, len(items)):
			item = items[i] | items[j]
			if check4ChipKills(item) == True:
				result.append(item + 2**(floor.bit_length() - 1))
	return result

'''
def findMoves(floor):
	result = []
	items = findItems(floor)
	for item1 in items:
		for item2 in items:
			item = item1 | item2
			if check4ChipKills(item) == True:
				result.append(item + 2**(floor.bit_length() - 1))
	return result
'''

def nextSteps(status):
	num = 2**14
	steps = []
	for key, val in enumerate(status):
		if (num & val):
			floor = key
			break
	moves = findMoves(status[floor])
	if floor - 1 >= 0:
		#1 floor up
		for move in moves:
			if check4ChipKills(move | status[floor-1]):
				step = list(status)
				step[floor] = step[floor] ^ move
				if check4ChipKills(step[floor]):
					step[floor-1] = step[floor-1] | move
					if not (step in steps):
						steps.append(step)
	if floor + 1 < len(status):
		#1 floor down
		for move in moves:
			if check4ChipKills(move | status[floor+1]):
				step = list(status)
				step[floor] = step[floor] ^ move
				if check4ChipKills(step[floor]):
					step[floor+1] = step[floor+1] | move
					if not (step in steps):
						steps.append(step)
	return steps

# 2, 8, 32,.. Chips
# 1, 4, 16,.. Generators
start = [[int('111110000001111', 2), int('000000111110000', 2), int('000001000000000', 2), int('000000000000000', 2)]]
goal = [0,0,0,int('111111111111111', 2)]
steps = 0
#print(findMoves(start[0][0]))

moves = []
moves.append(start)
print(moves)
while 1:
	stepMoves = []
	for move in moves[steps]:
		if (move == goal):
			print(move)
			sys.exit(steps)
		newSteps = list(nextSteps(move))
		for step in newSteps:
			add = True
			for checkSteps in moves:
				if (step in checkSteps) == True:
					add = False
			if (add == True):
				if (step in stepMoves) != True:
					stepMoves.append(step)
	moves.append(stepMoves)
	print(steps, len(moves[steps]))
	#print(moves)
	if len(moves[steps]) > 40000 or len(moves[steps]) == 0:
		#print(moves)
		sys.exit(steps)
	steps += 1

