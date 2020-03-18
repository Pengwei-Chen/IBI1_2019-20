import random
x=random.randint(1,8192)
print(x,end=" is ")
m=x
n=0
string=""
while m!=0:
    n=m%2
    m=m//2
    string=str(n)+string
for i in range(0,len(string)):
    if string[i]=="1":
        print("2**"+str(len(string)-i-1),end="")
        for j in range (i+1,len(string)):
            if string[j]=="1":
                print(" + ",end="")
                break
            