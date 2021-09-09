import random
from variables import COEF_MIN, COEF_MAX, DBL_MAX
from variables import ACCEL_G, ACCEL_P, INERTIA

class Particle():
    def __init__(self, argSwarm):
        self.swarm = argSwarm
        self.pos = [0.0]*self.swarm.dataset.exVarNum
        self.velocity = [0.0]*self.swarm.dataset.exVarNum
        for i in range(self.swarm.dataset.exVarNum):
            self.pos[i] = COEF_MIN + (COEF_MAX-COEF_MIN) * random.random()
            self.velocity[i] = COEF_MIN + (COEF_MAX-COEF_MIN) * random.random()

        self.pBestPos = [0.0]*self.swarm.dataset.exVarNum
        self.pBestValue = DBL_MAX
        self.evaluate()
    
    def move(self):
        for i in range(self.swarm.dataset.exVarNum):
            self.velocity[i] = INERTIA * self.velocity[i] \
                + ACCEL_G * (self.swarm.gBestPos[i]-self.pos[i])*random.random() \
                + ACCEL_P * (self.pBestPos[i]-self.pos[i])*random.random()
        self.evaluate()

    def evaluate(self):
        self.value = 0.0
        for i in range(self.swarm.dataset.dataNum):
            diff = self.swarm.dataset.resSData[i]
            for j in range(self.swarm.dataset.exVarNum):
                diff -= self.pos[j]*self.swarm.dataset.exSData[i][j]
            
            self.value += diff**2.0
        if self.pBestValue > self.value:
            for i in range(self.swarm.dataset.exVarNum):
                self.pBestPos[i] = self.pos[i]

            self.pBestValue = self.value

