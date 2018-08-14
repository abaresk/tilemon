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
from collections import defaultdict

from . import tilemon
from . import genome_gen
from .genome_compare import levDistance

# Constants
LEVDISTANCE_THRESHOLD = 10


class Society():
	def __init__(self):
		self.id = {}	# -> maps a randomly-generated id to a Tilemon
		self.id2species = defaultdict(list)
		self.species2id = defaultdict(list)

		# Startup function - initializes society with 1 member
		self.beginSociety()
		return


	def generateTilemon(self):
		return tilemon.Tilemon(dna=genome_gen.generate())

	def beginSociety(self):
		tile = self.generateTilemon()
		tileId = str(uuid.uuid4())
		speciesId = str(uuid.uuid4())

		self.id[tileId] = tile
		self.id2species[tileId].append(speciesId)
		self.species2id[speciesId].append(tileId)
		return


	def addTilemon(self, parentId):
		childmon = reproduce(parentId)
		childId = str(uuid.uuid4())

		self.id[childId] = childmon
		self.addToSpeciesLists(childId, parentId)
		return


	def addToSpeciesLists(self, childId, parentId):
		parentSpecies = self.id2species[parentId] 	# list of species it's in

		# for each species the parent is in
		for species in parentSpecies:	
			diffSpecies = set()

			# check if the child matches each member
			for memberId in self.species2id[species]:	
				if self._genomeDistance(memberId, childId) > LEVDISTANCE_THRESHOLD:
					diffSpecies.add(memberId)

			# if it doesn't match with some
			if diffSpecies:	
				sameSpecies = set(self.species2id[species]) - diffSpecies

				# Create new species, add members to it, and add it to members
				newSpeciesId = str(uuid.uuid4())
				self.species2id[newSpeciesId] = list(sameSpecies)

				for memberId in sameSpecies:
					self.id2species[memberId].append(newSpeciesId)

			# !!! Figure out how to add child info !!!
			else:
				self.species2id[parentSpecies].append(childId)
				self.id2species[chil]
		return


	def reproduce(self, parentId):
		# return the child Tilemon
		pass


	def _genomeDistance(self, id1, id2):
		genome1 = self.id[id1].dna
		genome2 = self.id[id2].dna

		return levDistance(genome1, genome2)





