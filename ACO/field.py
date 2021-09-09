import pandas as pd
import numpy as np
class Field():
    def __init__(self, filename):
        self.distance  = pd.read_csv(filename, header=None)
        self.nodeNum = self.distance.shape[0]
        self.pheromone = np.zeros(\
            (self.nodeNum,self.nodeNum)).tolist()


