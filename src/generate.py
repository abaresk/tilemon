'''
Tilemon Generator
'''
from src.constants import *
from src.genome import Genome

import random

seqLength = 500		# start small!!

class Generator():
	def __init__(self):
		self.genome = self.generate()

	def generate(self):
		length = random.randint(seqLength//2,seqLength)
		seq = []
		for x in range(length):
			seq.append(random.choice(ntides))
		return Genome(''.join(seq))

	def update(self):
		self.genome = self.generate()
		return
