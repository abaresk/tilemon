from context import src

from src import genome_gen as gg
from src import tilemon as tm

def generateTilemon():
	return tm.Tilemon(dna=gg.generate())