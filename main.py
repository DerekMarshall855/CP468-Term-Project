# IMPORTS
from genetic_algorithm import *
import matplotlib.pyplot as plt

# Max number of breed calls until giving up/settling (Settle at local max/min)
GENS = 300
PLOT = True

populationSize = 20000
mutateProb = 0.05
retain = 0.15
randRetain = 0.03
lowBound = -1
highBound = 1
benchmark = 4  # 1 - DeJongs 2 - Rosenbrocks 3 - Himmelblaus 4 - size25(memSize >=51) 5 - size27(memSize >= 55)
memSize = 51  # Usually 20 or lower for benchmark 1-3, 4 - 51, 5 - 55, 6 - 59, 7 - 63, 8 - 67
binary = True  # If True low and high bound are binary (Each value is one or the other), else not binary

pop = Population(size=populationSize,
                 mutationProb=mutateProb,
                 retain=retain,
                 randRetain=randRetain,
                 low=lowBound,
                 high=highBound,
                 of=benchmark,
                 memSize=memSize,
                 binary=binary)

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
