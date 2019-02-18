
from playbox.distance import DistanceTest
from playbox.display import *

from src.generate import Generator
from src.genome import Genome
from src.tilemon import Tilemon

# dtest = DistanceTest()
# dtest.test()

generator = Generator()
tm = Tilemon(generator.genome)
print(generator.genome)
print(tm.shape)
display(tm)
