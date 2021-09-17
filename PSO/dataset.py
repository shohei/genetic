import pdb
import pandas as pd
import numpy as np
import math

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

        self.coef = [0.0]*self.exVarNum

        for i in range(self.dataNum):
            for j in range(self.exVarNum):
                self.exData[i][j] = df.loc[i,j]
                self.exAve[j] += self.exData[i][j]
            self.resData[i] = df.loc[i,self.exVarNum-1]
            self.resAve += self.resData[i]

        for j in range(self.exVarNum):
            self.exAve[j] /= self.dataNum
            for i in range(self.dataNum):
                self.exSd[j] += (self.exData[i][j] - self.exAve[j])**2
            self.exSd[j] = math.sqrt(self.exSd[j] / self.dataNum)

        self.resAve /= self.dataNum
        for i in range(self.dataNum):
            self.resSd += (self.resData[i] - self.resAve)**2
        self.resSd = math.sqrt(self.resSd / self.dataNum)

        for i in range(self.dataNum):
            for j in range(self.exVarNum):
                self.exSData[i][j] = (self.exData[i][j] - self.exAve[j]) / self.exSd[j]
            self.resSData[i] = (self.resData[i]-self.resAve) / self.resSd

    def setCoef(self, sCoef):
        self.constant = self.resAve
        for i in range(self.exVarNum):
            self.coef[i] = self.resSd / self.exSd[i] * sCoef[i]
            self.constant -= self.coef[i] * self.exAve[i]

    def printEquation(self):
        print("Regression: y= ",end='')
        for i in range(self.exVarNum):
            print("{:8.3f} x{} + ".format(self.coef[i],i+1),end='')
        print("{:8.3f}".format(self.constant))

