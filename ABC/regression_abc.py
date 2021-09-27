from flowerset import FlowerSet
from variables import REPEAT_NUM

if __name__=="__main__":
    fSet = FlowerSet("sampledata.csv")
    for i in range(REPEAT_NUM):
        fSet.employedBeePhase()
        fSet.onlookerBeePhase()
        fSet.scoutBeePhase()
        fSet.saveBestPos()
        print("Generation:{}, best fitness:{}".format(i,fSet.bestValue))
    fSet.printResult()

