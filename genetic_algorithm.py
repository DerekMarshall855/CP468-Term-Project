import random
from math import floor


def evaluate_fitness(chromosome):
    return chromosome[2]
    # function here


class Species:

    def __init__(self, subjects):
        self.individuals = subjects
        self.fitness = [] * len(subjects)
        for i in subjects:
            self.fitness.append(int(evaluate_fitness(i)))

    """
       selection
       ------------------------------------------------
       chooses a  set of parents based on their fitness scores
       ------------------------------------------------
       self - Access to the species of individuals
       ------------------------------------------------
       randomly creates a new list of parents with the intended highest fitness scores
       ------------------------------------------------
       object.selection
    """
    def selection(self):

        totalfitness = 0
        # this for loop calculates the total fitness score in order to calculate an individuals percentage later
        for i in self.fitness:
            totalfitness += i

        selectionList = []
        # this for loop goes throuhg every individual and clones it respective to its fitness in the new list
        for individual in range(len(self.individuals)):
            weight = floor((self.fitness[individual] / totalfitness) * 100)
            # the weight of an individual is how many copies will be made in the list of that individual out of 100
            weightedindividual = [self.individuals[individual]] * weight
            # this for ensures there are no lists in the list, could be lambda
            for i in weightedindividual:
                selectionList.append(i)
        # parents is the list with the now hopefully improved selection of individuals
        # the amount of parents chosen is 2 for testing purposes, unknown what this number should be
        parents = random.sample(selectionList, 2)
        print(parents)
        # parents will mate and create new children to be added to the population

    """
       crossover
       ------------------------------------------------
       matches all options of the parents together and randomly creates new offspring
       ------------------------------------------------
       self - Access to the species of individuals
       parents - the list of parents that will be matched
       ------------------------------------------------
       randomly creates children that will be added to the population
       ------------------------------------------------
       Use: object.crossover(parents)
    """
    def crossover(self, parents):
        children = []
        newindividuals = []

        # the two for loops go trough every possibility of parents and make children with them
        for i in range(len(parents)):
            for j in range(i + 1, len(parents)):
                # split can happen anywhere in the range of the individual
                split = random.randint(0, len(parents[0]))
                print(split)
                x = 0
                # this is where children are made. initially copies of the parents
                # their values get switched according to the split index
                while x <= split and x< len(parents[0]):
                    children = [parents[i], parents[j]]
                    a = children[0][x]
                    children[0][x] = children[1][x]
                    children[1][x] = a
                    x += 1
                # checks if children are already possibly in the new individuals
                for z in children:
                    if z not in newindividuals:
                        newindividuals.append(z)

        print(newindividuals)
        # these are added to self.individuals but for now they are printed

    def mutate(self):
        print("mutating")
        # randomly mutate here
