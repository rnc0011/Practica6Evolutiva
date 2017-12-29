import entrada_salida
import numpy as np
sobrepeso = 0
indi2 = None

def evaluate(individual):
    
    score = 0
    peticiones_totales = 0
    latencia_minima = 0
    caches_usadas = list()
     
    for i in range(entrada_salida.n_caches):
        caches_usadas.append(list())
        for j in range(entrada_salida.n_videos):
            caches_usadas[i].append(0)
            
    for i in range(entrada_salida.endpoints):
        for j in range(entrada_salida.n_videos):
            latencia_minima = 0
            if entrada_salida.peticiones[i][j] is not 0:
                peticiones_totales += entrada_salida.peticiones[i][j] 
                latencia_minima = entrada_salida.latencias[i][-1]
                for cache in entrada_salida.latencias[i]:
                    if cache is not -1 and indi2[i][j] == 1 and entrada_salida.latencias[i][cache] < latencia_minima:
                        caches_usadas[cache][j] = 1
                        latencia_minima = entrada_salida.latencias[i][cache]
                score += entrada_salida.peticiones[i][j] * latencia_minima
                
    score /= peticiones_totales
    
    for i in range(entrada_salida.n_caches):
        for j in range(entrada_salida.n_videos):
            if caches_usadas[i][j] == 0 and indi2[i][j] == 1:
                score += 10000

    return score,   

def feasible(individual):
    global sobrepeso
    global indi2
    flag = True
    indi = np.array(individual)
    indi2 = indi.reshape(entrada_salida.n_caches, entrada_salida.n_videos)
    tamanos = np.dot(indi2, entrada_salida.tamano_videos)
    sobrepeso = 0
    
    for i in tamanos:
        if i > entrada_salida.tamano_caches:
            sobrepeso += i - entrada_salida.tamano_caches
            flag = False
            
    return flag

def distance(individual):
	return sobrepeso * 100000