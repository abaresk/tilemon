'''
Compare the genomes of different tilemons
	* Uses Rank Distance to compute the distance between two genome strings
	* This algorithm runs linearly, as opposed to standard Levenshtein Distance
	* Reference: https://pdfs.semanticscholar.org/3208/ba4168dbd5b28669e66f427f94ea5f95d332.pdf
'''
from src.constants import *

from collections import defaultdict
from collections import deque
import numpy as np

class GenCmp():
	def __init__(self, dna1, dna2):
		self.dna1 = dna1
		self.dna2 = dna2

class GenCmpRank(GenCmp):
	def __init__(self, dna1, dna2):
		GenCmp.__init__(dna1, dna2)
		self.genMap1 = defaultdict(deque)
		self.genMap2 = defaultdict(deque)
		self.threshold = DISTANCE_THRESHOLD_RANK

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

		self.dna1 = self.dna1[::-1]
		self.dna2 = self.dna2[::-1]

		self.makeGenMaps()
		dist += self.getRankDistance()

		dist /= len(self.dna1) * (len(self.dna1) + 1) + len(self.dna2) * (len(self.dna2) + 1)
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

class GenCmpLev(GenCmp):
	def __init__(self, dna1, dna2):
		GenCmp.__init__(self, dna1, dna2)
		self.threshold = DISTANCE_THRESHOLD_LEV

	def distance(self):
		m = len(self.dna1)+1
		n = len(self.dna2)+1
		dist = np.zeros((m,n)) 	# distance matrix
								# dist[str1][str2]

		for i in range(1,m):
			dist[i][0] = i

		for j in range(1,n):
			dist[0][j] = j

		for j in range(1,n):
			for i in range(1,m):
				cost = 0 if self.dna1[i-1] == self.dna2[j-1] else 1
				dist[i][j] = min(dist[i-1][j] + 1, dist[i][j-1] + 1, dist[i-1][j-1] + cost)

		return dist[m-1][n-1]
