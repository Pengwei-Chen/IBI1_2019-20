#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#define basic variables
N=10000
beta=0.3
gamma=0.05
day=0

#define a class for record
class timecourse:
    suscept=[0 for i in range(1001)]
    infect=[0 for i in range(1001)]
    recover=[0 for i in range(1001)]
    def __init__(self,suscept,infect,recover,day):
        self.suscept[day]=suscept
        self.infect[day]=infect
        self.recover[day]=recover
    def timepoint(self,suscept,infect,recover,day):
        self.suscept[day]=suscept
        self.infect[day]=infect
        self.recover[day]=recover
time=timecourse(9999,1,0,0)

#create plot
plt.figure(figsize=(6,4),dpi=150)

#try different vaccination rates
for percentage in range(0,11):
    
    #initialize values
    infect=1
    recover=0
    suscept=int((10000-infect)*(1-percentage*0.1))
    
    #randomize
    for day in range(1,1001):
        si=np.random.choice(range(2),suscept,p=[1-beta*infect/N,beta*infect/N])
        ir=np.random.choice(range(2),infect,p=[1-gamma,gamma])
        
        #record
        for i in si:
            if i==1:
                suscept-=1
                infect+=1
        for i in ir:
            if i==1:
                infect-=1
                recover+=1
        time.timepoint(suscept,infect,recover,day)

    #add curve
    x=[]
    y=[]
    for i in range(1001):
        x.append(i)
        y.append(time.infect[i])

    plt.plot(x,y,linewidth=1,label=str(percentage*10)+'%')

#draw figure
#plt.title('SIR model with different vaccination rates',fontsize=20)
plt.title('SIR model with different vaccination rates',fontsize=20,color=cm.viridis(30))
plt.xlabel('time',fontsize=12)
plt.ylabel('number of infected people',fontsize=12)
plt.tick_params(axis='both',labelsize=10)
plt.legend(loc='upper right')
plt.savefig(r'D:\figure.png',type='png')





















