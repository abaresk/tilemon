
from src.generate import Generator
from src.compare import GenomeCompare

import matplotlib.pyplot as plt

NUM_TRIALS = 100

class DistanceTest():
    def __init__(self):
        self.datapoints = [[],[]]
        self.gen1 = Generator()
        self.gen2 = Generator()

    def fillDataPoints(self):
        self.datapoints = [[], []]
        for i in range(NUM_TRIALS):
            self.gen1.update()
            self.gen2.update()
            cmp = GenomeCompare(self.gen1.genome, self.gen2.genome)
            dist = cmp.levDistance()
            rank = cmp.distance()

            self.datapoints[0].append(dist)
            self.datapoints[1].append(rank)
        return

    def plot(self):
        plt.plot(self.datapoints[0], self.datapoints[1], 'o')
        plt.show()
        return

    def test(self):
        self.fillDataPoints()
        self.plot()
        return
