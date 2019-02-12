'''
Decode a Tilemon genome
'''
from src.mutate import Mutator

class Genome():
	def __init__(self, dna=''):
		self.dna = dna
		self.mutator = Mutator(genome)

	def __len__(self):
		return len(self.dna)

	def reverse(self):
		self.update(self.dna[::-1])
		return

	def mutate(self):
		return self.mutator.mutate()

	def update(self, dna):
		self.dna = dna
		self.mutator = Mutator(genome)
		return
