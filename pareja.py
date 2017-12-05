'''
  *Esta funcion se encarga de seleccionar los mejores individuos,
  *luego los cruza y finalmente los cruza.
'''
import numpy as np

def pareja(n,rank,mut,cross,AG):
	hijo = np.zeros((rank.size))
	hijo[0] = n[np.argmax(rank)]
	i=1
	while i<(rank.size//2):
		#Ruleta al padre
		aux = np.random.rand()*(np.sum(rank))
		padre = -1
		while aux>0:
			padre += 1
			aux = aux - rank[padre]
		#Ruleta a la madre
		aux = np.random.rand()*(np.sum(rank))
		madre = -1
		while aux>0:
			madre += 1
			aux = aux - rank[madre]
		#Creo los hijos
		hijo[(i*2)-1] = n[padre]
		hijo[(i*2)] = n[madre]
		#Probabilidad de cruzamiento
		c = np.random.rand()
		#print("\n Un par de valores antes del Cruzamineto del AG : "+str(AG))
		#print(bin(int(hijo[(i*2)-1])))
		#print(bin(int(hijo[(i*2)])))
		if c<cross:
			cp = (2**(np.random.randint(63)))-1 #000011111
			hijo[(i*2)-1] = (n[padre]&~cp)|(n[madre]&cp)
			hijo[(i*2)] = (n[madre]&~cp)|(n[padre]&cp)
			#print("\n Un par de valores despues del Cruzamineto del AG : "+str(AG))
			#print(bin(int(hijo[(i*2)-1])))
			#print(bin(int(hijo[(i*2)])))
		#Probabilidad de mutamiento
		m = np.random.rand()
		if m<mut:
			mp = 2**(np.random.randint(63))
			if np.random.randint(2):
				hijo[(i*2)-1] = int(hijo[i*2]-1)^mp
			else:
				hijo[(i*2)] = int(hijo[(i*2)])^mp
			#print("\n Un par de valores despues de la mutacion del AG : "+str(AG))
			#print(bin(int(hijo[(i*2)-1])))
			#print(bin(int(hijo[(i*2)])))
		i = i+1
	return hijo