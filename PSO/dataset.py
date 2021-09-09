import pandas as pd
import numpy as np

class Dataset():
    def __init__(self, filename):
        df = pd.read_csv(filename, header=None)
        self.dataNum = df.shape[0]
        self.exVarNum = df.shape[1]-1

        self.exData = np.zeros((self.dataNum,self.exVarNum)).tolist()
        self.exSData = np.zeros((self.dataNum,self.exVarNum)).tolist()
        self.resData = [0.0]*self.dataNum
        self.resSData = [0.0]*self.dataNum

        self.exAve = [0.0]*self.exVarNum
        self.exSd = [0.0]*self.exVarNum

        self.resAve = 0.0
        self.resSd = 0.0

    def setCoef(self, sCoef):
        self.constant = self.resAve
        for i in range(self.exVarNum):
            self.coef[i] = self.resSd / self.exSd[i] * sCoef[i]
            self.constant -= self.coef[i] * self.exAve[i]

    def printEquation(self):
        print("Regression: y= ",end='')
        for i in range(self.exVarNum):
            print("{.3f} x{} + ".format(self.coef[i],i+1))
        print("{.3f}",self.constant)
