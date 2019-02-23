'''
Functions for dna mutation
'''
from src.constants import *

import random

### Mutations
class Mutator():
	def __init__(self, dna):
		self.dna = dna

	# Single-nucleotide swap
	def pointMutate(self):
		i = random.randint(0, len(self.dna)-1)
		return self.dna[:i] + random.choice(ntides) + self.dna[i+1:]

	def insertMutate(self):
		i = random.randint(0, len(self.dna))
		return self.dna[:i] + random.choice(ntides) + self.dna[i:]

	def deleteMutate(self):
		if len(self.dna) > 1:
			i = random.randint(0, len(self.dna)-1)
			return self.dna[:i] + self.dna[i+1:]
		else:
			return self.dna

	# duplicate up to 50%
	def duplicateMutate(self):
		genlen = len(self.dna)
		maxlen = genlen // 2
		duplen = random.randint(1,maxlen)
		i = random.randint(0, genlen)

		if random.random() < 0.5:
			endpoint = i + duplen if i + duplen < genlen else genlen
			substr = self.dna[i:endpoint]
		else:
			endpoint = i - duplen if i - duplen > 0 else 0
			substr = self.dna[endpoint:i]

		return self.dna[:i] + substr + self.dna[i:]

	# delete up to 25%
	def bulkDeleteMutate(self):
		genlen = len(self.dna)
		maxlen = genlen // 4
		dellen = random.randint(1,maxlen)
		i = random.randint(0, genlen)

		if random.random() < 0.5:
			endpoint = i + dellen if i + dellen < genlen else genlen
			return self.dna[:i] + self.dna[endpoint:]
		else:
			endpoint = i - dellen if i - dellen > 0 else 0
			return self.dna[:endpoint] + self.dna[i:]

	# swap two sections of a dna, each no larger than 25%
	def invertMutate(self):
		genlen = len(self.dna)
		maxlen = genlen // 4

		# i is starting point for left; j is starting point for right
		i = random.randint(0, genlen)
		j = random.randint(i, genlen)

		# if there is something to swap
		if i != j:
			leftlen = random.randint(1, maxlen)
			rightlen = random.randint(1, maxlen)

			leftend = i + leftlen if i + leftlen < j else j
			rightend = j + rightlen if j + rightlen < genlen else genlen

			self.dna = self.dna[:i] + self.dna[j:rightend] + self.dna[leftend:j] + self.dna[i:leftend] + self.dna[rightend:]

		return self.dna

	def mutate(self):
		fxns = [self.pointMutate, self.insertMutate, self.deleteMutate, self.duplicateMutate, self.bulkDeleteMutate, self.invertMutate]
		fxn = random.choice(fxns)
		# print(fxn) # for debugging
		return fxn()
