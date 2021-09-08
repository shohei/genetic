# coding:utf-8
import random
from variables import POP_SIZE, ELITE 
from variables import N, FLT_MAX, TOURNAMENT_SIZE, RAND_MAX 
from individual import Individual
import pdb
import numpy as np

class Population():
    def __init__(self):
        self.ind = [Individual()]*POP_SIZE
        self.nextInd = [Individual()]*POP_SIZE
        for i in range(POP_SIZE):
            self.ind[i] = Individual()
            self.nextInd[i] = Individual()
        self.evaluate()

    def evaluate(self):
        for i in range(POP_SIZE):
            self.ind[i].evaluate()
        fitnesses = np.array([ind.fitness for ind in self.ind])
        orders = fitnesses.argsort()
        ranks = orders.argsort()
        tmp = self.ind.copy()
        for i,rank in enumerate(ranks):
            self.ind[rank] = tmp[i]
        # self.sort(0, POP_SIZE-1)

    def sort(self, lb, ub):
        if lb < ub:
            k = (lb+ub)//2
            pivot = self.ind[k].fitness
            i = lb
            j = ub
            while i <= j:
                if self.ind[i].fitness < pivot:
                    i+=1
                if self.ind[j].fitness > pivot:
                    j-=1
                if i<= j:
                    self.ind[i], self.ind[j] = self.ind[j], self.ind[i]
                    i+=1
                    j-=1

            self.sort(lb, j)
            self.sort(i, ub)

    def alternate(self):
        #ルーレット選択のための処理
        # self.denom = 0.0
        # self.trFit = [0]*POP_SIZE
        # for i in range(POP_SIZE):
        #     try:
        #         self.trFit[i] = (self.ind[POP_SIZE-1].fitness - self.ind[i].fitness) / \
        #             (self.ind[POP_SIZE-1].fitness - self.ind[0].fitness)
        #     except Exception:
        #         pdb.set_trace()
        #     self.denom += self.trFit[i] 

        for i in range(ELITE):
            for j in range(N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        for i in range(ELITE,POP_SIZE):
            # p1 = self.select_ranking_probability()
            # p2 = self.select_ranking_probability()
            # p1 = self.select_ranking()
            # p2 = self.select_ranking()
            # p1 = self.select_roulette()
            # p2 = self.select_roulette()
            p1 = self.select_tournament()
            p2 = self.select_tournament()
            # self.nextInd[i].crossover_one_point(self.ind[self.p1], self.ind[self.p2])
            self.nextInd[i].crossover_two_point(self.ind[p1], self.ind[p2])
            # self.nextInd[i].crossover_uniform(self.ind[self.p1], self.ind[self.p2])

        for i in range(POP_SIZE):
            self.nextInd[i].mutate()

        self.nextInd = self.ind
        self.evaluate()

    #select by order
    def select_ranking(self):
        denom = POP_SIZE * (POP_SIZE+1) // 2
        r = ((random.randint(0,RAND_MAX) << 16) + \
             (random.randint(0,RAND_MAX) << 1) + \
             (random.randint(0,RAND_MAX) % 2)) % denom + 1

        for num in reversed(range(1,POP_SIZE)):
            if r <= num:
                break
            r -= num

        return POP_SIZE - num

    def select_tournament(self):
        tmp = [0]*N
        ret = -1
        self.bestFit = FLT_MAX
        num = 0
        while True:
            r = random.randint(0,RAND_MAX) % N
            if tmp[r] == 0:
                tmp[r] = 1
                if self.ind[r].fitness < self.bestFit:
                    ret = r
                    self.bestFit = self.ind[r].fitness
                num += 1
                if num == TOURNAMENT_SIZE:
                    break
        return ret

    def select_roulette(self):
        # r = random.randint(0,RAND_MAX)
        r = random.random()
        for rank in range(1,POP_SIZE):
            prob = self.trFit[rank-1] / self.denom
            if r<= prob:
                break
            r -= prob
        
        return rank-1

    def select_ranking_probability(self):
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

