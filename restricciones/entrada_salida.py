#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:59:44 2017

@author: Raúl Negro Carpintero
@author: Mario Núñez Izquierdo
"""

import csv

n_videos = 0
latencias = None
n_caches = 0
tamano_videos = None
tamano_caches = 0
peticiones = None

def entrada(fichero_entrada):  
    
    global n_videos
    global latencias
    global n_caches
    global tamano_videos
    global tamano_caches
    global peticiones
    global endpoints
    
    archivo = open(fichero_entrada)
    longitud = len(archivo.readlines())
    archivo.seek(0)
    entrada = csv.reader(archivo)
    endpoints = 0
    n_videos = 0
    caches = 0
    caches_totales = 0
    n_caches = 0
    tamano_caches = 0
    tamano_videos = list()
    latencias = list()
    lista_cifras = list()
    matriz = list()
    peticiones = list()
    
    for i in range(longitud):
        aux = next(entrada)
        lista_cifras = list()
        matriz.append(list()) 
        for char in aux[0]:
            if char is not ' ':
                lista_cifras.append(char)
            else:
                matriz[i].append(calcular_datos(lista_cifras))
                lista_cifras = list()
        matriz[i].append(calcular_datos(lista_cifras))
        
    archivo.close()
        
    endpoints = matriz[0][1]
    n_videos = matriz[0][0]
    n_caches= matriz[0][3]
    tamano_caches = matriz[0][4]
    tamano_videos = matriz[1]
    
    for i in range(endpoints):
        latencias.append(dict())
        caches = matriz[2 + i + caches_totales][1]
        latencias[i][-1] = matriz[2 + i + caches_totales][0]
        caches_totales += caches
        for j in range(caches):
            latencias[i][matriz[3 + i + j][0]] = matriz[3 + i + j][1]
           
    for i in range(endpoints):
        peticiones.append(list())
        for j in range(n_videos):
            peticiones[i].append(0)
            
    for i in range(2 + endpoints + caches_totales, len(matriz)):
        peticiones[matriz[i][1]][matriz[i][0]] = matriz[i][2]
    
def calcular_datos(datos):
    resultado = 0
    i = 0
    while i < len(datos):
        resultado += int(datos[i]) * (10**(len(datos) - i - 1))
        i += 1
    return resultado 

def salida(fichero_salida, individuo):
    
    flag = False
    caches_usadas = 0
    resultado = list()
    resultado.append(list())
    
    for i in range(n_caches):
        resultado.append(list())
        for j in range(n_videos):
            if individuo[i][j] != 0:
                resultado[i+1].append(j)
                flag = True
        if flag:
            flag = False
            caches_usadas += 1
    resultado[0].append(caches_usadas)
    
    csv_salida = open(fichero_salida, 'w', newline='')
    salida = csv.writer(csv_salida, delimiter=' ')
    salida.writerows(resultado)
    del salida
    csv_salida.close()