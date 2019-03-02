#
# from playbox.distance import DistanceTest
# from playbox.display import *
from playbox.societyTest import SocietyTest

from src.generate import *
from src.tilemon import Tilemon

# dtest = DistanceTest()
# dtest.test()

# generator = Generator()
# tm = Tilemon(generator.genome)
# print(generator.genome)
# print(tm.shape)
# display(tm)

CYCLE_LENGTH = 1000    # make like 50
stest = SocietyTest()
while input('Continue? ') != 'n':
    stest.runCycles(CYCLE_LENGTH)
    stest.allAlive()
    stest.printKinLengths()
stest.printAllGenomes()
