#design a program
import random
n=random.randint(2,100)
while n!=1:#loop
    print(n)
    if n%2==0:#odd or even -> different operation
        n=n//2
    else:
        n=n*3+1
print("1")#complement the sequence