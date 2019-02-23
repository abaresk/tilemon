
from src.society import Society
from src.compare import GenomeCompare as Gencmp

class SocietyTest():
	def __init__(self):
		self.soc = Society()
		return

	def runCycles(self, cycles):
		for i in range(cycles):
			self.soc.advanceCycle()
		return

	def allAlive(self):
		for monId, mon in self.soc.id.items():
			for kinMate in mon.kin:
				if kinMate not in self.soc.id.values():
					print('bad - should be dead')
		return

	def printKinLengths(self):
		for monId, mon in self.soc.id.items():
			print(str(monId) + ': \t' + str(len(mon.kin)))
		return

	def printKin(self, id):
		return [key for member in self.soc.id[id].kin for key, val in self.soc.id.items() if val == member]

	def printKinDistance(self, id):
		kin = self.printKin(id)
		return {member: self.printGenomeDistance(id, member) for member in kin}

	def printGenomeDistance(self, id1, id2):
		return Gencmp(self.soc.id[id1].genome, self.soc.id[id2].genome).distance()

	def printGenome(self, id):
		return self.soc.id[id].genome

	def printAllGenomes(self):
		for mon in self.soc.id.values():
			print(mon.genome)
		return

	# Debugging shortucts: remove later -----------------
	def pkl(self):
		return self.printKinLengths()

	def pk(self, id):
		return self.printKin(id)

	def pkd(self, id):
		return self.printKinDistance(id)

	def pgd(self, id1, id2):
		return self.printGenomeDistance(id1, id2)

	def pg(self, id):
		return self.printGenome(id)

	def pga(self):
		return self.printAllGenomes()
	# ---------------------------------------------------

	def printAges(self):
		for monId, mon in self.soc.id.items():
			print(self.soc.calcMonAge(mon))
			if self.soc.calcMonAge(mon) > mon.lifespan:
				print('bad age')
		return
