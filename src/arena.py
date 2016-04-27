import jsonpickle

class ArenaType():
	Circle = 0
	Square = 1

class ArenaCoverType():
	Soil = 0
	Sand = 1
	Grass = 2
	Stone = 3

class Arena():
	def __init__(self, name, size, stype, cover):
		self.name = name
		self.size = size
		self.type = stype
		self.cover = cover