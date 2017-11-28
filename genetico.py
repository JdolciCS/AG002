###librerias
import numpy as np
from fun import fun
from ran import ran
from fentogen import fentogen
from pareja import pareja
from gentofen import gentofen

def genetico(pMut,pCru):
	f = 0
	c = 0
	pMut = pMut.reshape(pMut.shape[0],int(pMut.size/pMut.shape[0]))
	pCru = pCru.reshape(pMut.shape[0],int(pMut.size/pMut.shape[0]))
	de = np.zeros([pMut.shape[0],pMut.shape[1]])
	while f<pMut.shape[0]:
		c = 0
		while c<pMut.shape[1]:
			dominio_funcion = 10
			largo = 8				#longitud del gen (debe ser par)
			Ngen = 20				#cantidad de generaciones
			Nind = 20				#numero de individuos
			mut = pMut[f][c]				#tasa de mutacion
			cross = pCru[f][c]				#tasa de cruzamiento
			Nprueba = 20

			##domimio de la poblacion inicial##
			xmin = -dominio_funcion
			xmax = dominio_funcion
			ymin = -dominio_funcion
			ymax = dominio_funcion
		 
			p = 0
			mE = np.zeros(Nprueba)
			while p<Nprueba:
				ac_02 = 0
				ac_03 = 0
				n = ran([xmin,ymin],[xmax,ymax],Nind)
				t = np.arange(1,Ngen+1,1)
				#ciclo principal
				iter = 0
				while iter < Ngen:
					rank = 1/(1-fun(n[:,0],n[:,1]))
					n = fentogen(n,largo,xmax,ymax,xmin,ymin)
					n = pareja(n,rank,mut,cross)
					n = gentofen(n,largo,xmax,ymax,xmin,ymin)
					iter = iter+1
				rank = 1/(1-fun(n[:,0],n[:,1]))
				mE[p] = fun(n[np.argmax(rank),0],n[np.argmax(rank),1])
				p = p+1
			promedio = mE.mean()
			#print(np.sqrt(np.sum((promedio-mE)**2)/2))
			de[f][c] = np.sqrt( ( np.sum((promedio-mE)**2) )/Nprueba )
			c = c+1
		f = f+1
	return de