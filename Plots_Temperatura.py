import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

datos=np.genfromtxt("DT.txt", delimiter=",")
n=9409

def graficar(di, df,caso,tiempo,f):
	T=datos[di:df,2:5]
	fig=plt.figure()
	ax=fig.add_subplot(111, projection="3d")
	surf1=ax.plot_wireframe(T[:,0],T[:,1],T[:,2])
	ax.set_zlabel("Temperatura (C)")
	ax.set_title("CASO "+str( caso)+", t= "+str(tiempo)+"s, frontera "+f)
	if(caso==1 and tiempo==2500):
		ax.set_zlim(50, 100)
	#plt.show()
	plt.savefig("CASO"+str(caso)+"t"+str(tiempo)+"sfrontera"+f+".png",format='png')	
	plt.close()

#CASO 1 CERRADO
graficar(0,9408,1,0,"Cerrada")
graficar(9409,18817,1,100,"Cerrada")
graficar(18818,28226,1,2500,"Cerrada")

#CASO 1 PERIODICO
graficar(28227,37635,1,0,"Periodica")
graficar(37636,47044,1,100,"Periodica")
graficar(47045,56453,1,2500,"Periodica")

#CASO 1 ABIERTO
graficar(56454,65862,1,0,"Abierta")
graficar(65863,75271,1,100,"Abierta")
graficar(75272,84680,1,2500,"Abierta")

#CASO 2 CERRADO
graficar(84681,94089,2,0,"Cerrada")
graficar(94090,103498,2,100,"Cerrada")
graficar(103499,112907,2,2500,"Cerrada")

#CASO 2 PERIODICO
graficar(112908,122316,2,0,"Periodica")
graficar(122317,131725,2,100,"Periodica")
graficar(131726,141134,2,2500,"Periodica")

#CASO 2 ABIERTO
graficar(141135,150543,2,0,"Abierta")
graficar(150544,159952,2,100,"Abierta")
graficar(159953,169361,2,2500,"Abierta")


#CASO 1 PROMEDIO
time=np.linspace(0,2500,10000)
plt.plot(time[:-1],datos[169362:179361,1],color='blue')
plt.plot(time[:-1],datos[179362:189361,1],color='red')
plt.plot(time[:-1],datos[189362:199361,1],color='green')
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura media (C)")
plt.legend(["Cerrada","Periodica","Abierta"])
plt.title("Temperatura media Caso 1")
plt.savefig("Caso1Mean.png",format='png')
plt.close()

#CASO 2 PROMEDIO
plt.plot(time[:-1],datos[199362:209361,1],color='blue')
plt.plot(time[:-1],datos[209362:219361,1],color='red')
plt.plot(time[:-1],datos[219362:229361,1],color='green')
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura media (C)")
plt.legend(["Cerrada","Periodica","Abierta"])
plt.title("Temperatura media Caso 2")
plt.savefig("Caso2Mean.png",format='png')
plt.close()


