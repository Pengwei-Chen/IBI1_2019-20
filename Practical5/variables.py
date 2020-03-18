a=123
b=123123
if b%7==0:
    print("b can be divided by 7")
else:
    print("b can't be divided by7")
c=b/7
d=c/11
e=d/13
if a>e:
    print("a is larger")
elif a<e:
    print("e is larger")
else:
    print("a is equal to e")
for i in range (0,2):
    for j in range (0,2):
        if i==0:
            X=False
        else:
            X=True
        if j==0:
            Y=False
        else:
            Y=True
        Z=(X	and	not	Y)	or	(Y	and	not	X)
        W=X!=Y
        if W==Z:
            print("= ",end="")
        else:
            print("<> ",end="")
    print()
