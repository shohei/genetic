from dataset import Dataset
from particle import Particle
from variables import SWARM_SIZE

class Swarm():
    def __init__(self, filename):
        self.dataset = Dataset(filename)
        self.particle = [[]] * SWARM_SIZE
        self.best = 0
        for i in range(SWARM_SIZE):
            self.particle[i] = Particle(self)
            if self.particle[self.best].value > self.particle[i].value:
                self.best = i
        self.gBestPos = [0.0]*self.dataset.exVarNum
        for i in range(self.dataset.exVarNum):
            self.gBestPos[i] = self.particle[self.best].pos[i]
        self.gBestValue = self.particle[self.best].value

    def move(self):
        self.best = -1
        for i in range(SWARM_SIZE):
            self.particle[i].move()
            if self.gBestValue > self.particle[i].value:
                self.best = i

        if self.best != -1:
            for i in range(self.dataset.exVarNum):
                self.gBestPos[i] = self.particle[self.best].pos[i]
            self.gBestValue = self.particle[self.best].value

    def printResult(self):
        self.dataset.setCoef(self.gBestPos)
        self.dataset.printEquation()