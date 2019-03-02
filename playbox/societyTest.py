
from src.society import Society
from src.compare import *

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

	def printKinDistanceLev(self, id):
		kin = self.printKin(id)
		return {member: self.printLevDistance(id, member) for member in kin}

	def printKinDistanceRank(self, id):
		kin = self.printKin(id)
		return {member: self.printRankDistance(id, member) for member in kin}

	def printLevDistance(self, id1, id2):
		return GenCmpLev(self.soc.id[id1].dna, self.soc.id[id2].dna).distance()

	def printRankDistance(self, id1, id2):
		return GenCmpRank(self.soc.id[id1].dna, self.soc.id[id2].dna).distance()

	def printGenome(self, id):
		return self.soc.id[id].dna

	def printAllGenomes(self):
		for mon in self.soc.id.values():
			print(mon.dna)
		return

	# Debugging shortucts: remove later -----------------
	def pkl(self):
		return self.printKinLengths()

	def pk(self, id):
		return self.printKin(id)

	def pkdl(self, id):
		return self.printKinDistanceLev(id)

	def pkdr(self, id):
		return self.printKinDistanceRank(id)

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
