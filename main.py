# IMPORTS
from genetic_algorithm import *
import matplotlib.pyplot as plt

# Max number of breed calls until giving up/settling (Settle at local max/min)
GENS = 200
PLOT = True

populationSize = 200
mutateProb = 0.15
retain = 0.25
randRetain = 0.03
lowBound = -1
highBound = 1

pop = Population(size=populationSize,
                 mutationProb=mutateProb,
                 retain=retain,
                 randRetain=randRetain,
                 low=lowBound,
                 high=highBound)

for i in range(GENS):
    pop.avg_fitness(gen=i)
    pop.next_gen()

    if pop.onTarget:
        print("Finished at gen: ", i, ", Avg Population Fitness: ", pop.history[-1])
        break

if not pop.onTarget:
    print("Algorithm finished without solution, showing graph...")

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
