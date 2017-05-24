import numpy as np
import matplotlib.pyplot as plt
datos=np.loadtxt("Canal_ionico.txt")
x=datos[:,0]
y=datos[:,1]
datos1=np.loadtxt("Canal_ionico1.txt")
x1=datos1[:,0]
y1=datos1[:,1]

#Modelo
def model(x,y,h,k):
    return np.ndarray.min(((x-h)**2+(y-k)**2)**(0.5)-1)

#Algoritmo Metropolis
H_walk = np.empty((0))
K_walk = np.empty((0))
R_walk = np.empty((0))
H_walk = np.append(H_walk, 4.0)
K_walk = np.append(K_walk, 4.0)
R_init = model(x,y, H_walk[0], K_walk[0])
H1_walk = np.empty((0))
K1_walk = np.empty((0))
R1_walk = np.empty((0))
H1_walk = np.append(H1_walk, 6.0)
K1_walk = np.append(K1_walk, 6.0)
R1_init = model(x1,y1, H1_walk[0], K1_walk[0])
n = 10000
for i in range(n):
    H_prime = np.random.normal(H_walk[i], 0.1) 
    K_prime = np.random.normal(K_walk[i], 0.1)
    R_init = model(x,y, H_walk[i], K_walk[i])
    R_prime = model(x,y, H_prime, K_prime)
    alpha = R_prime/R_init
    
    H1_prime = np.random.normal(H1_walk[i], 0.1) 
    K1_prime = np.random.normal(K1_walk[i], 0.1)
    R1_init = model(x1,y1, H1_walk[i], K1_walk[i])
    R1_prime = model(x1,y1, H1_prime, K1_prime)
    alpha1 = R1_prime/R1_init
    if(alpha>=1.0):
        H_walk = np.append(H_walk,H_prime)
        K_walk = np.append(K_walk,K_prime)
        R_walk = np.append(R_walk,R_prime)
    else:
        beta = np.random.random()
        if(beta>=alpha):
            H_walk = np.append(H_walk, H_prime)
            K_walk = np.append(K_walk, K_prime)
            R_walk = np.append(R_walk, R_prime)
        else:
            H_walk = np.append(H_walk, H_walk[i])
            K_walk = np.append(K_walk, K_walk[i])
            R_walk = np.append(R_walk, R_init)

    if(alpha1>=1.0):
        H1_walk = np.append(H1_walk,H1_prime)

        K1_walk = np.append(K1_walk,K1_prime)
        R1_walk = np.append(R1_walk,R1_prime)
    else:
        beta1 = np.random.random()
        if(beta1>=alpha1):
            H1_walk = np.append(H1_walk, H1_prime)
            K1_walk = np.append(K1_walk, K1_prime)
            R1_walk = np.append(R1_walk, R1_prime)
        else:
            H1_walk = np.append(H1_walk, H1_walk[i])
            K1_walk = np.append(K1_walk, K1_walk[i])
            R1_walk = np.append(R1_walk, R1_init)
#Graficas            
plt.hist(H_walk, 20, normed=True)
plt.title("Histograma de X")
#plt.show()
plt.savefig("XH.pdf",format='pdf')
plt.close()
plt.hist(K_walk, 20, normed=True)
plt.title("Histograma de Y")
#plt.show()
plt.savefig("YH.pdf",format='pdf')
plt.close()

plt.hist(H1_walk, 20, normed=True)
plt.title("Histograma de X1")
#plt.show()
plt.savefig("X1H.pdf",format='pdf')
plt.close()
plt.hist(K1_walk, 20, normed=True)
plt.title("Histograma de Y1")
#plt.show()
plt.savefig("Y1H.pdf",format='pdf')
plt.close()

#Fit
maxR = np.argmax(R_walk)
best_H = H_walk[maxR]
best_K = K_walk[maxR]
best_R=model(x,y,best_H,best_K)
orig=plt.scatter(x,y)
punto=plt.scatter(best_H,best_K,c='red')
circ=plt.Circle((best_H,best_K), radius=best_R, color='red', fill=False)
plt.title("Mejor modelo. x="+str(np.round(best_H,4))+", y="+str(np.round(best_K,4))+", R="+str(np.round(best_R,4)))
plt.xlabel("X")
plt.ylabel("Y")
ax = plt.gca()
ax.add_artist(orig)
ax.add_artist(punto)
ax.add_artist(circ)
ax.set_xlim((-7, 17))
ax.set_ylim((-7, 17))
#plt.show()
plt.savefig("FitCircle.pdf",format='pdf')
plt.close()

maxR1 = np.argmax(R1_walk)
best_H1 = H1_walk[maxR1]
best_K1 = K1_walk[maxR1]
best_R1=model(x1,y1,best_H1,best_K1)
orig1=plt.scatter(x1,y1)
punto1=plt.scatter(best_H1,best_K1,c='red')
circ1=plt.Circle((best_H1,best_K1), radius=best_R1, color='red', fill=False)
plt.title("Mejor modelo. x="+str(np.round(best_H1,4))+", y="+str(np.round(best_K1,4))+", R="+str(np.round(best_R1,4)))
plt.xlabel("X")
plt.ylabel("Y")
ax = plt.gca()
ax.add_artist(orig1)
ax.add_artist(punto1)
ax.add_artist(circ1)
ax.set_xlim((-7, 17))
ax.set_ylim((-7, 17))
#plt.show()
plt.savefig("FitCircle1.pdf",format='pdf')
plt.close()
