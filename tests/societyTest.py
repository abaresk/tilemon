
from src.society import *

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
