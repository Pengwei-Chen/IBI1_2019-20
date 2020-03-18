import matplotlib.pyplot as plt
str=input("gene_lengths=")
str=str.strip("[]")
Length=str.split(",")
for i in range(0,len(Length)):
    Length[i]=int(Length[i])
Length.sort()
del(Length[0])
del(Length[len(Length)-1])
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
