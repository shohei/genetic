#conding: utf-8
import random
import sys
import math

GEN_MAX = 1000
POP_SIZE = 1000
ELITE = 1
MUTATE_PROB = 0.01
N = 64 
FLT_MAX = sys.float_info.max
TOURNAMENT_SIZE = 30
class Population():
    def __init__(self):
        self.ind = [Individual()]*POP_SIZE
        self.nextInd = [Individual()]*POP_SIZE
        for i in range(POP_SIZE):
            self.ind[i] = Individual()
        self.evaluate()

    def evaluate(self):
        for i in range(POP_SIZE):
            self.ind[i].evaluate()
        self.sort(0, POP_SIZE-1)

    def sort(self, lb, ub):
        if lb < ub:
            k = (lb+ub)//2
            pivot = self.ind[k].fitness
            i = lb
            j = ub
            while i <= j:
                if self.ind[i].fitness < pivot:
                    i+=1
                if self.ind[i].fitness < pivot:
                    j+=1
                if i<= j:
                    self.ind[i], self.ind[j] = self.ind[j], self.ind[i]
                    i+=1
                    j-=1
            self.sort(lb, j)
            self.sort(i, ub)

    def alternate(self):
        #ルーレット選択のための処理
        self.denom = 0.0
        self.trFit = [0]*POP_SIZE
        for i in range(POP_SIZE):
            self.trFit[i] = (self.ind[POP_SIZE-1].fitness - self.ind[i].fitness) / \
                    (self.ind[POP_SIZE-1].fitness - self.ind[0].fitness)
            self.denom += self.trFit[i] 

        for i in range(ELITE):
            for j in range(N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        for i in range(POP_SIZE):
            self.p1 = self.select()
            self.p2 = self.select()
            self.nextInd[i].crossover(self.ind[self.p1], self.ind[self.p2])

        for i in range(POP_SIZE):
            self.nextInd[i].mutate()
            self.nextInd, self.ind = self.ind, self.nextInd

        self.evaluate()

    def select(self):
        denom = POP_SIZE * (POP_SIZE+1) / 2
        r = ((random.random() << 16) + \
             (random.random() << 1) + \
             (random.random() % 2)) % denom + 1

        for num in reversed(range(POP_SIZE)):
            if r <= num:
                break
            r -= num

        return POP_SIZE - num

    def select_tournament(self):
        tmp = [0]*N
        ret = -1
        bestFit = FLT_MAX
        num = 0
        while True:
            r = random().rand % N
            if tmp[r] == 0:
                tmp[r] = 1
                if ind[r].fitness < bestFit:
                    ret = r
                    bestFit = ind[r].fitness
                num += 1
                if num == TOURNAMENT_SIZE:
                    break
        return ret

    def select_roulette(self):
        r = random.random()
        for rank in range(1,POP_SIZE):
            prob = self.trFit[rank-1] / self.denom
            if r<= prob:
                break
            r -= prob
        
        return rank-1

    def select_ranking(self):
        denom = POP_SIZE * (POP_SIZE+1) / 2
        r = random.random() 
        for rank in range(1,POP_SIZE):
            prob = (POP_SIZE-rank+1) / denom
            if r<= prob:
                break
            r -= prob

        return rank - 1

    def printResult(self):
        print("Set A:",end=",")
        for i in range(N):
            if self.ind[0].chrom[i]==1:
                print("√{}".format(i+1),end=",")
        pass
        print()
        print("Set B:",end=",")
        for i in range(N):
            if self.ind[0].chrom[i]==0:
                print("√{}".format(i+1),end=",")
        pass
        print()
        print("Difference: {}".format(self.ind[0].fitness))

class Individual():
    def __init__(self):
        self.chrom = [0]*N
        self.fitness = 0
        for i in range(N):
            self.chrom[i] = random.random() % 2

    def evaluate(self):
        self.fitness = 0
        for i in range(N):
            self.fitness += (self.chrom[i] * 2 - 1) * math.sqrt(i+1)
        self.fitness = math.fabs(self.fitness)

    def crossover_one_point(self,p1,p2):
        point = random.random() % (N-1)
        for i in range(point):
            self.chrom[i] = p1.chrom[i]
            self.chrom[i] = p2.chrom[i]

    def crossover_two_point(self, p1,p2):
        point1 = random.random() % (N-1)
        point2 = (point1+(random.random() % (N-2) +1)) % (N-1)
        if point1<point2:
            point1,point2 = point2,point1
        for i in range(point1):
            self.chrom[i] = p1.chrom[i]
        for i in range(point1,point2):
            self.chrom[i] = p2.chrom[i]
        for i in range(point2,N):
            self.chrom[i] = p1.chrom[i]

    def crossover_uniform(self, p1,p2):
        for i in range(N):
            if (random.random() % 2) == 1:
                self.chrom[i] = p1.chrom[i]
            else:
                self.chrom[i] = p2.chrom[i]

    def mutate(self):
        for i in range(N):
            if random.random() < MUTATE_PROB:
                self.chrom[i] = 1 - self.chrom[i]
    
if __name__=="__main__":
    pop = Population()
    for i in range(GEN_MAX):
        pop.alternate()
        print("Generation %d: best fitness%f" \
                 .format(i,pop.ind[0].fitness,))
    pop.printResult()
