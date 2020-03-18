#initialize
import matplotlib.pyplot as plt

#input
str=input("gene_lengths=")

#simple processing of input
str=str.strip("[]")

#divide and transfer into "Length"
Length=str.split(",")

#digitalize
for i in range(0,len(Length)):
    Length[i]=int(Length[i])

#sort
Length.sort()
Length.reverse()

#delete the longest	and	shortest
del(Length[0])
del(Length[len(Length)-1])

#output
print(Length)
plt.boxplot(Length,
            vert=True,
            whis = 1.5,
            patch_artist=True,
            boxprops={"color":"black","facecolor":"lightblue"},
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show
