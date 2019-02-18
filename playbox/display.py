'''
Display a given tilemon
'''

from src.point import *


SCREEN_SIZE = 30

BLANK = '  '
START = 'TT'
BODY = '++'

def display(tilemon):
	points = tilemon.getShape()
	printPoints(points)
	return

def printPoints(points):
	for row in range(SCREEN_SIZE):
		for col in range(SCREEN_SIZE):
			if row == SCREEN_SIZE // 2 and col == SCREEN_SIZE // 2:
				print(START, end='')
			elif (Point(row, col) - Point(SCREEN_SIZE // 2, SCREEN_SIZE // 2)).toTuple() in points:
				print(BODY, end='')
			else:
				print(BLANK, end='')
		print()
