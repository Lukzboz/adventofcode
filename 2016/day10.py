import re

class Bot:
	
	def __init__(self, id):
		self.high = -1
		self.low = -1
		self.id = id
		self.goalHigh = None
		self.goalLow = None
	
	def getChip(self, nr):
		if int(nr) > int(self.high):
			self.low = self.high
			self.high = nr
		else:
			self.low = nr
		if self.low > -1:
			print ("Give", self.id, self.goalHigh.id, self.high, self.goalLow.id, self.low)
			if (self.high == "61") and (self.low == "17"):
				print ("I am the one", self.id)
			self.giveChip()
	
	def storeGoal(self, basket, switch):
		if switch == "high":
			self.goalHigh = basket
		else:
			self.goalLow = basket
		
	def giveChip(self):
		self.goalHigh.getChip(self.high)
		self.high = -1
		self.goalLow.getChip(self.low)
		self.low = -1
		

class Bin:
	def __init__(self, id):
		self.Chip = -1
		self.id = id
	
	def getChip(self, nr):
		self.Chip = nr

file_ = open('day10_input.txt', 'r')
data = file_.readlines()
bots = {}
bins = {}
patternTake = "value (\d+) goes to bot (\d+)"
patternGive = "bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)"

for line in data:
	take = re.match(patternTake, line)
	if take != None:
		if not take.group(2) in bots:
			bots[take.group(2)] = Bot(take.group(2))
		bots[take.group(2)].getChip(take.group(1))
	
	give = re.match(patternGive, line)
	if give != None:
		if not give.group(1) in bots:
			bots[give.group(1)] = Bot(give.group(1))
		if give.group(2) == "bot":
			if not give.group(3) in bots:
				bots[give.group(3)] = Bot(give.group(3))
			bots[give.group(1)].storeGoal(bots[give.group(3)], "low")
		else:
			if not give.group(3) in bins:
				bins[give.group(3)] = Bin(give.group(3))
			bots[give.group(1)].storeGoal(bins[give.group(3)], "low")
		
		if give.group(4) == "bot":
			if not give.group(5) in bots:
				bots[give.group(5)] = Bot(give.group(5))
			bots[give.group(1)].storeGoal(bots[give.group(5)], "high")
		else:
			if not give.group(5) in bins:
				bins[give.group(5)] = Bin(give.group(5))
			bots[give.group(1)].storeGoal(bins[give.group(5)], "high")


for key, value in bins.items():
	print (key, value.Chip)

