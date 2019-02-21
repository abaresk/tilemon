
from src.society import Society

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
				if kinMate not in self.soc.values():
					print('bad - should be dead')
		return

	def printKinLengths(self):
		for monId, mon in self.soc.id.items():
			print(len(mon.kin))
		return

	def printAges(self):
		for monId, mon in self.soc.id.items():
			print(self.calcMonAge(mon))
			if self.calcMonAge(mon) > mon.lifespan:
				print('bad age')
		return
