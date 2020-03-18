import matplotlib.pyplot as plt
A=input("A=")
C=input("C=")
G=input("G=")
T=input("T=")
dictionary={"A":A,"C":C,"G":G,"T":T}
labels="A","C","G","T"
sizes=A,C,G,T
explode=(0,0,0,0)
print(dictionary)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",
        shadow=True,startangle=50)
plt.axis("equal")
plt.show