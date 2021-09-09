from ant import Ant 
from field import Field
from variables import ANT_NUM, PHERO_L, HEU_L, PHERO_R, EVA_R
import numpy as np
class Colony():
    def __init__(self, filename):
        self.field = Field(filename)
        self.ant= [Ant(self)]*ANT_NUM

        self.nume = np.zeros((self.field.nodeNum,self.field.nodeNum)).tolist()
        # for i in range(self.field.nodeNum):
        #     self.nume[i] = [0.0]*self.field.nodeNum

    def selectRoute(self):
        for i in range(self.field.nodeNum):
            for j in range(i):
                self.nume[i][j] = \
                    (self.field.pheromone[i][j])**PHERO_L * \
                        (1/self.field.distance[i][j])**HEU_L
            for j in range(i+1,self.field.nodeNum):
                self.nume[i][j] = \
                    (self.field.pheromone[i][j])**PHERO_L * \
                        (1/self.field.distance[i][j])**HEU_L

        for i in range(ANT_NUM):
            self.ant[i].selectRoute()

    def renewPheromone(self):
        for i in range(self.field.nodeNum):
            for j in range(i+1,self.field.nodeNum):
                self.field.pheromone[i][j] *= 1 - EVA_R

        for i in range(ANT_NUM):
            self.ant[i].putPheromone()

        
    def printPheromone(self):
        for i in range(self.field.nodeNum):
            for j in range(self.field.nodeNum):
                print(self.field.pheromone[i][j],end='')
            print()
