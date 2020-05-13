#show progress
print('Progressing...')

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#create population array
population=np.zeros((100,100))

#choose outbreak point
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

#record infected location in a list
infloc=[]
infloc.append([outbreak[0],outbreak[1]])

#create figure
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='Blues',interpolation='nearest')
plt.savefig(r'D:\time=0.png')

#define basic variables
N=10000
beta=0.1 #reduced because too fast
gamma=0.05
day=0

for time in range(1,101):
    #infection and recovering incidences in a time point
    #susceptiable to infected with possibility
    for loc in infloc:
        #neighbors
        for i in range(loc[0]-1,loc[0]+2):
            for j in range(loc[1]-1,loc[1]+2):
                if i>-1 and i<100 and j>-1 and j<100:
                    #infect with possibility if not infected
                    if population[i,j]==0:
                        infection=np.random.choice(range(2),1,p=(1-beta,beta))
                        if infection==1:
                            population[i,j]=1
                            infloc.append([i,j]) 
        
        #infected to recovered with possibility
        if population[loc[0],loc[1]]==1:
            recovering=np.random.choice(range(2),1,p=(1-gamma,gamma))
            if recovering==1:
                population[loc[0],loc[1]]=2
                infloc.remove(loc) #it will not affect loop 'for loc in infloc'

#save image of key points
    if time==25 or time==50 or time==75 or time==100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='Blues',interpolation='nearest')
        plt.savefig(r'D:\time='+str(time)+'.png')

#show progress
print('Done!')






















