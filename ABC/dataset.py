import pandas as pd


class Dataset():
    def __init__(self, filename):
        df = pd.read_csv(filename, header=Non)

        self.exData = []
        self.exSData = []
        self.resData = []
        self.resSData = []
        self.exSd = []
        self.coef = []

        self.resAve = 0.0
        self.resSd = 0.0

    def setCoef(self, sCoef):
        pass

    def printEquation(self):
        pass
