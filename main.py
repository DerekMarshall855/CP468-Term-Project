# making sure github link works
from genetic_algorithm import  Species

individuals = [[1,2,3,4,5], [5,4,5,2,1], [3,1,1,2,3]]
parents = [[5,4,5,2,1], [1,2,3,4,5]]

humans = Species(individuals)
#print(humans.individuals[0])
#print(humans.fitness)
#humans.selection()
humans.crossover(parents)