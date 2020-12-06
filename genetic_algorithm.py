import random
import numpy

TARGET_FITNESS = 0
MEM_SIZE = 50


class Member:
    """
    __init__
    ---------------------------
    Takes data, mutationProb, lowBound, HighBound to create Member of Population, randomly mutates member
    ---------------------------
    """
    def __init__(self, data=None, mutationProb=0.01, lowBound=-1, highBound=1):
        self.lowBound = lowBound
        self.highBound = highBound
        if data is not None:  # If given data, set data and perform mutation
            self.data = data
            if mutationProb > numpy.random.rand():
                self.mutate()
        else:  # Otherwise generate data for member
            # Create list of MEM_SIZE with val between lower and upper bounds
            value = [self.highBound, self.lowBound]
            self.data = numpy.random.choice(value, size=MEM_SIZE)

    """
    mutate
    ------------------------------------
    Mutates one item in the list at random
    ------------------------------------
    self
    ------------------------------------
    returns:
    ------------------------------------
    USE:
        member.mutate()
    """
    def mutate(self):
        i = numpy.random.randint(len(self.data) - 1)  # Select random index
        # Change random data to value between lower and upper bounds
        if self.data[i] == 1:
            self.data[i] == -1
        else:
            self.data[i] = 1;

    """
       evaluate_fitness
       ------------------------------------------------
       Returns the fitness score of a member, 0 is perfectly fit
       ------------------------------------------------
       self - Access to the Member
       ------------------------------------------------
        returns:
            Difference between target fitness and actual fitness
       ------------------------------------------------
        USE:
            mem.evaluate_fitness()
        OR:
            pop.members[i].evaluate_fitness()
    """
    def evaluate_fitness(self):
        return abs(TARGET_FITNESS - self.sum_data())

    """
    sum_data
    ------------------------------------------------
    Sums the numbers in Member.data to estimate fitness
    ------------------------------------------------
    self
    ------------------------------------------------
    returns:
        dSum - sum of numbers in self.data
    ------------------------------------------------
    USE:
        fit = mem.sum_data()
    """
    def sum_data(self):
        dSum = 0
        for i in self.data:
            dSum += i
        return dSum

    """
    compare_fitness
    --------------------------------------------------
    Compares self member and other member to see which is more fit
    --------------------------------------------------
    self, other
    --------------------------------------------------
    returns:
        True if self is more fit, False otherwise
    --------------------------------------------------
    USE:
        flag = self.compare_fitness(other)
    """
    def compare_fitness(self, other):
        return self.evaluate_fitness() < other.evaluate_fitness()


class Population:
    """
    __init__
    -------------------------------------
    Creates pop with size, mutate probability, list of Members, parent list, child list, fitness history
    onTarget boolean (false if not at target avgFitness), retain (% of generation to keep), randRetain
    """
    def __init__(self, size=10, mutationProb=0.01, retain=0.1, randRetain=0.03, low=-1, high=1):
        self.size = size
        self.mutationProb = mutationProb
        self.retain = retain
        self.randRetain = randRetain
        self.history = []
        self.parents = []
        self.children = []
        self.onTarget = False

        self.members = []
        for i in range(size):  # Create size members with random data, mutationProb chance of mutating
            self.members.append(Member(data=None, mutationProb=self.mutationProb, lowBound=low, highBound=high))

    """
    print_mem_sol
    --------------------------------
    Outputs member with perfect fitness
    --------------------------------
    self
    --------------------------------
    prints, no return
    --------------------------------
    USE:
        pop.print_data()
    """
    def print_data(self):
        self.sort_members()
        print(self.members[0].data)

    """
    avg_fitness
    ----------------------------------------
    self
    ----------------------------------------
    return:
        Average fitness of population
    ----------------------------------------
    Use: avg = pop.avg_fitness()
    """
    def avg_fitness(self, gen=None):
        fitSum = 0
        for i in self.members:
            fitSum += i.evaluate_fitness()

        avgFit = fitSum/self.size
        self.history.append(avgFit)

        if int(round(avgFit)) == 0:
            self.onTarget = True
            print("Member with best fitness: ", end="")
            self.print_data()

        if gen is not None:
            if gen % 10 == 0:  # Check status every 10 generations
                print("Gen #: ", gen, " avgFitness: ", avgFit)

        return avgFit

    """
    select_parents
    ----------------------------------------
    Selects parents of next generation
    ----------------------------------------
    self
    ----------------------------------------
    return:
    ----------------------------------------
    Use: pop.select_parents()
    """
    def select_parents(self):
        # Sort members by fitness (reverse order aka: most fit at index 0)
        self.sort_members()
        # Select top self.retain % of members to keep as parents
        retainParents = self.retain * len(self.members)
        self.parents = self.members[:int(retainParents)]
        # Select other parents randomly to retain
        unfit = self.members[int(retainParents):]
        for i in unfit:
            if self.randRetain > numpy.random.rand():
                self.parents.append(i)

    """
    crossover
    ----------------------------------------
    Generates next generation of children
    ----------------------------------------
    self
    ----------------------------------------
    return:
    ----------------------------------------
    Use: pop.crossover()
    """
    def crossover(self):
        numChildren = self.size - len(self.parents)  # Replace all non-parents
        children = []
        if len(self.parents) > 0:
            while len(children) < numChildren:
                p1 = random.choice(self.parents)
                p2 = random.choice(self.parents)  # Choose 2 random parents
                if p1 != p2:  # Cant be the same parent
                    # Try to implement without use of zip
                    child = self.create_child(p1, p2)
                    children.append(child)
            self.members = self.parents + children

    """
    next_gen
    ----------------------------------------
    Selects parents, generates children, reset parent and child lists
    ----------------------------------------
    self
    ----------------------------------------
    return:
    ----------------------------------------
    Use: pop.next_gen()
    """
    def next_gen(self):
        self.select_parents()
        self.crossover()
        self.parents = []
        self.children = []

    """
    sort_members
    -------------------------------------
    mutates member list to sort by fitness
    -------------------------------------
    self
    -------------------------------------
    returns:
    -------------------------------------
    Use: pop.sort_members()
    """
    def sort_members(self):
        # Sort members by fitness, reverse list so most fit is first
        # Only works with reversed and reverse=True, idk why currently
        self.members = list(reversed(sorted(self.members, key=lambda k: k.evaluate_fitness(), reverse=True)))
        # self.members.sort(key=lambda k: k.evaluate_fitness(), reverse=False)

    """
    create_child
    --------------------------------------------
    Creates 2 children of parents, selects one with best fitness
    --------------------------------------------
    p1 - Member parent 1
    p2 - Member parent 2
    --------------------------------------------
    return:
        Member fittestChild
    --------------------------------------------
    USE:
        newChild = self.create_child(p1, p2)
    """
    @staticmethod
    def create_child(p1, p2):
        dataLen = len(p1.data)
        crossIndex = random.randint(1, dataLen)
        c1 = list(p1.data)
        c2 = list(p2.data)
        for i in range(crossIndex, dataLen):
            c1[i], c2[i] = c2[i], c1[i]

        c1 = Member(c1)
        c2 = Member(c2)
        if c1.compare_fitness(c2):
            return c1
        else:
            return c2
