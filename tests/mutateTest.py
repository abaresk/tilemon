from context import src

from src import mutate
from src import genome_gen as gg

for i in range(1000):
	# if i % 150 == 0:
	# 	x = 2
	gen = gg.generate()

	gen1 = mutate.pointMutate(gen)
	gen2 = mutate.insertMutate(gen)
	gen3 = mutate.deleteMutate(gen)
	gen4 = mutate.duplicateMutate(gen)
	gen5 = mutate.bulkDeleteMutate(gen)
	gen6 = mutate.invertMutate(gen)


gen = mutate.mutateGenome(gen)
print(gen)
