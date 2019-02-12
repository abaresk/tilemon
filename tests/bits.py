from context import src

from tilemon_generate import *
from src.genome_gen import *
from src.genome_compare import *


import math
import timeit


a = generate()
b = generate()


genVal = {'t':0, 'c':1, 'a':2, 'g':3}	# blank space is 4


def gen2num(genome):
	lgenome = len(genome)
	num = 4		# start with blank space

	for x in genome:
		num *= 8
		num += genVal[x]

	return num


def bitDistanceAux(x, y):	# input is two gene numbers
	z = x ^ y
	count = 0

	# Create mask to OR the even and odd bits
	mask = 0
	while z > 0:
		mask <<= 3
		mask += 4
		z >>= 3

	z = x ^ y
	result = (z & mask) | ((z & (mask>>1)) << 1) | ((z & (mask>>2)) << 2)

	# Count number of ones
	while result > 0:
		result &= result-1
		count += 1

	return count


def bitDistance(x, y):	# input is two gene numbers
	if y > x:
		x, y = y, x

	# Move y until it has same number of bits as x (fill in with blank space '4')
	logx = math.floor(math.log(x)/math.log(8))

	while logx > math.floor(math.log(y)/math.log(8)):
		y = (y << 3) | 4

	
	mn = bitDistanceAux(x,y)	# minimum distance
	while y % 8 > 3:	# until blank spaces are gone
		y >>= 3
		dist = bitDistanceAux(x, y)
		mn = dist if dist < mn else mn

	return mn


x = gen2num(a)
y = gen2num(b)

# distLev = levDistance(a,b)
distBit = bitDistance(x,y)


# Timing
levTime = timeit.timeit('levDistance(a,b)', globals=globals(), number=25)
bitTime = timeit.timeit('bitDistance(x,y)', globals=globals(), number=25)
print(levTime, bitTime)

