
from src.constants import *
from src.tilemon import Tilemon
from src.mutate import Mutator
from src.genome import Genome
from src.generate import Generator
from src.compare import GenomeCompare as Gencmp

import random
from collections import defaultdict


class Society():
	def __init__(self):
		self.id = {}	# -> maps a randomly-generated id to a Tilemon
		self.cycle = 0

		self.generator = Generator()

		self.initSociety()
		return

	# Initiate the society with a single member
	def initSociety(self):
		mon = self.createTilemon()
		monId = self.createId()
		self.id[monId] = mon
		return

	def createId(self):
		id = random.randint(0, 1_000)
		while id in self.id:
			id = random.randint(0, 1_000)
		return id

	# Everything that happens in a given turn (besides movement)
	# Age everyone then replicate (so babies start at 0). Then kill those
	# that exceeded their age limit
	def advanceCycle(self):
		self.cycle += 1
		self.reproduceCycle()
		if len(self.id) > 1:
			self.killSociety()
		return

	# Do a reproduction cycle over the society
	def reproduceCycle(self):
		for mon in list(self.id.values()):
			rando = random.random()
			if rando < mon.probReproduce:
				self.addTilemon(mon)
		return

	def addTilemon(self, parent):
		child = self.replicate(parent)
		childId = self.createId()
		self.id[childId] = child
		self.updateKin(child, parent)
		return

	def replicate(self, parent):
		genome = parent.genome
		if random.random() < MUTATION_RATE:
			genome = Genome(Mutator(genome.dna).mutate())
		return Tilemon(genome, self.cycle)

	def updateKin(self, child, parent):
		for member in list(parent.kin):
			gencmp = Gencmp(child.genome, member.genome)
			if gencmp.distance() < DISTANCE_THRESHOLD:
				child.addKin(member)
				member.addKin(child)
			# else:
			# 	print('new species') # for debugging
		return

	# Do a killing cycle over the society
	def killSociety(self):
		for monId, mon in list(self.id.items()):
			if self.calcMonAge(mon) > mon.lifespan:
				self.killTilemon(monId)
		return

	def calcMonAge(self, mon):
		return self.cycle - mon.birthday

	def killTilemon(self, monId):
		for member in list(self.id[monId].kin):
			member.removeKin(self.id[monId])
		del self.id[monId]
		return

	def createTilemon(self):
		return Tilemon(self.generator.generate())

	def printGen(self):
		for memberId in self.id:
			print(self.id[memberId].dna)
		return
