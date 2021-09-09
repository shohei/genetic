from swarm import Swarm
from variables import TIME_MAX

if __name__=="__main__":
    swarm = Swarm("sampledata.csv")
    for t in range(TIME_MAX):
        swarm.move()
        print("time {}: best result{}".format(t,swarm.gBestValue))
    swarm.printResult()



