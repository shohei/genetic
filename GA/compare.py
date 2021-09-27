import random

from deap import base
from deap import creator
from deap import tools
import pdb

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)

def main(selMethod, cxMethod, indpb=0.05, tournsize=3):
    if cxMethod=="One":
        toolbox.register("mate", tools.cxOnePoint)
    if cxMethod=="Two":
        toolbox.register("mate", tools.cxTwoPoint)
    if cxMethod=="Uniform":
        toolbox.register("mate", tools.cxUniform, indpb=indpb)
    toolbox.register("mutate", tools.mutFlipBit, indpb=indpb)
    if selMethod=="Roulette":
        toolbox.register("select", tools.selRoulette)
    elif selMethod=="Tournament":
        toolbox.register("select", tools.selTournament, tournsize=tournsize)
    pop = toolbox.population(n=100)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    fits = [ind.fitness.values[0] for ind in pop]
    g = 0
    CXPB, MUTPB = 0.5, 0.2
    # pdb.set_trace()
    while max(fits) < 100 and g < 1000:
        g = g + 1
        # print("-- Generation %i --" % g)
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        pop[:] = offspring
        fits = [ind.fitness.values[0] for ind in pop]
        # print("  Max %s" % max(fits))
        if max(fits)==100:
            return g, 100
    return g, max(fits)

if __name__=="__main__":
    tournsize = 5
    indpb = 0.01
    # g, max_val = main("Roulette","Two",indpb, tournsize)
    g, max_val = main("Tournament","One",indpb, tournsize)
    print("indpb:",indpb,"tournsize",tournsize,"iteration",g, "max",max_val)
    g, max_val = main("Tournament","Two",indpb, tournsize)
    print("indpb:",indpb,"tournsize",tournsize,"iteration",g, "max",max_val)
    g, max_val = main("Tournament","Uniform",indpb, tournsize)
    print("indpb:",indpb,"tournsize",tournsize,"iteration",g, "max",max_val)
