#coding:utf-8
from variables import REPEAT_NUM
from colony import Colony

if __name__=="__main__":
    colony = Colony()
    for i in range(REPEAT_NUM):
        colony.selectRoute()
        colony.renewPheromone()
    colony.printPheromone()
