'''
Compare the genomes of different tilemons
	* Uses Rank Distance to compute the distance between two genome strings
	* This algorithm runs linearly, as opposed to standard Levenshtein Distance
	* Reference: https://pdfs.semanticscholar.org/3208/ba4168dbd5b28669e66f427f94ea5f95d332.pdf
'''
from collections import defaultdict
from collections import deque

class GenomeCompare():
	def __init__(self, genome1, genome2):
		self.genome1 = genome1
		self.genome2 = genome2
		self.genMap1 = defaultdict(deque)
		self.genMap2 = defaultdict(deque)

	def makeGenMaps(self):
		self.genMap1 = self.initDict(self.genome1)
		self.genMap2 = self.initDict(self.genome2)
		return

	# @profile
	def initDict(self, genome):
		dict = defaultdict(deque)
		for i, ntide in enumerate(genome.dna):
			dict[ntide].append(i)
		return dict

	# @profile
	def distance(self):
		dist = 0
		self.makeGenMaps()
		dist += self.getRankDistance()

		self.genome1.reverse()
		self.genome2.reverse()

		self.makeGenMaps()
		dist += self.getRankDistance()

		dist /= len(self.genome1) * (len(self.genome1) + 1) + len(self.genome2) * (len(self.genome2) + 1)
		return dist

	# @profile
	def getRankDistance(self):
		dist = 0
		for ntide in self.genMap1:
			while self.genMap1[ntide] and self.genMap2[ntide]:
				index1, index2 = self.genMap1[ntide].popleft(), self.genMap2[ntide].popleft()
				dist += abs(index1 - index2)
			while self.genMap1[ntide] or self.genMap2[ntide]:
				if self.genMap1[ntide]:
					dist += self.genMap1[ntide].popleft()
				else:
					dist += self.genMap2[ntide].popleft()
		return dist
