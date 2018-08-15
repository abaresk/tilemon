from context import src

from tilemon_generate import *
from src.society import *

t1 = generateTilemon()

soc = Society()
og = list(soc.id.keys())

soc.addTilemon(og[0])

for memberId in list(soc.id.keys()):
	soc.addTilemon(memberId)

t2 = soc.generateTilemon()