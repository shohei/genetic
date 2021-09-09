import random
from variables import COEF_MIN, COEF_MAX, COEF_MIN, RAND_MAX
from variables import EBEE_NUM


class Flower():
    def __init__(self, argFSet):
        self.fSet = argFSet
        self.pos = [0.0]*self.fSet.dataset.exVarNum
        for i in range(self.fSet.dataset.exVarNum):
            self.pos[i] = COEF_MIN + (COEF_MAX-COEF_MIN)*random.random()
        self.visitNum = 0
        self.evaluate()

    def change(self, base):
        for i in range(self.fSet.dataset.exVarNum):
            self.pos[i] = self.fSet.flower[base].pos[i]
        i = random.randint(0,RAND_MAX) % self.fSet.dataset.exVarNum
        j = (base + (random.randint(0,RAND_MAX) % (EBEE_NUM-1) +1)) % EBEE_NUM
        self.pos[i] = self.pos[i] \
                 + (random.randint(0,RAND_MAX)/(RAND_MAX/2.0)-1) \
                 * (self.pos[i]-self.fSet.flower[j].pos[i])
        self.visitNum = 0
        self.evaluate()

    def renew(self):
        for i in range(self.fSet.dataset.exVarNum):
            pos[i] = COEF_MIN + (COEF+_MAX - COEF_MIN) * random.random()

        self.visitNum = 0
        self.evaluate()

    def evaluate(self):
        value = 0.0
        for i in range(self.fSet.dataset.dataNum):
            diff = self.fSet.dataset.resSData[i]
            for j in range(self.fSet.dataset.exVarNum):
                diff -= self.pos[j]*self.fSet.dataset.exSData[i][j]
            value += diff**2.0

