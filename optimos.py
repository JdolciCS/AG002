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
Ngen = 20				#cantidad de generaciones
Nind = 20				#numero de individuos
mut = 0.1				#tasa de mutacion
cross = 0.8				#tasa de cruzamiento
Nprueba = 20

fig_01 = np.zeros((Ngen))
fig_02 = np.zeros((Ngen))
fig_03 = np.zeros((Ngen))
fig_04 = np.zeros((Nprueba))
fig_05 = np.zeros((Nprueba,2))

##domimio de la poblacion inicial##
xmin = 0.0001 #-dominio_funcion
xmax = dominio_funcion
ymin = 0.0001 #-dominio_funcion
ymax = dominio_funcion

##Ploteo de la superficie

		####X = np.arange(xmin, xmax, (xmax - xmin)/100)
		####Y = np.arange(ymin, ymax, (ymax - ymin)/100)
		####X, Y = np.meshgrid(X, Y)	#meshgrid
####Z = genetico(X,Y) # Z esta de la forma original y fun(x,y) esta invertida

#fig = plt.figure()
#ax = Axes3D(fig)
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)	#surfc
#plt.show(block=False)
##time.sleep(3)
##plt.cla()
##plt.show()
p = 0
while p<Nprueba:
	print(p)
	fig_01_ = np.zeros((Ngen))
	fig_02_ = np.zeros((Ngen))
	fig_03_ = np.zeros((Ngen))
	ac_02 = 0
	ac_03 = 0
	n = ran([xmin,ymin],[xmax,ymax],Nind)
	t = np.arange(1,Ngen+1,1)
	#ciclo principal
	iter = 0
	aux = 0
	while iter < Ngen:
		print(iter)
		rank = 1/(genetico(n[:,0],n[:,1]))
		n = fentogen(n,largo,xmax,ymax,xmin,ymin)
		n = pareja(n,rank,mut,cross)
		n = gentofen(n,largo,xmax,ymax,xmin,ymin)
		fig_01_[iter] = np.amax(rank)
		aux = genetico(n[:,0],n[:,1])
		ac_02 = ac_02 + np.amin(aux)
		ac_03 = ac_03 + np.mean(aux)
		fig_02_[iter] = ac_02/(iter+1)
		fig_03_[iter] = ac_03/(iter+1)
		iter = iter+1
	fig_04[p] = np.amin(aux)
	#fig_05[p,0] = n[np.argmin(genetico(n[:,0],n[:,1])),0]
	#fig_05[p,1] = n[np.argmin(genetico(n[:,0],n[:,1])),1]
	p = p+1
	fig_01 = fig_01+fig_01_
	fig_02 = fig_02+fig_02_
	fig_03 = fig_03+fig_03_
fig_01 = fig_01/Nprueba
fig_02 = fig_02/Nprueba
fig_03 = fig_03/Nprueba
plt.figure(3)
	#plt.subplot(2,2,1)
	#plt.plot(fig_05[:,0],fig_05[:,1],'ro')
	#plt.contour(X,Y,Z)
	#plt.title('Resultado mut = '+str(mut)+' cross = '+str(cross))
plt.subplot(2,2,2)
plt.plot(t,fig_01,'-')
#plt.xlabel('Generacion')
plt.title('Mejores elementos')
plt.subplot(2,2,3)
p = plt.plot(t,fig_02,'--',label = "Off-line")
#plt.xlabel('Generacion')
plt.title('off-line')
plt.subplot(2,2,4)
plt.plot(t,fig_03,'-.',label = "on-line")
#plt.xlabel('Generacion')
plt.title('on-line')
plt.show(block = False)
plt.figure(4)
plt.boxplot(fig_04)
plt.title('BoxPlot mut = '+str(mut)+' cross = '+str(cross))
plt.show()