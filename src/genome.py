'''
Decode a Tilemon genome
'''

class Genome():
	def __init__(self, dna=''):
		self.dna = dna
		return

	def __len__(self):
		return len(self.dna)

	def __repr__(self):
		return self.dna

	def reverse(self):
		self.update(self.dna[::-1])
		return

	def update(self, dna):
		self.dna = dna
		return
