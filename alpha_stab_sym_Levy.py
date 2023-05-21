import numpy as np
#import matplotlib.pyplot as plt

def stab_transf(G,W,alpha):
    val=(np.sin(alpha*G))/((np.cos(G))**(1/alpha))*((np.cos((1-alpha)*G))/(W))**((1-alpha)/(alpha))
    return val

def alpha_stab_levy(times, alpha, G,W ):
    inc=[0]
    N=len(times)
    for i in range(N-1):
        inc.append((times[i+1]-times[i])**(1/alpha)*(np.sin(alpha*G[i]))/((np.cos(G[i]))**(1/alpha))*((np.cos((1-alpha)*G[i]))/(W[i]))**((1-alpha)/(alpha)))
    return np.cumsum(inc)

#constraints: 
# time_zero == 0
# seq_len = len(G) = len(W)
# alpha \in (0,2] 


time_zero = 0
horizon = 1
seq_len = 100
times=[i*horizon/seq_len for i in range(time_zero,seq_len+1)]
low=-np.pi/2
high=np.pi/2
G=np.random.uniform(low,high,seq_len)
W=np.random.exponential(1,seq_len)
alpha = 1.1
path=alpha_stab_levy(times,alpha,G,W)
#plt.plot(path)