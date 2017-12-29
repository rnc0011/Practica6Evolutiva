import random
import entrada_salida
import numpy as np
import matplotlib.pyplot as plt
from evaluacion import evaluate
from deap import base, creator, tools, algorithms

def configuracionIndividuos():
    global toolbox
    toolbox = base.Toolbox()
    global pop
    
    tamano = entrada_salida.n_videos * entrada_salida.n_caches
    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,-1.0))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    toolbox.register("attribute", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, 
                     creator.Individual, toolbox.attribute, n=tamano)
    toolbox.register("population", 
                     tools.initRepeat, list, toolbox.individual)
    
    pop = toolbox.population(n = 100)
    
def configuracionAlgoritmo_Experimento1():
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selSPEA2)
    toolbox.register("evaluate", evaluate)
    
def configuracionAlgoritmo_Experimento2():
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("evaluate", evaluate)

def main():
    input_file = 'me_at_the_zoo.csv'
    output_file = 'salida.csv'
    
    entrada_salida.entrada(input_file)
    
    configuracionIndividuos()
    
    configuracionAlgoritmo_Experimento1()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    population1, logbook1 = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=200, stats=stats)

    print(stats)
    print("La mejor solucion encontrada es: ")
    print(tools.selBest(population1, 1))
    
    gen = logbook1.select("gen")
    mins = logbook1.select("min")
    
    fig, ax1 = plt.subplots()
    
    line1 = ax1.plot(gen, mins, "r-", label="Min Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    
    plt.plot()
    
    indi = tools.selBest(population1, 1)
    indi2 = np.array(indi)
    mejor_individuo = indi2.reshape(entrada_salida.n_caches, entrada_salida.n_videos)
    entrada_salida.salida(output_file, mejor_individuo)


if __name__ == "__main__":
    main()
