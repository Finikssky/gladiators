import jsonpickle
import random

class ArenaType():
	Circle = 0
	Square = 1

class ArenaCoverType():
	Soil = 0
	Sand = 1
	Grass = 2
	Stone = 3

class Arena():
	def __init__(self, name, size = 1, stype = ArenaType.Circle, cover = ArenaCoverType.Sand):
		self.name = name
		self.size = size
		self.type = stype
		self.cover = cover

	def generate(self, name = "unnamed"):
		self.name = name
		self.type = random.randint(0, 1)
		self.cover = random.randint(0, 3)
		self.size = random.randint(100, 500)