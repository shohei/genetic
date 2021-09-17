#coding:utf-8
import pdb
from variables import REPEAT_NUM
from colony import Colony
import os
SCRIPT_DIR =os.path.dirname(os.path.abspath(__file__))

if __name__=="__main__":
    colony = Colony(SCRIPT_DIR+"/sampledata.csv")
    for i in range(REPEAT_NUM):
        print(i)
        colony.selectRoute()
        colony.renewPheromone()
        # if colony.field.pheromone[6][6] > 0:
        #     pdb.set_trace()
    colony.printPheromone()
