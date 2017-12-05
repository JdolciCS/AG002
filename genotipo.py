'''
  *Esta funcion toma los genes, los normaliza y luego los une formando el genotipo
 '''
import numpy as np
def genotipo(n,largo,xmax,ymax,xmin,ymin):
	n[:,0] = (n[:,0]-xmin)/(xmax - xmin)#Normaliza los datos
	n[:,1] = (n[:,1]-ymin)/(ymax - ymin)
	n = n * (10**(largo+1))#combierte a entero para poder trabajar con binario
	n = n.astype(int)
	r = n[:,1]+(n[:,0]*(2**32))
	return r