'''
Decode a Tilemon genome
'''
from src.mutate import Mutator

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		return

class Genome():
	def __init__(self, genome=''):
		self.genome = genome
		self.points = set()	# set of points
		self.mutator = Mutator(genome)
		self.update(genome)

	def __len__(self):
		return len(self.genome)

	def reverse(self):
		self.update(self.genome[::-1])
		return

	def decode(self):
		path = [Point(0, 0)]
		for i in range(len(self.genome) // 2):
			x, y = self.genome[2*i], self.genome[2*i+1]
			if x != y:
				if x == 't':
					delta = 1 if y == 'c' else (0 if y == 'a' else -1)
					path.append(Point(path[-1].x + delta, path[-1].y + 1))

				elif x == 'a':
					delta = 1 if y == 't' else (0 if y == 'c' else -1)
					path.append(Point(path[-1].x + 1, path[-1].y + delta))

				elif x == 'c':
					delta = 1 if y == 'a' else (0 if y == 'g' else -1)
					path.append(Point(path[-1].x + delta, path[-1].y - 1))

				elif x == 'g':
					delta = 1 if y == 'a' else (0 if y == 't' else -1)
					path.append(Point(path[-1].x - 1, path[-1].y + delta))
			elif len(path) > 1:
				path.pop()

		return set(path)

	def mutate(self):
		return self.mutator.mutate()

	def update(self, genome):
		self.genome = genome
		self.points = self.decode()
		self.mutator = Mutator(genome)
		return
