import random
from variables import RAND_MAX, PHERO_Q, PHERO_R
import pdb

class Ant():
    def __init__(self, argColony):
        self.colony = argColony
        self.route = [0]*self.colony.field.nodeNum
        self.candidate = [0]*self.colony.field.nodeNum
        self.totalDis = 0.0

    def selectRoute(self):
        for i in range(self.colony.field.nodeNum):
            self.candidate[i] = 1
        
        self.totalDis = 0.0
        for i in range(self.colony.field.nodeNum-2):
            denom = 0.0
            for j in range(self.colony.field.nodeNum):
                if self.candidate[j]==1:
                    denom += self.colony.nume[self.route[i]][j]
            
            next = -1
            if (denom!=0.0) & (random.random()<=PHERO_R):
                r = random.random()
                for next in range(1,self.colony.field.nodeNum):
                    if self.candidate[next]==1:
                        prob = self.colony.nume[self.route[i]][next] / denom
                        if r <= prob:
                            break
                        r -= prob
                if next==self.colony.field.nodeNum:
                    next = -1
            if next==-1:
                next2 = random.randint(0,RAND_MAX) % (self.colony.field.nodeNum-i-1)
                for next in range(1,self.colony.field.nodeNum-1):
                    if self.candidate[next]==1:
                        if next2==0:
                            break
                        else:
                            next2 -= 1

            self.route[i+1] = next
            self.candidate[next] = 0
            self.totalDis += self.colony.field.distance[self.route[i]][next]
        
            for next in range(1,self.colony.field.nodeNum):
                if self.candidate[next]==1:
                    break
            
            self.route[self.colony.field.nodeNum-1] = next
            self.totalDis += self.colony.field.distance[ \
                self.route[self.colony.field.nodeNum-2]][next]

            self.totalDis += self.colony.field.distance[next][0]



    def putPheromone(self):
        p = PHERO_Q / self.totalDis
        for i in range(self.colony.field.nodeNum-1):
            if self.route[i]<self.route[i+1]:
                self.colony.field.pheromone[self.route[i]][self.route[i+1]] += p
            else:
                self.colony.field.pheromone[self.route[i]][self.route[i+1]] += p
            
            self.colony.field.pheromone[0][\
                self.route[self.colony.field.nodeNum-1]]








