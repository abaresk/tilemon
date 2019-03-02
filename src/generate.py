'''
Tilemon Generator
'''
from src.constants import *

import random

seqLength = 100		# start small!!

def generateDNA():
	length = random.randint(seqLength//2,seqLength)
	seq = []
	for x in range(length):
		seq.append(random.choice(ntides))
	return ''.join(seq)
