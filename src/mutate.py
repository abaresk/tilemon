'''
Functions for genome mutation
'''

import random

nucleotideBank = ['t','c','a','g']


### Mutations

# Single-nucleotide swap
def pointMutate(genome):
	i = random.randint(0, len(genome)-1)
	return genome[:i] + random.choice(nucleotideBank) + genome[i+1:]

def insertMutate(genome):
	i = random.randint(0, len(genome))
	return genome[:i] + random.choice(nucleotideBank) + genome[i:]

def deleteMutate(genome):
	i = random.randint(0, len(genome)-1)
	return genome[:i] + genome[i+1:]

# duplicate up to 50%
def duplicateMutate(genome):
	genlen = len(genome)
	maxlen = genlen // 2
	duplen = random.randint(1,maxlen)
	i = random.randint(0, genlen)

	if random.random() < 0.5:
		endpoint = i + duplen if i + duplen < genlen else genlen
		substr = genome[i:endpoint]
	else:
		endpoint = i - duplen if i - duplen > 0 else 0
		substr = genome[endpoint:i]

	return genome[:i] + substr + genome[i:]

# delete up to 25%
def bulkDeleteMutate(genome):
	genlen = len(genome)
	maxlen = genlen // 4
	dellen = random.randint(1,maxlen)
	i = random.randint(0, genlen)

	if random.random() < 0.5:
		endpoint = i + dellen if i + dellen < genlen else genlen
		return genome[:i] + genome[endpoint:]
	else:
		endpoint = i - dellen if i - dellen > 0 else 0
		return genome[:endpoint] + genome[i:]

# swap two sections of a genome, each no larger than 25%
def invertMutate(genome):
	genlen = len(genome)
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

		genome = genome[:i] + genome[j:rightend] + genome[leftend:j] + genome[i:leftend] + genome[rightend:]

	return genome


def mutateGenome(genome):
	mutationTypes = [pointMutate, insertMutate, deleteMutate, duplicateMutate, bulkDeleteMutate, invertMutate]
	return random.choice(mutationTypes)(genome)
