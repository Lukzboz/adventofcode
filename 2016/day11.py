import re

class Item:
	def __init__(self, floor, type, material):
		self.floor = floor
		self.type = type
		self.material = material
	
class Floor:
	def __init__(self, floor):
		self.items = []
		self.floor = floor
	
	def setItem(items):
		if ceckItem(items):
			self.items.append(item in items)
	
	def checkItem(items):
		#was wenn 2 gleiche materialien ankommen?
		result = True
		for item in items:
			for obj in self.items:
				if item.type == "chip" and obj.material == item.material:
					result = True
				elif item.material != item.material:
					result = False
		return result

class Elevator:
	def __init__(self, floor):
		self.floor = floor
		self.maxFloor = 4
		self.minFloor = 1
	
	def checkMove(items):
		if len(items) == 2 and items(0).material != items(1).material:
			return False
		return True
	
	def checkDir(dir):
		if (self.floor + dir > 4) or (self.floor + dir < 1):
			return False
		return True

class Emulator:
	
	def __init__(self):
		self.floors = []
		self.floors.append(Floor(1))
		self.floors.append(Floor(2))
		self.floors.append(Floor(3))
		self.floors.append(Floor(4))
		self.items = []
		self.items.append(Item(1, 'generator', 'strontium'))
		self.items.append(Item(1, 'chip', 'strontium'))
		self.items.append(Item(1, 'generator', 'plutonium'))
		self.items.append(Item(1, 'chip', 'plutonium'))
		self.items.append(Item(2, 'generator', 'thulium'))
		self.items.append(Item(2, 'generator', 'ruthenium'))
		self.items.append(Item(2, 'chip', 'ruthenium'))
		self.items.append(Item(2, 'generator', 'curium'))
		self.items.append(Item(2, 'chip', 'curium'))
		self.items.append(Item(3, 'chip', 'thulium'))
		self.elevator = Elevator(1)
		
		for floor in self.floors:
			for item in self.items:
				if item.floor == floor.floor:
					floor.setItem(item)
	
	def emulate():
		
	def tryMove():
		for item in self.items:
			
		

