from dataset import Dataset
from variables import EBEE_NUM, DBL_MIN, DBL_MAX, OBEE_NUM
from variables import VISIT_MAX
from flower import Flower
import random
class FlowerSet():
    def __init__(self, filename):
        self.dataset = Dataset(filename)
        self.flower = [[]]*EBEE_NUM
        best = 0
        for i in range(EBEE_NUM):
            self.flower[i] = Flower(self)
            if self.flower[best].value > self.flower[i].value:
                best = i

        self.bestPos = [0.0]*self.dataset.exVarNum
        for i in range(self.dataset.exVarNum):
            self.bestPos[i] = self.flower[best].pos[i]

        self.bestValue = self.flower[best].value
        self.newFlower = Flower(self)
        self.trValue = [0.0]*EBEE_NUM

    def employedBeePhase(self):
        for i in range(EBEE_NUM):
            self.newFlower.change(i)
            if self.flower[i].value > self.newFlower.value:
                self.newFlower, self.flower[i] = self.flower[i], self.newFlower
            self.flower[i].visitNum += 1

    def onlookerBeePhase(self):
        for j in range(OBEE_NUM):
            max = DBL_MIN
            min = DBL_MAX
            for i in range(EBEE_NUM):
                if max < self.flower[i].value:
                    max = self.flower[i].value
                if min > self.flower[i].value:
                    min = self.flower[i].value
            self.denom = 0.0
            for i in range(EBEE_NUM):
                self.trValue[i] = (max-self.flower[i].value)/(max-min)
                self.denom += self.trValue[i]

        r = random.random()
        for i in range(EBEE_NUM-1):
            prob = self.trValue[i] / self.denom
            if r<= prob:
                break
            r -= prob
        
        self.newFlower.change(i)
        if self.flower[i].value > self.newFlower.value:
            self.newFlower, self.flower[i] = self.flower[i], self.newFlower
        
        self.flower[i].visitNum += 1

    def scoutBeePhase(self):
        for i in range(EBEE_NUM):
            if VISIT_MAX <= self.flower[i].visitNum:
                self.flower[i].renew()

    def saveBestPos(self):
        best = -1
        for i in range(EBEE_NUM):
            if self.bestValue > self.flower[i].value:
                best = i
        if best != -1:
            for i in range(self.dataset.exVarNum):
                self.bestPos[i] = self.flower[best].pos[i]
            self.bestValue = self.flower[best].value

    def printResult(self):
        self.dataset.setCoef(self.bestPos)
        self.dataset.printEquation()
