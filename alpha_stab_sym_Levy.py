import numpy as np

#### comments on implementation: ####

#constraints: 
# time_zero == 0
# seq_len = len(G) = len(W)
# alpha \in (0,2]

# core method:
""" def alpha_stab_levy(times, alpha, G,W ):
    inc=[0]
    N=len(times)
    for i in range(N-1):
        inc.append((times[i+1]-times[i])**(1/alpha)*(np.sin(alpha*G[i]))/((np.cos(G[i]))**(1/alpha))*((np.cos((1-alpha)*G[i]))/(W[i]))**((1-alpha)/(alpha)))
    return np.cumsum(inc) """

#EXAMPLE:  direct usage of the methods "alpha_stab_levy"
""" time_zero = 0
horizon = 1
seq_len = 100
times=[i*horizon/seq_len for i in range(time_zero,seq_len)]
low=-np.pi/2
high=np.pi/2
G=np.random.uniform(low,high,seq_len)
W=np.random.exponential(1,seq_len)
alpha = 1.1
path=alpha_stab_levy(times,alpha,G,W)
#plt.plot(path) """
####                              ####


class AlphaStabSymLevy():
    
    def __init__(self,XXX,alpha,switch="seq_len"):
        if switch == "seq_len":
            self.seq_len = XXX[0]
            self.time_horizon = XXX[1]
            self.times = [i*self.time_horizon/self.seq_len for i in range(self.seq_len)]
        elif switch == "times":
            self.times = XXX
            self.seq_len = len(self.times)-1
        else:
            print("ERROR")
            
        self.alpha = alpha
    
    def alpha_stab_levy(self, times, alpha, G,W ):
        inc=[0]
        N=len(times)
        for i in range(N-1):
            inc.append((times[i+1]-times[i])**(1/alpha)*(np.sin(alpha*G[i]))/((np.cos(G[i]))**(1/alpha))*((np.cos((1-alpha)*G[i]))/(W[i]))**((1-alpha)/(alpha)))
        return np.cumsum(inc)
    
    def __call__(self):
        low=-np.pi/2
        high=np.pi/2
        G=np.random.uniform(low,high,self.seq_len)
        W=np.random.exponential(1,self.seq_len)
        path = self.alpha_stab_levy(self.times,self.alpha,G,W)
        return path

#EXAMPLES:

#import matplotlib.pyplot as plt

#EXAMPLE 1:

#levy = AlphaStabSymLevy([1000,1],1.3)
#plt.plot(levy())

#EXAMPLE 2:

#horizon = 1
#seq_len = 1000
#times=[i*horizon/seq_len for i in range(seq_len)]
#levy_t = AlphaStabSymLevy(times,1.3,switch="times")
#plt.plot(levy_t())
