from flowerset import FlowerSet

if __name__=="__main__":
    fSet = FlowerSet("sampledata.csv")
    for i in range(REPEAT_NUM):
        fSet.employedBeePhase()
        fSet.onlookerBeePhase()
        fSet.scoutBeePhase()
        fSet.saveBestPos()
        print("Generation:{}, best fitness:{}"i,fSet.bestValue)
    fSet.printResult()

