#coding: utf-8
import matplotlib.pyplot as plt
from variables import GEN_MAX
from population import Population

if __name__=="__main__":
    pop = Population()
    fig, ax = plt.subplots(1, 1)
    lines, = ax.plot(0, 0)
    x = []                 
    y = []                 
    for i in range(GEN_MAX):
        pop.alternate()
        print("Generation:{}, best fitness: {}" \
                 .format(i,pop.ind[0].fitness,))
        x.append(i)
        y.append(pop.ind[0].fitness)
        lines.set_data(x, y)
        ax.set_xlim((min(x), max(x)))
        ax.set_ylim((min(y), max(y)))
        ax.set_yscale('log')
        plt.pause(.01)

    pop.printResult()
