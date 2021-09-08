import random 
import numpy as np
import sys
import pdb
import matplotlib.pyplot as plt

wvs = [(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)]
ws = [wv[0] for wv in wvs]
vs = [wv[1] for wv in wvs]
MAX_WEIGHT = 10
GEN_MAX = 1000
#POP_SIZE = 1000
POP_SIZE = 30 
ELITE = 1
MUTATE_PROB = 0.01
N = 6
FLT_MAX = sys.float_info.max
TOURNAMENT_SIZE = 30
RAND_MAX = 2**16
class Population():
    def __init__(self):
        self.ind = [0]*POP_SIZE
        self.nextInd = [0]*POP_SIZE
        for i in range(POP_SIZE):
            self.ind[i] = Individual()
            self.nextInd[i] = Individual()

    def alternate(self):
        for i in range(ELITE):
            for j in range(N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        for i in range(ELITE,POP_SIZE):
            p1 = self.select()
            p2 = self.select()
            self.nextInd[i].crossover(self.ind[p1], self.ind[p2])

        for i in range(POP_SIZE):
            self.nextInd[i].mutate()
        
        self.nextInd, self.ind = self.ind, self.nextInd

        self.evaluate()

    def evaluate(self):
        for i in range(POP_SIZE):
            self.ind[i].evaluate()
        fitnesses = np.array([ind.fitness for ind in self.ind])
        orders = (-1*fitnesses).argsort().argsort()
        tmp = self.ind.copy()
        for i,order in enumerate(orders):
            self.ind[order] = tmp[i] 

        chroms = [ind.chrom for ind in self.ind]
        chroms_set =  set(tuple(row) for row in chroms)
        self.number_of_solutions = len(chroms_set)

    def select(self):
        fitnesses = [ind.fitness for ind in self.ind]
        ranks = np.argsort(fitnesses)
        indices = list(range(N))
        rankProb = [0]*N
        for i in range(N):
            rankProb[i] = (POP_SIZE-ranks[i]+1)/(0.5*POP_SIZE*(POP_SIZE+1))
        res = random.choices(population=indices, weights=rankProb,k=1)
        return res[0]

    def printResult(self):
        pass


class Individual():
    def __init__(self):
        self.fitness = 0.0
        self.chrom = [random.randint(0,RAND_MAX) % 2 for i in range(N)] 

    def evaluate(self):
        self.fitness = np.dot(np.array(self.chrom),np.array(vs))
        total_weight = np.dot(np.array(self.chrom),np.array(ws))
        if total_weight > MAX_WEIGHT:
            self.fitness = 0.0

    def crossover(self, parent1, parent2):
        point = random.randint(0,RAND_MAX) % (N-1)
        for i in range(point):
            self.chrom[i] = parent1.chrom[i]
        for i in range(point, N):
            self.chrom[i] = parent2.chrom[i]

    def mutate(self):
        for i in range(N):
            if random.random() < MUTATE_PROB:
                self.chrom[i] = 1 - self.chrom[i]

if __name__=="__main__":
    try:
        pop = Population()
        best = -1 
        solution = []
        fig, ax = plt.subplots(1, 1)
        lines, = ax.plot(0, 0)
        x = []
        y = []
        for i in range(GEN_MAX):
            pop.alternate()
            print("Generation: {}, Best fitness: {}, solution: {}, # of solution: {}".format( \
                        i,pop.ind[0].fitness,pop.ind[0].chrom,pop.number_of_solutions))
            if pop.ind[0].fitness > best:
                best = pop.ind[0].fitness
                solution = pop.ind[0].chrom
            x.append(i)
            y.append(pop.ind[0].fitness)
            lines.set_data(x, y)
            ax.set_xlim((min(x), max(x)))
            ax.set_ylim((min(y), max(y)))
            # ax.set_yscale('log')
            plt.pause(.01)
        print('Result')
        print("best: {}, solution: {}".format(best, solution))
        exit()
    except KeyboardInterrupt:
        print('Result')
        print("best: {}, solution: {}".format(best, solution))
        exit()

