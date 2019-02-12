
from tilemon_generate import *
from src.society import *

# Write function to check that kin are all alive
def allAlive(soc):
	for memberId in list(soc.id):
		for kinId in soc.id2kin[memberId]:
			if kinId not in soc.id:
				print('bad')
	return

def printKinLengths(soc):
	for memberId in list(soc.id):
		print(len(soc.id2kin[memberId]))
	return

def printAges(soc):
	for memberId in list(soc.id):
		print(soc.id[memberId].age)
		# if soc.id[memberId].age > soc.id[memberId].actualLifeSpan:
		# 	print('bad age')



soc = Society()
og = list(soc.id.keys())

# soc.addTilemon(og[0])
c = 250
for x in range(10000):
	if (x+1)%c == 0:
		c = c
		allAlive(soc)
		print(len(soc.id))
		printAges(soc)
	soc.turnCycle()
	# if len(soc.id) == 1:
	print(x)

print()
# for memberId in list(soc.id.keys()):
# 	soc.addTilemon(memberId)
