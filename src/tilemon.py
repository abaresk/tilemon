'''
Data Structure for a Tilemon
	Tilemon class stores the genetic code, shape and location of a Tilemon
'''
from src.constants import *
from src.point import Point

import math

class Tilemon():
	def __init__(self, dna='', birthday=0, pos=Point(0, 0)):
		self.pos = pos
		self.birthday = birthday
		self.dna = dna
		self.kin = {self}

		# Dependent data
		self.updateGenome(dna)
		return

	def updateGenome(self, dna):
		self.dna = dna
		self.shape = self.getShape()
		self.numTiles = len(self.shape)
		self.lifespan = self.calcLifespan()
		self.probReproduce = self.calcProbReproduce()
		self.gestatePeriod = self.calcGestatePeriod()
		self.rotatePeriod = self.calcRotatePeriod()
		return

	def addKin(self, mon):
		self.kin.add(mon)
		return

	def removeKin(self, mon):
		assert(mon in self.kin)
		self.kin.remove(mon)
		return

	def getShape(self):
		path = [Point(0, 0)]
		points = set([p.toTuple() for p in path])
		for i in range(len(self.dna) // 2):
			x, y = self.dna[2*i], self.dna[2*i+1]
			if x != y:
				if x == 't':
					delta = 1 if y == 'c' else (0 if y == 'a' else -1)
					point = Point(path[-1].x + delta, path[-1].y + 1)

				elif x == 'a':
					delta = 1 if y == 't' else (0 if y == 'c' else -1)
					point = Point(path[-1].x + 1, path[-1].y + delta)

				elif x == 'c':
					delta = 1 if y == 'a' else (0 if y == 'g' else -1)
					point = Point(path[-1].x + delta, path[-1].y - 1)

				elif x == 'g':
					delta = 1 if y == 'a' else (0 if y == 't' else -1)
					point = Point(path[-1].x - 1, path[-1].y + delta)

				points.add(point.toTuple())
				path.append(point)
			elif len(path) > 1:
				path.pop()

		return points

	def calcLifespan(self):
		return MINIMUM_LIFE_SPAN + self.numTiles

	def calcProbReproduce(self):
		return 1.05 / self.lifespan	# reproduces ~1.05 times per lifetime

	def calcRotatePeriod(self):
		return math.ceil(math.log(self.numTiles)/math.log(4))

	def calcGestatePeriod(self):
		return 1 + math.ceil(math.log(len(self.dna))/math.log(8))
