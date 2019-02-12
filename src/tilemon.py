'''
Data Structure for a Tilemon
	Tilemon class stores the genetic code and location of a Tilemon
'''
from src.constants import *
from src.genome import Genome
from src.point import Point

import math

class Tilemon():
	def __init__(self, genome=Genome(''), points=set(), loc=Point(0, 0), age=0):
		# Main data
		# self.genome = dna
		# self.points = points
		self.loc = loc
		self.age = age

		# Dependent data
		self.updateGenome(genome)
		# self.numTiles = self.getNumTiles()
		# # self.naturalLifeSpan = self.calcLifespan()
		# self.probReproduceTurn = self.getProbReproduceTurn()
		# self.rotateTime = self.getRotateTime()
		# self.reproduceTime = self.getReproduceTime()
		# return

	def updateGenome(self, genome):
		self.genome = genome
		self.shape = self.getShape()
		self.numTiles = len(self.shape)
		self.lifespan = self.calcLifespan()
		self.probReproduce = self.calcProbReproduce()
		self.gestatePeriod = self.calcGestatePeriod()
		self.rotatePeriod = self.calcRotatePeriod()
		return

	def getShape(self):
		path = [Point(0, 0)]
		for i in range(len(self.genome) // 2):
			x, y = self.genome.dna[2*i], self.genome.dna[2*i+1]
			if x != y:
				if x == 't':
					delta = 1 if y == 'c' else (0 if y == 'a' else -1)
					path.append(Point(path[-1].x + delta, path[-1].y + 1))

				elif x == 'a':
					delta = 1 if y == 't' else (0 if y == 'c' else -1)
					path.append(Point(path[-1].x + 1, path[-1].y + delta))

				elif x == 'c':
					delta = 1 if y == 'a' else (0 if y == 'g' else -1)
					path.append(Point(path[-1].x + delta, path[-1].y - 1))

				elif x == 'g':
					delta = 1 if y == 'a' else (0 if y == 't' else -1)
					path.append(Point(path[-1].x - 1, path[-1].y + delta))
			elif len(path) > 1:
				path.pop()

		return set(path)

	def calcLifespan(self):
		return MINIMUM_LIFE_SPAN + self.numTiles

	def calcProbReproduce(self):
		return 1.05 / self.lifespan	# reproduces ~1.1 times per lifetime

	def calcRotatePeriod(self):
		return math.ceil(math.log(self.numTiles)/math.log(4))

	def getReproduceTime(self):
		return 1 + math.ceil(math.log(len(self.genome))/math.log(8))

	def increaseAge(self):
		self.age += 1
		return


# # Test
# t1 = Tilemon(dna='cctggtttgggatctgtcaaagtcaacgtaccaactagtctccaacgcatcgtaggggccttatgcgtatggctcacaaaactaatgcgagggctctctaatacggccactcacgctaatcggcgatcctggttacgtca')
# t1.loc = [5,5]
# t1.getNumTiles()
