
from playbox.distance import DistanceTest
from playbox.display import *
from playbox.societyTest import SocietyTest

from src.generate import Generator
from src.genome import Genome
from src.tilemon import Tilemon

# dtest = DistanceTest()
# dtest.test()

# generator = Generator()
# tm = Tilemon(generator.genome)
# print(generator.genome)
# print(tm.shape)
# display(tm)

CYCLE_LENGTH = 10
stest = SocietyTest()
for i in range(100):
    stest.runCycles(CYCLE_LENGTH)
