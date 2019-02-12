'''
Data Structure for the all Tilemons in the world

	* Each Tilemon keeps track of its own:
		+ age
		+ location
		+ genetic code

	* Society keeps a record of:
		+ all living creatures
		+ all species listings

	* World will use the information in Society to find life statistics, 
	  such as:
	  	+ how much surface area of each creature is covered
	  	+ how much space each creature has around it

	* WorldEngine will use Society to do large-scale operations, such as:
		+ update Society with new creatures / dead creatures
		+ move species members closer together
		+ reproduction (hold onto id of parent)
		+ kill creatures
'''

import uuid
import random
from collections import defaultdict

from . import tilemon
from . import mutate
from . import genome_gen as gg
from . import genome_compare as gc

# Constants
LEVDISTANCE_THRESHOLD = 5	# maybe make lower

# MUTATION_RATE should be 0.001!!
MUTATION_RATE = 0.25


class Society():
	def __init__(self):
		self.id = {}	# -> maps a randomly-generated id to a Tilemon

		# maps each tilemon's id to the id's of its kin
		self.id2kin = defaultdict(list) 

		# Startup function - initializes society with 1 member
		self.beginSociety()
		return


	# Initiate the society with a single member
	def beginSociety(self):
		tile = self.generateTilemon()
		tileId = str(uuid.uuid4())

		self.id[tileId] = tile
		self.id2kin[tileId].append(tileId)
		return


	# Everything that happens in a given turn (besides movement)
	# Age everyone then reproduce (so babies start at 0). Then kill those 
	# that exceeded their age limit
	def turnCycle(self):
		self.ageSociety()
		self.reproduceSociety()
		if len(self.id) > 1:
			self.killSociety()
		return


	def ageSociety(self):
		for memberId in list(self.id.keys()):
			self.id[memberId].increaseAge()
		return


	# Do a reproduction cycle over the society
	def reproduceSociety(self):
		for memberId in list(self.id.keys()):
			probReproduceTurn = self.id[memberId].probReproduceTurn
			rando = random.random()
			if rando < probReproduceTurn:
				self.addTilemon(memberId)
		return

	def addTilemon(self, parentId):
		childmon = self.reproduce(parentId)
		childId = str(uuid.uuid4())

		self.id[childId] = childmon
		self.updateKin(childId, parentId)
		return

	def reproduce(self, parentId):
		# return the child Tilemon
		genome = self.id[parentId].dna
		childGenome = genome

		# TODO: figure out how to generate the child location
		parentLoc = self.id[parentId].loc

		# Mutation
		if random.random() < MUTATION_RATE:
			childGenome = mutate.mutateGenome(genome)

		childmon = tilemon.Tilemon(dna=childGenome)

		return childmon

	def updateKin(self, childId, parentId):
		parentKin = list(self.id2kin[parentId])
		for memberId in parentKin:
			if self._genomeDistance(memberId, childId) <= LEVDISTANCE_THRESHOLD:
				self.id2kin[childId].append(memberId)
				self.id2kin[memberId].append(childId)
			# else:
				# print('new species') # for debugging
		self.id2kin[childId].append(childId)
		return


	# Do a killing cycle over the society
	def killSociety(self):
		for memberId in list(self.id.keys()):
			if self.id[memberId].age >= self.id[memberId].actualLifeSpan:
				self.killTilemon(memberId)
		return

	# Write code to kill old creatures
	def killTilemon(self, monId):
		del self.id[monId]

		for memberId in self.id2kin[monId]:
			if memberId != monId:
				self.id2kin[memberId].remove(monId)

		self.id2kin.pop(monId)
		return



	def generateTilemon(self):
		return tilemon.Tilemon(dna=gg.generate())


	def _genomeDistance(self, id1, id2):
		genome1 = self.id[id1].dna
		genome2 = self.id[id2].dna

		return gc.levDistance(genome1, genome2)


	def printGen(self):
		for memberId in self.id:
			print(self.id[memberId].dna)
		return

