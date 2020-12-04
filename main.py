# IMPORTS
from genetic_algorithm import *

# Max number of breed calls until giving up/settling (Settle at local max/min)
GENS = 5000

populationSize = 1000
mutateProb = 0.01
retain = 0.1
randRetain = 0.03

pop = Population(size=populationSize, mutationProb=mutateProb, retain=retain, randRetain=randRetain, low=-5.12, high=5.12)

for i in range(GENS):
    pop.avg_fitness(gen=i)
    pop.next_gen()

    if pop.onTarget:
        print("Finished at gen: ", i, ", Avg Population Fitness: ", pop.history[-1])
        break
