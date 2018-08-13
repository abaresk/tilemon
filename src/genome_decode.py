'''
Decode a Tilemon genome
'''

### DECODING
# Return a list of points to be marked in as the body
def pairify(genomeStr):
	x = []
	y = []
	for i, c in enumerate(genomeStr):
		y.append(c) if i % 2 else x.append(c)
	return zip(x,y)

def removeDups(zipped):
	d = {}
	x = []
	y = []
	zip1,zip2 = zipped

	for xx,yy in zip(zip1,zip2):
		d[(xx,yy)] = True

	for tup in d.keys():
		x.append(tup[0])
		y.append(tup[1])

	return [x,y]


def decodeGenome(genomeStr):
	xPoints = [0]
	yPoints = [0]
	
	xPath = [0]
	yPath = [0]

	genomeZip = pairify(genomeStr)

	for x, y in genomeZip:
		if x == y:
			if len(xPath) > 1:
				xPath.pop()
				yPath.pop()
		else:
			if x == 't':
				delta = 1 if y == 'c' else (0 if y == 'a' else -1)
				xPath.append(xPath[-1] + delta)
				yPath.append(yPath[-1] + 1)

			elif x == 'a':
				delta = 1 if y == 't' else (0 if y == 'c' else -1)
				xPath.append(xPath[-1] + 1)
				yPath.append(yPath[-1] + delta)

			elif x == 'c':
				delta = 1 if y == 'a' else (0 if y == 'g' else -1)
				xPath.append(xPath[-1] + delta)
				yPath.append(yPath[-1] - 1)

			elif x == 'g':
				delta = 1 if y == 'a' else (0 if y == 't' else -1)
				xPath.append(xPath[-1] - 1)
				yPath.append(yPath[-1] + delta)

			xPoints.append(xPath[-1])
			yPoints.append(yPath[-1])
	
	return removeDups([xPoints,yPoints])
