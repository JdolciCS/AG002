'''
  *Este es el algoritmo principal, este algoritmo esta encargado
  *de optimizar  los valores de las probabilidades de mutacion y
  *cruzamiento de un segundo algoritmo genetico(AG_objetivo).
'''
import numpy as np
import matplotlib.pyplot as plt
from ran import ran 				#Contiene funcion que genera poblacion aleatoria	
from genotipo import genotipo		#Contiene funcion que convierte los genes a genotipo
from pareja import pareja			#Funcion que se encarga de hacer la seleccion, cruzamiento y mutacion
from gen import gen					#Convierte el genotipo a genes
from AG_objetivo import AG_objetivo	#Es la funcion que contiene el algoritmo genetico que queremos optimizar


'''Parametros del algoritmo'''
dominio_funcion = 0.99999999
largo = 8						#longitud del gen (precision)(debe ser par)
Ngen = 40						#cantidad de generaciones
Nind = 40						#numero de individuos
mut = 0.1						#tasa de mutacion
cross = 0.8						#tasa de cruzamiento

'''domimio de la poblacion inicial'''
xmin = 0.00000001
xmax = dominio_funcion
ymin = 0.00000001
ymax = dominio_funcion

'''Arrays que usamos para graficar'''
mejoresElementos = np.zeros((Ngen))		#Valores finales de la curva Mejores elementos
off_line = np.zeros((Ngen))				#Valores finales de la curva off-line
on_line = np.zeros((Ngen))				#Valores finales de la curva on-line
sum_offLine = 0							#Es la variable que contiene la sumatoria del grafico off-line en cada generacion
sum_onLine = 0							#Es la variable que contiene la sumatoria del grafico on-line en cada generacion
axesX = np.arange(1,Ngen+1,1)			#Vector con el numero de generaciones, se usa para graficar




'''ciclo principal'''
genes = ran([xmin,ymin],[xmax,ymax],Nind)		#Generacion aleatoria de la primera generacion de genes
individuos = AG_objetivo(genes[:,0],genes[:,1])	#Se calcula cada "INDIVIDUO" a partir de los genes, AG_objetivo es la funcion objetivo
rank = 1/(1 - individuos)						#Se obtiene la "APTITUD" de cada individuo
iter = 0
while iter < Ngen:
	print("AG_1 : "+str(iter))
	genotipos = genotipo(genes,largo,xmax,ymax,xmin,ymin)	#se obtiene cada "GENOTIPO" a partir de los genes
	genotipoHijos = pareja(genotipos,rank,mut,cross,1)		#Se obtiene "GENOTIPOS HIJOS", seleccionando, mutando y cruzando los genotipos
	genes = gen(genotipoHijos,largo,xmax,ymax,xmin,ymin)	#Se obtiene la nueva generacion de "GENES" a partir de los genotipos hijos
	individuos = AG_objetivo(genes[:,0],genes[:,1])			#Obtengo los nuevos "INDIVIDUOS", a partir de los nuevos genes
	rank = 1/(1 - individuos)								#Se obtiene la nueva "APTITUD" de cada individuo
	'''Datos de los graficos'''
	mejoresElementos[iter] = np.amax(rank)
	sum_offLine = sum_offLine + np.amax(individuos)
	sum_onLine = sum_onLine + np.mean(individuos)
	off_line[iter] = sum_offLine/(iter+1)
	on_line[iter] = sum_onLine/(iter+1)
	iter = iter+1


'''Obtencion de la mejor solucion'''
mutFinal = genes[np.argmax(individuos),0]
crossFinal = genes[np.argmax(individuos),1]
print("Mut : "+str(mutFinal)+"    Cross : "+str(crossFinal))


'''Inicio de los graficos'''
plt.figure(3)
plt.subplot(2,2,2)
plt.plot(axesX,mejoresElementos,'-')
plt.title('Mejores elementos')
plt.subplot(2,2,3)
p = plt.plot(axesX,off_line,'--',label = "Off-line")
plt.title('off-line')
plt.subplot(2,2,4)
plt.plot(axesX,on_line,'-.',label = "on-line")
plt.title('on-line')
plt.show()