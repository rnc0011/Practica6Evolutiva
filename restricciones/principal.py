import random
import entrada_salida
import numpy as np
import matplotlib.pyplot as plt
from evaluacion import evaluate, feasible, distance
from deap import base, creator, tools, algorithms

def configuracionIndividuos():
    global toolbox
    toolbox = base.Toolbox()
    global pop
    
    tamano = entrada_salida.n_videos * entrada_salida.n_caches
    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    toolbox.register("attribute", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, 
                     creator.Individual, toolbox.attribute, n=tamano)
    toolbox.register("population", 
                     tools.initRepeat, list, toolbox.individual)
    
    pop = toolbox.population(n = 1000)
    
def configuracionAlgoritmo_Experimento1():
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)
    toolbox.decorate("evaluate", tools.DeltaPenalty(feasible, 1000000, distance))

def configuracionAlgoritmo_Experimento2():
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selBest)
    toolbox.register("evaluate", evaluate)
    toolbox.decorate("evaluate", tools.DeltaPenalty(feasible, 1000000, distance))

def configuracionAlgoritmo_Experimento3():
    toolbox.register("mate", tools.cxUniform, indpb=0.2)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)
    toolbox.decorate("evaluate", tools.DeltaPenalty(feasible, 1000000, distance))

def main():
    
    input_file = 'me_at_the_zoo.csv'
    output_file = 'salida.csv'
    
    entrada_salida.entrada(input_file)
    
    configuracionIndividuos()
    
    """ configuracionAlgoritmo_Experimento1()
    stats1 = tools.Statistics(lambda ind: ind.fitness.values)
    stats1.register("avg", np.mean)
    stats1.register("std", np.std)
    stats1.register("min", np.min)
    stats1.register("max", np.max)
    population1, logbook1 = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats1)

    print(stats1)
    print("La mejor solucion encontrada es: ")
    print(tools.selBest(population1, 1))
    print("Su fitness es: ")
    print(tools.selBest(population1, 1)[0].fitness.values)
    
    gen = logbook1.select("gen")
    avgs = logbook1.select("avg")
    
    fig, ax1 = plt.subplots()
    
    line1 = ax1.plot(gen, avgs, "r-", label="Average Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness 1", color="b")
    
    plt.plot()
    
    indi = tools.selBest(population1, 1)
    indi2 = np.array(indi)
    mejor_individuo = indi2.reshape(entrada_salida.n_caches, entrada_salida.n_videos)
    entrada_salida.salida(output_file, mejor_individuo)
    
    #Segundo experimento
    configuracionAlgoritmo_Experimento2()
    stats2 = tools.Statistics(lambda ind: ind.fitness.values)
    stats2.register("avg", np.mean)
    stats2.register("std", np.std)
    stats2.register("min", np.min)
    stats2.register("max", np.max)
    population2, logbook2 = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats2)

    print(stats2)
    print("La mejor solucion encontrada es: ")
    print(tools.selBest(population2, 1))
    print("Su fitness es: ")
    print(tools.selBest(population2, 1)[0].fitness.values)
    
    gen = logbook2.select("gen")
    avgs = logbook2.select("avg")
    
    fig, ax1 = plt.subplots()
    
    line1 = ax1.plot(gen, avgs, "r-", label="Average Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness 2", color="b")
    
    plt.plot()
    """
    #Tercer experimento
    configuracionAlgoritmo_Experimento3()
    stats3 = tools.Statistics(lambda ind: ind.fitness.values)
    stats3.register("avg", np.mean)
    stats3.register("std", np.std)
    stats3.register("min", np.min)
    stats3.register("max", np.max)
    population3, logbook3 = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=500, stats=stats3)

    print(stats3)
    print("La mejor solucion encontrada es: ")
    print(tools.selBest(population3, 1))
    print("Su fitness es: ")
    print(tools.selBest(population3, 1)[0].fitness.values)
    
    gen = logbook3.select("gen")
    avgs = logbook3.select("avg")
    
    fig, ax1 = plt.subplots()
    
    line1 = ax1.plot(gen, avgs, "r-", label="Average Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness 3", color="b")
    
    plt.plot()

if __name__ == "__main__":
    main()
