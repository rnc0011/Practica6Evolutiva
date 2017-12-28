''' 
DESCRIPCIÓN:

En este modulo se deben incluir los metodos necesarios para realizar la configuración que permita emplear
un algoritmo evolutivo definido en la libreria DEAP para la solucion del problema de HashCode'17.

Puesto que en el enunciado se solicita la comparacion de al menos 3 configuraciones, existen 3 copias de 
la funcion principal, en la que en cada una se debe incluir una variante.
'''

'''
Se deja al alumno libertad para tomar las decisiones de diseño de estos procesos: Se puede implementar
en una clase python o simplemente en un modulo con diferentes funciones y variables. Se pueden emplear 
las variables internas que se necesiten y  dividir el trabajo en funciones auxiliares según se considere 
conveniente.
''' 

'''
En más detalle, los pasos completos serán:

1.- Emplear 'creator' para definir los tipos de los individuos y de la funcion de adaptacion
(ver http://deap.readthedocs.io/en/master/overview.html, sección "Types")

2.- Emplear 'base.Toolbox' para configurar la poblacion de individuos. Es decir, indicar al algoritmo
primero como vamos a representar internamente una solución posible al problema (individuo) y luego como se va a 
representar el conjunto de soluciones posibles (poblacion) que vamos a intentar evolucionar hasta encontrar 
la más adecuada.
(ver http://deap.readthedocs.io/en/master/overview.html - sección "Initialization")
(ver http://deap.readthedocs.io/en/master/tutorials/basic/part2.html - seccion "A First Individual")

3.- Emplear 'base.Toolbox' para configurar que algoritmo de los vistos en teoría para cada una de las secciones
de un A.G. se desea emplear en cada caso.
(ver http://deap.readthedocs.io/en/master/overview.html, sección "Operators")
(ver http://deap.readthedocs.io/en/master/tutorials/basic/part2.html - seccion "Using the Toolbox")
Se puede encontrar el listado completo de las diferentes alternativas para cada operación básica en:
http://deap.readthedocs.io/en/master/api/tools.html#operators

4.- Es importante que en el apartado "evaluate" de esa configuración, se incluya la función de adaptación que se ha 
programado en el modulo "evaluacion.py" (creado en esta práctica)

5.- Con todo ya configurado, iniciar el proceso de evolución.
Comprobar https://deap.readthedocs.io/en/master/tutorials/basic/part2.html - sección "Algorithms"
Simplemente se trata de llamar al metodo "algorithms.eaSimple" facilitando los parametros definidos en los 
puntos anteriores. Otro ejemplo con más configuraciones (que en este caso no son necesarias) está en:
 http://deap.readthedocs.io/en/master/examples/ga_onemax_short.html

6.- Recuperar las estadísticas para poder completar una gráfica y comparar resultados.
La manera más sencilla de hacer esto es emplear el objeto 'stats' que se incluye en la librería. Se debe: 
1) Configurar para indicar que datos se quieren registrar sobre la evolucion.
2) Facilitar el objeto como parametro al algoritmo que realizar la evolución. 
3) Recuperar al finalizar la evolución y acceder a los resultados.
4) Realizar un plot empleando esos datos numéricos.
Se puede ver un tutorial completo en: http://deap.readthedocs.io/en/master/tutorials/basic/part3.html - Sección "Some Plotting Sugar"
NO es necesario emplear lo indicado en "Multi-objective Statistics", ya que nuestro problema no lo requiere.
''' 

## Se debe MODIFICAR para definir que cada individuo tiene que tener más de un fitness
## Se debe indicar por cada uno si se quiere maximizar o minimizar.
def configuracionIndividuos():
	#TODO
	''' 1.- Definir el tipo del fitness MULTI-OBJETIVO
		2.- Definir tipo y tamaño de cada individuo
		3.- Definir población como conjunto de individuos
	No es necesario que se modifiquen los de la práctica anterior, al tratarse del mismo problema
	'''

# Se debe MODIFICAR para que admita el tratamiento de restricciones.
# ver https://deap.readthedocs.io/en/master/tutorials/advanced/constraints.html
# ultima parte del ejemplo
def configuracionAlgoritmo_Experimento1():
	#TODO
	''' 1.- Definir la funcion que calcula la adaptacion
		CUIDADO - En esta práctica se debe modificar
		2.- Definir metodos para seleccion, cruce, mutacion
		CUIDADO - La selección debe ser solo entre aquellas que acepten mutli-objetivo
	'''
### Se incluirá en la función calculaSolucion_1() la mejor configuración que se haya encontrado en las diferentes pruebas
### Se considera que esa sería la respuesta que proporcionaría el programa en el desafío HashCode'17.


# Se debe MODIFICAR para que admita el tratamiento de restricciones.
# ver https://deap.readthedocs.io/en/master/tutorials/advanced/constraints.html
# ultima parte del ejemplo
def configuracionAlgoritmo_Experimento2():
	#TODO
	''' 1.- Definir funcion de adaptacion
		2.- Definir metodos para seleccion, cruce, mutacion
		CUIDADO - La selección debe ser solo entre aquellas que acepten mutli-objetivo
	'''


# Se debe MODIFICAR para que admita el tratamiento de restricciones.
# ver https://deap.readthedocs.io/en/master/tutorials/advanced/constraints.html
# ultima parte del ejemplo
def configuracionAlgoritmo_Experimento3():
	#TODO
	''' 1.- Definir funcion de adaptacion
		2.- Definir metodos para seleccion, cruce, mutacion
		CUIDADO - La selección debe ser solo entre aquellas que acepten mutli-objetivo
	'''

def main():

	input_file = 'ruta/del/fichero/de/entrada'
	output_file = 'ruta/del/fichero/de/solucion'

	# 1.- Llamar a los metodos de lectura de datos, para tenerlos disponibles en los siguientes metodos

	# 2.- Configurar los individuos
	configuracionIndividuos()

	# 2.- Ejecución del algoritmo con la configuración seleccionada
	configuracionAlgoritmo_Experimento1(toolbox) # Esta configuración será la encontrada como la mejor para el problema planteado
	# Configuraciones adicionales (si es necesario)
	population1, logbook1 = algoritms.eaSimple()

	# Se incluyen para mayor claridad.
	# Se pueden simplemente comentar para obtener los resultados mas interesantes
	configuracionAlgoritmo_Experimento2(toolbox)
	# Configuraciones adicionales (si es necesario)
	population1, logbook1 = algoritms.eaSimple()
	configuracionAlgoritmo_Experimento3(toolbox)
	# Configuraciones adicionales (si es necesario)
	population1, logbook1 = algoritms.eaSimple()

	# 3.- calculo de estadísticas y graficas
	# Para comparar los resultados obtenidos por los diferentes experimentos
	# (Estarán en las variables de population y logbook) 

	# 4.- Almacenamiento de la solución óptima en el fichero de resultados

if __name__ == "__main__":
    main()
