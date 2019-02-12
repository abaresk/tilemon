'''
Display a given tilemon
'''

import copy

from genome_gen import generate
from genome_decode import decodeGenome


SCREEN_SIZE = 20

BLANK = '  '
START = 'TT'
BODY = '++'


### GRAPHING

def getOrigin():
	return SCREEN_SIZE // 2

def centerPoints(pointsZip):
	zipped = zip(pointsZip[0], pointsZip[1])
	points = []
	origin = getOrigin()


	for x, y in zipped:
		points.append((x + origin, y + origin))

	return points


def printGraph(pointsZip):
	points = centerPoints(pointsZip)
	origin = getOrigin()

	for row in reversed(range(SCREEN_SIZE)):
		for col in range(SCREEN_SIZE):
			if row == origin and col == origin:
				print(START, end='')
			elif (col,row) in points:
				print(BODY, end='')
			else:
				print(BLANK, end='')
		print()

	return


# Main
seq = generate()
print(seq)

zipped = decodeGenome(seq)

zipcp = copy.deepcopy(zipped)

print(list(zip(zipcp[0], zipcp[1])))
# print(list(centerPoints(zipped)))

printGraph(zipped)
