import numpy as np 
import matplotlib.pyplot as plt
import toCart as tc
def plotArray(x):
	ax = plt.subplot()
	#ax.plot(0,0,color = 'g',linewidth = 30)
	for i in range(0,len(x)-1):
		ax.scatter(x[:,1],x[:,0],color = 'r',linewidth = 1)
                #ax.plot(x[:,1],x[:,0],color = 'r',linewidth=1)
                #ax.axis('off')
	ax.grid(False)
	plt.show()


