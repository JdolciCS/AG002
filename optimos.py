import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from fun import fun
from ran import ran
from fentogen import fentogen
from pareja import pareja
from gentofen import gentofen
import time as time
from genetico import genetico


###Parametros del algoritmo###
genes = 2				#cromosoma-->(gen x,gen y)
dominio_funcion = 0.9999
largo = 8				#longitud del gen (debe ser par)
Ngen = 30				#cantidad de generaciones
Nind = 10				#numero de individuos
mut = 0.1				#tasa de mutacion
cross = 0.8				#tasa de cruzamiento

fig_01 = np.zeros((Ngen))
fig_02 = np.zeros((Ngen))
fig_03 = np.zeros((Ngen))

##domimio de la poblacion inicial##
xmin = 0.0001 #-dominio_funcion
xmax = dominio_funcion
ymin = 0.0001 #-dominio_funcion
ymax = dominio_funcion


fig_01_ = np.zeros((Ngen))
fig_02_ = np.zeros((Ngen))
fig_03_ = np.zeros((Ngen))
ac_02 = 0
ac_03 = 0
n = ran([xmin,ymin],[xmax,ymax],Nind)
t = np.arange(1,Ngen+1,1)
#ciclo principal
iter = 0
#print("Iteracion general : "+str(iter)+"/"+str(Ngen))
aux = genetico(n[:,0],n[:,1])
while iter < Ngen:
	#print("Iteracion general : "+str(iter+1)+"/"+str(Ngen))
	rank = 1/(1-aux)
	n = fentogen(n,largo,xmax,ymax,xmin,ymin)
	n = pareja(n,rank,mut,cross,1)
	n = gentofen(n,largo,xmax,ymax,xmin,ymin)
	fig_01_[iter] = np.amax(rank)
	aux = genetico(n[:,0],n[:,1])
	ac_02 = ac_02 + np.amax(aux)
	ac_03 = ac_03 + np.mean(aux)
	fig_02_[iter] = ac_02/(iter+1)
	fig_03_[iter] = ac_03/(iter+1)
	iter = iter+1
r1 = n[np.argmax(aux),0]
r2 = n[np.argmax(aux),1]
print("Mut : "+str(r1)+"    Cross : "+str(r2))
plt.figure(3)
plt.subplot(2,2,2)
plt.plot(t,fig_01_,'-')
plt.title('Mejores elementos')
plt.subplot(2,2,3)
p = plt.plot(t,fig_02_,'--',label = "Off-line")
plt.title('off-line')
plt.subplot(2,2,4)
plt.plot(t,fig_03_,'-.',label = "on-line")
plt.title('on-line')
plt.show()