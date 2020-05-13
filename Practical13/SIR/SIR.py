#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

#define basic variables
N=10000
suscept=9999
infect=1
recover=0
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

#random choice
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

#draw figure
x=[]
ys=[]
yi=[]
yr=[]
for i in range(1001):
    x.append(i)
    ys.append(time.suscept[i])
    yi.append(time.infect[i])
    yr.append(time.recover[i])
plt.figure(figsize=(6,4),dpi=150)
plt.plot(x,ys,linewidth=2,label='susceptiable')
plt.plot(x,yi,linewidth=2,label='infected')
plt.plot(x,yr,linewidth=2,label='recovered')
plt.title('SIR model',fontsize=20)
plt.xlabel('time',fontsize=12)
plt.ylabel('number of people',fontsize=12)
plt.tick_params(axis='both',labelsize=10)
plt.legend(loc='upper right')
plt.savefig(r'D:\figure.png',type='png')





















