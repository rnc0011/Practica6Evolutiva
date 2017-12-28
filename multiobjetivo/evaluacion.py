''' 
DESCRIPCIÓN:

En este modulo se deben incluir los metodos necesarios para realizar las comprobaciones sobre soluciones
individuales que permitan emplear un algoritmo evolutivo definido en la libreria DEAP para la solucion del 
problema de HashCode'17.

En general, en este modulo se pide incluir todos los metodos que tienen que ver con la representación interna
de las soluciones al problema y las posibles conversiones entre la representacion interna y otras que se
pueda necesitar.

Esto incluye:

1.- Importar modulos necesarios

2.- Evaluación de cada uno de los individuos
Se puede consultar un ejemplo en: https://deap.readthedocs.io/en/master/overview.html
En el apartado "Operators", en la primera función definida.
Se debe implementar al menos UNA FUNCIÓN a la que se le facilitará cada uno de los individuos de la 
población y deberá determinar su grado de adaptación al problema que se solicita resolver.

3.- Otros cálculos sobre individuos
Probablemente sea necesario, dado un individuo, obtener una representación del mismo preparada para 
imprimir en pantalla o para almacenar en un fichero. Se pueden emplear funciones auxiliares para ello.
'''

'''
Se deja al alumno libertad para tomar las decisiones de diseño de estos procesos: Se puede implementar
en una clase python o simplemente en un modulo con diferentes funciones y variables. Se pueden emplear 
las variables internas que se necesiten y dividir el trabajo en funciones auxiliares según se considere 
conveniente.
''' 

# Ejemplo de función de evaluación

def evaluate(individual):

'''
Se sugiere partir de las funciones de evaluación que se hayan implementado en prácticas anteriores.

En este caso, la función deberá devovler más de un valor de evaluación (dentro de una tupla). 
Uno hará referencia al TIEMPO que se tarda en servir los videos.
El otro al ESPACIO libre que queda en cada servidor.

Un ejemplo se puede encontrar en: 
https://deap.readthedocs.io/en/master/tutorials/basic/part2.html
'''