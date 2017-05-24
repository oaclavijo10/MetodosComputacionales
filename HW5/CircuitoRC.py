import numpy as np
import matplotlib.pyplot as plt
datos=np.loadtxt("CircuitoRC.txt")
t=datos[:,0]
q=datos[:,1]

#Modelos
def likelihood(y_obs, y_model):
    chi_squared = (1.0/2.0)*np.sum(((y_obs-y_model)**2)/y_model)
    return np.exp(-chi_squared)
def model(t,R,C):
    return 10*C*(1-np.exp(-t/(R*C)))

#Estimacion bayesiana
R_walk = np.empty((0))
C_walk = np.empty((0))
L_walk = np.empty((0))
R_walk = np.append(R_walk, 10)
C_walk = np.append(C_walk, 10)
y_init = model(t, R_walk[0], C_walk[0])
L_walk = np.append(L_walk, likelihood(q, y_init))
n = 10000
for i in range(n):
    R_prime = np.random.normal(R_walk[i], 0.1) 
    C_prime = np.random.normal(C_walk[i], 0.1)

    y_init = model(t, R_walk[i], C_walk[i])
    y_prime = model(t, R_prime, C_prime)
    L_prime = likelihood(q, y_prime)
    L_init = likelihood(q, y_init)
    alpha = L_prime/L_init
    if(alpha>=1.0):
        R_walk = np.append(R_walk,R_prime)
        C_walk = np.append(C_walk,C_prime)
        L_walk = np.append(L_walk, L_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            R_walk = np.append(R_walk,R_prime)
            C_walk = np.append(C_walk,C_prime)
            L_walk = np.append(L_walk, L_prime)
        else:
            R_walk = np.append(R_walk,R_walk[i])
            C_walk = np.append(C_walk,C_walk[i])
            L_walk = np.append(L_walk, L_init)

#Graficas y histogramas
plt.scatter(R_walk, -np.log(L_walk))
plt.title("R en funcion del Likelihood")
plt.xlabel("R (Ohms)")
plt.ylabel("-Log Likelihood")
plt.savefig("RL.pdf",format='pdf')
plt.close()
plt.scatter(C_walk, -np.log(L_walk))
plt.title("C en funcion del Likelihood")
plt.xlabel("C (F)")
plt.ylabel("-Log Likelihood")
plt.savefig("CL.pdf",format='pdf')
plt.close()
plt.hist(R_walk, 20, normed=True)
plt.title("Histograma de R")
plt.savefig("RH.pdf",format='pdf')
plt.close()
plt.hist(C_walk, 20, normed=True)
plt.title("Histograma de C")
plt.savefig("CH.pdf",format='pdf')
plt.close()

#Fit
max_likelihood_id = np.argmax(L_walk)
best_R = R_walk[max_likelihood_id]
best_C = C_walk[max_likelihood_id]
best_y = model(t, best_R, best_C)
plt.scatter(t,q)
plt.plot(t, best_y,c='black')
plt.title("Mejor modelo. R="+str(np.round(best_R,5))+" Ohms,C="+str(np.round(best_C,5))+" F,L="+str(np.round(np.log10(L_walk[max_likelihood_id]),5)))
plt.xlabel("Tiempo")
plt.ylabel("Carga (C)")
plt.savefig("Fit.pdf",format='pdf')
plt.close()
