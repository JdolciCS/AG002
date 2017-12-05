'''
  *Esta funcion es la la funcion objetivo del primer algoritmo genetico (AG_01)
  *Esta funcion retorna la media de los mejores valores
'''
import numpy as np
from fun_objetivo import fun_objetivo	#Funcion Objetivo para este algoritmo genetico
from ran import ran
from genotipo import genotipo
from pareja import pareja
from gen import gen

def AG_objetivo(pMut,pCru):
	fila = 0		#fila y columna son los indices de la matriz pMut y pCru
	columna = 0
	pMut = pMut.reshape(pMut.shape[0],int(pMut.size/pMut.shape[0]))
	pCru = pCru.reshape(pMut.shape[0],int(pMut.size/pMut.shape[0]))
	promedio = np.zeros([pMut.shape[0],pMut.shape[1]])
	while fila<pMut.shape[0]:
		columna = 0
		while columna<pMut.shape[1]:
			#print("   Par de Probabilidad : "+str(a)+"/"+str(50))
			dominio_funcion = 10
			largo = 8				#longitud del gen (debe ser par)
			Ngen = 40				#cantidad de generaciones
			Nind = 40				#numero de individuos
			mut = pMut[fila][columna]				#toma una tasa de mutacion de la matriz pMut
			cross = pCru[fila][columna]				#toma una tasa de cruzamiento de la matriz pCru
			Nprueba = 20

			##domimio de la poblacion inicial##
			xmin = -dominio_funcion
			xmax = dominio_funcion
			ymin = -dominio_funcion
			ymax = dominio_funcion
		 
			prueba = 0
			mejorIndividuo = np.zeros(Nprueba)
			while prueba<Nprueba:
				#ciclo principal
				genes = ran([xmin,ymin],[xmax,ymax],Nind)
				individuos = fun_objetivo(genes[:,0],genes[:,1])
				rank = 1/(1-individuos)
				iter = 0
				while iter < Ngen:
					genotipos = genotipo(genes,largo,xmax,ymax,xmin,ymin)
					genotipoHijos = pareja(genotipos,rank,mut,cross,2)
					genes = gen(genotipoHijos,largo,xmax,ymax,xmin,ymin)
					individuos = fun_objetivo(genes[:,0],genes[:,1])
					rank = 1/(1-individuos)
					iter = iter+1
				mejorIndividuo[prueba] = np.amax(individuos)
				prueba = prueba+1
			promediofc = mejorIndividuo.mean()
			#print(np.sqrt(np.sum((promedio-mejorIndividuo)**2)/2))
			promedio[fila][columna] = promediofc
			columna = columna+1
		fila = fila+1
	return promedio