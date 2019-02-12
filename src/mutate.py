'''
Functions for genome mutation
'''
from src.constants import *

import random

### Mutations
class Mutator():
	def __init__(self, genome):
		self.genome = genome

	# Single-nucleotide swap
	def pointMutate(self):
		i = random.randint(0, len(self.genome)-1)
		return self.genome[:i] + random.choice(ntides) + self.genome[i+1:]

	def insertMutate(self):
		i = random.randint(0, len(self.genome))
		return self.genome[:i] + random.choice(ntides) + self.genome[i:]

	def deleteMutate(self):
		if len(self.genome) > 1:
			i = random.randint(0, len(self.genome)-1)
			return self.genome[:i] + self.genome[i+1:]
		else:
			return self.genome

	# duplicate up to 50%
	def duplicateMutate(self):
		genlen = len(self.genome)
		maxlen = genlen // 2
		duplen = random.randint(1,maxlen)
		i = random.randint(0, genlen)

		if random.random() < 0.5:
			endpoint = i + duplen if i + duplen < genlen else genlen
			substr = self.genome[i:endpoint]
		else:
			endpoint = i - duplen if i - duplen > 0 else 0
			substr = self.genome[endpoint:i]

		return self.genome[:i] + substr + self.genome[i:]

	# delete up to 25%
	def bulkDeleteMutate(self):
		genlen = len(self.genome)
		maxlen = genlen // 4
		dellen = random.randint(1,maxlen)
		i = random.randint(0, genlen)

		if random.random() < 0.5:
			endpoint = i + dellen if i + dellen < genlen else genlen
			return self.genome[:i] + self.genome[endpoint:]
		else:
			endpoint = i - dellen if i - dellen > 0 else 0
			return self.genome[:endpoint] + self.genome[i:]

	# swap two sections of a genome, each no larger than 25%
	def invertMutate(self):
		genlen = len(self.genome)
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

			genome = self.genome[:i] + self.genome[j:rightend] + self.genome[leftend:j] + self.genome[i:leftend] + self.genome[rightend:]

		return genome


	def mutate(self):
		fxns = [self.pointMutate, self.insertMutate, self.deleteMutate, self.duplicateMutate, self.bulkDeleteMutate, self.invertMutate]
		fxn = random.choice(fxns)
		print(fxn) # for debugging
		return fxn(self.genome)
