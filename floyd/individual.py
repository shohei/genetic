# coding:utf-8
import random
import math
from variables import MUTATE_PROB, N, RAND_MAX 

class Individual():
    def __init__(self):
        self.chrom = [0]*N
        self.fitness = 0
        for i in range(N):
            self.chrom[i] = random.randint(0,RAND_MAX) % 2

    def evaluate(self):
        fitness = 0
        for i in range(N):
            fitness += (self.chrom[i] * 2 - 1) * math.sqrt(i+1)
        self.fitness = math.fabs(fitness)

    def crossover_one_point(self,p1,p2):
        point = random.randint(0,RAND_MAX) % (N-1)
        for i in range(point):
            self.chrom[i] = p1.chrom[i]
        for i in range(point,N):
            self.chrom[i] = p2.chrom[i]

    def crossover_two_point(self, p1,p2):
        point1 = random.randint(0,RAND_MAX) % (N-1)
        point2 = (point1+(random.randint(0,RAND_MAX) % (N-2) +1)) % (N-1)
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
            if (random.randint(0,RAND_MAX) % 2) == 1:
                self.chrom[i] = p1.chrom[i]
            else:
                self.chrom[i] = p2.chrom[i]

    def mutate(self):
        for i in range(N):
            if random.random() < MUTATE_PROB:
                self.chrom[i] = 1 - self.chrom[i]