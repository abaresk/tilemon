
from src.constants import *
from src.tilemon import Tilemon
from src.mutate import Mutator
from src.generate import *
from src.compare import *

import random
from collections import defaultdict


class Society():
	def __init__(self):
		self.id = {}	# -> maps a randomly-generated id to a Tilemon
		self.cycle = 0
		self.initSociety()
		return

	# Initiate the society with a single member
	def initSociety(self):
		mon = self.createTilemon()
		monId = self.createId()
		self.id[monId] = mon
		return

	def createId(self):
		id = random.randint(0, MAX_TILEMON)
		while id in self.id:
			id = random.randint(0, MAX_TILEMON)
		return id

	# @profile
	def advanceCycle(self):
		self.cycle += 1
		self.reproduceCycle()
		if len(self.id) > 1:
			self.killSociety()
		return

	# Do a reproduction cycle over the society
	def reproduceCycle(self):
		for mon in list(self.id.values()):
			rand = random.random()
			if rand < mon.probReproduce:
				self.addTilemon(mon)
		return

	def addTilemon(self, parent):
		child, mutated = self.replicate(parent)
		childId = self.createId()
		self.id[childId] = child
		self.updateKin(child, parent, mutated)
		return

	def replicate(self, parent):
		dna = parent.dna
		rand = random.random()
		if rand < MUTATION_RATE:
			dna = Mutator(dna).mutate()
		return Tilemon(dna, self.cycle), rand < MUTATION_RATE

	def updateKin(self, child, parent, mutated):
		for member in list(parent.kin):
			gencmp = GenCmpLev(child.dna, member.dna)
			if not mutated or gencmp.distance() < gencmp.threshold:
				child.addKin(member)
				member.addKin(child)
			# else:
			# 	print('new species') # for debugging
		return

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
		return Tilemon(generateDNA())

	def printGen(self):
		for memberId in self.id:
			print(self.id[memberId].dna)
		return
