import random

GEN_MAX = 1000
POP_SIZE = 1000
ELITE = 1
MUTATE_PROB = 0.01
N = 64 

class Population():
    def __init__(self):
        self.ind = [Individual()]*POP_SIZE
        self.nextInd = [Individual()]*POP_SIZE
        for i in range(POP_SIZE):
            self.ind[i] = Individual()
        self.evaluate()

    def alternate(self):
        pass

    def printResult(self):
        pass

    def evaluate(self):
        pass
    
    def select(self):
        pass

    def sort(self, lb, ub):
        pass

class Individual():
    def __init__(self):
        self.chrom = [0]*N
        self.fitness = 0

    def evaluate(self):
        pass

    def crossover(self,p1,p2):
       pass

    def mutate():
        pass
    
if __name__=="__main__":
    pop = Population()
    for i in range(GEN_MAX):
        pop.alternate()
        print("Generation %d: best fitness%f" \
                 .format(i,pop.ind[0].fitness,))
    pop.printResult()
