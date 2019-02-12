'''
Compare the genomes of different tilemons
	* Uses Rank Distance to compute the distance between two genome strings
	* This algorithm runs linearly, as opposed to standard Levenshtein Distance
	* Reference: https://pdfs.semanticscholar.org/3208/ba4168dbd5b28669e66f427f94ea5f95d332.pdf
'''
from collections import defaultdict
from collections import deque

# Comment this out when removing levDistance
import numpy as np

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

	def initDict(self, genome):
		dict = defaultdict(deque)
		for i, ntide in enumerate(genome.genome):
			dict[ntide].append(i)
		return dict

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

	# TODO: this should be deleted
	def levDistance(self):
		m = len(self.genome1)+1
		n = len(self.genome2)+1
		dist = np.zeros((m,n)) 	# distance matrix
								# dist[self.genome1][self.genome2]

		for i in range(1,m):
			dist[i][0] = i

		for j in range(1,n):
			dist[0][j] = j

		for j in range(1,n):
			for i in range(1,m):
				cost = 0 if self.genome1.genome[i-1] == self.genome2.genome[j-1] else 1
				dist[i][j] = min(dist[i-1][j] + 1, dist[i][j-1] + 1, dist[i-1][j-1] + cost)

		return dist[m-1][n-1]

# # Test
# a = 'tttagcttgtttaagacgttagcgtatcccttttaacaagccgcaaggtcgaacgcatcctcgttctgacttgcccttgagattgtaattatgtatgtgtgctagctgcctaaatgccgaggcacatgctcgagttgactccatcaaggttatgcactttacgaacgcgaggccttttacgtaagggtttgaagactcacaaagactgaggcttagtctacctttccactgcgcggctgaggtggctcgagcatcttgcaagagagtgtggcaggtgtcgatcggttagatccaagagcctagatctactggaatcgtcgcgaatccggttacctcacctccgttacacgccagtggaagagactaagaaacagcgtcaatcacgcccggtgtcatctctctcaccgcgatcggggtgctcttaataatcaaatcacggcggaaggggcaggactggttcgtcgccgaacggaagcaccattcggaaataatcttcgtgaacatgacaccagaccatcgtcgatggcctactacgccgtaatatcttcaaactgcctcacacagacccataacgtcttggtaataaactttagactcttaacaaagggaatatatttaggaacgctttccggtttcaagtaacggacgatagggctcaatacaaccgtacccccccggcttcgcgatgggtattaagcagcgtttatgcgctgactaattagtagttccgctcgatgcatagccagacacggaaaatcgattaggctatgcgatgatcgtcacggcggttaataggctgcctacgcttggaagcctcctggtcccctccgtccttctgaggtgtttcgattagctcgcattatacaggaaccgtcatcgataccatccgttcaccggacgtcgacgaaattagcaggaagacggctaagcttccacacagggggctcgatgtcggggtgtcttcgggcgttcatgtcgtttatcgagtaccgactcatttcgagtaccacagaatctttaaggcttggcctacgtatccctcacactcttacattatgaggccctcgcacaaagtgggtccctcaaggcatatagggccggcaaaacaatatcccacagcgtctcaccgctccagggtaatgtacttctctgctacagggttgcttttccaaaagattaaggatgcgacgttctgtcgagtcagaccattacgtcaggcagcctcatgcgcattctgccaacataccataagacctcgattcgctattgaagggcgtactccggaaagaatgtacaaaccgaaggttctgggcataagaccgcaattgctaagtaaccacgtcccctactattccatatatggtcgtcataacatgttgctcgccacgacaacgttttgaagccggggtctaagccatcgtacgacggagagctcttgaacgtgcggacatatgggcctttgtggaggaagccctgaggcagaccgattactgcacaccgcaattagacctcgcgcggcgtatcgttcatgcgtgtcacctaaagaccaaaggcgacgctgcaagtcggtgggaagaagtggcgctgcgcttttggaaccaccttaatcgtgagtgacacttgccggaacaaaactctgccaggccaccccttacacctgctgcgggattccaccgtcagagattatacatataaacttatactaacaatcatccctctcgggctcctgtgacataagctatttcatagtggt'
# b = 'cgtcatcgataccatccgttcaccggacgtcgacgaaattagcaggaagacggctaagcttccacacagggggctcgatgtcggggtgtcttcgggcgttcatgtcgtttatcgagtaccgactcatttcgagtaccacagaatctttaaggcttggcctacgtatccctcacactcttacattatgaggccctcgcacaaagtgggtccctcaaggcatatagggccggcaaaacaatatcccacagcgtctcaccgctccagggtaatgtacttctctgctacagggttgcttttccaaaagattaaggatgcgacgttctgtcgagtcagaccattacgtcaggcagcctcatgcgcattctgccaacataccataagacctcgattcgctattgaagggcgtactccggaaagaatgtacaaaccgaaggttctgggcataagaccgcaattgctaagtaaccacgtcccctactattccatatatggtcgtcataacatgttgctcgccacgacaacgttttgaagccggggtctaagccatcgtacgacggagagctcttgaacgtgcggacatatgggcctttgtggaggaagccctgaggcagaccgattactgcacaccgcaattagacctcgcgcggcgtatcgttcatgcgtgtcacctaaagaccaaaggcgacgctgcaagtcggtgggaagaagtggcgctgcgcttttggaaccaccttaatcgtgagtgacacttgccggaacaaaactctgccaggccaccccttacacctgctgcgggattccaccgtcagagattatacatataaacttatactaacaatcatccctctcgggctcctgtgacataagctatttcatagtggttttagcttgtttaagacgttagcgtatcccttttaacaagccgcaaggtcgaacgcatcctcgttctgacttgcccttgagattgtaattatgtatgtgtgctagctgcctaaatgccgaggcacatgctcgagttgactccatcaaggttatgcactttacgaacgcgaggccttttacgtaagggtttgaagactcacaaagactgaggcttagtctacctttccactgcgcggctgaggtggctcgagcatcttgcaagagagtgtggcaggtgtcgatcggttagatccaagagcctagatctactggaatcgtcgcgaatccggttacctcacctccgttacacgccagtggaagagactaagaaacagcgtcaatcacgcccggtgtcatctctctcaccgcgatcggggtgctcttaataatcaaatcacggcggaaggggcaggactggttcgtcgccgaacggaagcaccattcggaaataatcttcgtgaacatgacaccagaccatcgtcgatggcctactacgccgtaatatcttcaaactgcctcacacagacccataacgtcttggtaataaactttagactcttaacaaagggaatatatttaggaacgctttccggtttcaagtaacggacgatagggctcaatacaaccgtacccccccggcttcgcgatgggtattaagcagcgtttatgcgctgactaattagtagttccgctcgatgcatagccagacacggaaaatcgattaggctatgcgatgatcgtcacggcggttaataggctgcctacgcttggaagcctcctggtcccctccgtccttctgaggtgtttcgattagctcgcattatacaggaac'
#
# d = GenomeCompare(a,b)
# print(d.distance())
