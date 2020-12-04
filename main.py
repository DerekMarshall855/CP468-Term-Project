# IMPORTS
from genetic_algorithm import *
import matplotlib.pyplot as plt

# Max number of breed calls until giving up/settling (Settle at local max/min)
GENS = 5000
PLOT = False

populationSize = 1000
mutateProb = 0.01
retain = 0.1
randRetain = 0.03

pop = Population(size=populationSize,
                 mutationProb=mutateProb,
                 retain=retain,
                 randRetain=randRetain,
                 low=-5.12,
                 high=5.12)

for i in range(GENS):
    pop.avg_fitness(gen=i)
    pop.next_gen()

    if pop.onTarget:
        print("Finished at gen: ", i, ", Avg Population Fitness: ", pop.history[-1])
        break

if PLOT:
    print("Showing fitness history graph")
    plt.plot(numpy.arange(len(pop.history)), pop.history)
    plt.ylabel('Fitness')
    plt.xlabel('Generations')
    plt.title('Fitness - pop_size {} mutate_prob {} retain {} random_retain {}'.format(populationSize,
                                                                                       mutateProb,
                                                                                       retain,
                                                                                       randRetain))
    plt.show()
