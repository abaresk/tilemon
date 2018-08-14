'''
Tilemon Generator
'''

import random

tideBank = ['t','c','a','g']
seqLength = 200

def generate():
	length = random.randint(seqLength//2,seqLength)
	sequence = ''
	for x in range(length):
		sequence += random.choice(tideBank)
	return sequence

def prettyPrint():
	for i, x in enumerate(seq):
		if i % 2 == 0:
			print(' ', end='')
		print(x, end='')

	print()
	return
