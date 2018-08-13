'''
Data Structure for a Tilemon
	Tilemon class stores the genetic code and location of a Tilemon
'''
import math

from genome_decode import decodeGenome

REPRODUCE_FAILURE_PROB = 0.05

class Tilemon():
	def __init__(self, dna = '', loc = [0,0], age = 0):
		# Main data
		self.dna = dna
		self.loc = loc
		self.age = age

		# Dependent data
		self.numTiles = self.getNumTiles()
		self.lifeSpan = self.getLifeSpan()
		self.probReproduceTurn = self.getProbReproduceTurn()
		self.rotateTime = self.getRotateTime()
		self.reproduceTime = self.getReproduceTime()
		return

	def getMarkedSpaces(self):
		xPoints, yPoints = decodeGenome(self.dna)
		return [xPoints, yPoints]

	def getPoints(self):
		xPoints, yPoints = self.getMarkedSpaces()

		for i in range(len(xPoints)):
			xPoints[i] += self.loc[0]
			yPoints[i] += self.loc[1]

		return [xPoints,yPoints]

	def getNumTiles(self):
		xPoints = self.getMarkedSpaces()[0]
		return len(xPoints)

	def getLifeSpan(self):
		return 14 + self.getNumTiles()

	def getProbReproduceTurn(self):
		return 1 - math.pow(REPRODUCE_FAILURE_PROB, 1 / (self.getLifeSpan()))

	def getRotateTime(self):
		return math.ceil(math.log(self.getNumTiles())/math.log(4))

	def getReproduceTime(self):
		return 1 + math.ceil(math.log(len(self.dna))/math.log(8))

	# Update to fit new information
	def update(self):
		self.numTiles = self.getNumTiles()
		self.lifeSpan = self.getLifeSpan()
		self.probReproduceTurn = self.getProbReproduceTurn()
		self.rotateTime = self.getRotateTime()
		self.reproduceTime = self.getReproduceTime()
		return


# Test
t1 = Tilemon(dna='cctggtttgggatctgtcaaagtcaacgtaccaactagtctccaacgcatcgtaggggccttatgcgtatggctcacaaaactaatgcgagggctctctaatacggccactcacgctaatcggcgatcctggttacgtca')
t1.loc = [5,5]
t1.getNumTiles()