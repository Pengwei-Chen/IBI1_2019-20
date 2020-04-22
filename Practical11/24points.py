#recursive function
def calculate(numbers):
    global found
    global times
    if len(numbers)==1:
        if numbers[0]>23.999 and numbers[0]<24.001:#because division may cause deviation
            found=True
        return
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            
            #create a list without i and j(so that i+j,i-j... can be appended to it)
            numbers_except=[]
            for k in range(0,len(numbers)):
                if k!=i and k!=j:
                    numbers_except.append(numbers[k])
            #(I don't understand why 'del' and 'remove' also change 'numbers')

            #next turn recursion
            
            #+
            numbers_next=numbers_except+[numbers[i]+numbers[j]]
            calculate(numbers_next)
            times+=1
                    
            #-
            if found==False:
                if numbers[i]>numbers[j]:
                    numbers_next=numbers_except+[numbers[i]-numbers[j]]
                    calculate(numbers_next)
                    times+=1
                else:
                    numbers_next=numbers_except+[numbers[j]-numbers[i]]
                    calculate(numbers_next)
                    times+=1
                    
            #*
            if found==False:
                numbers_next=numbers_except+[numbers[i]*numbers[j]]
                calculate(numbers_next)
                times+=1
                
            #/
            if found==False:
                if numbers[j]!=0:
                    numbers_next=numbers_except+[numbers[i]/numbers[j]]
                    calculate(numbers_next)
                    times+=1
                if numbers[i]!=0:
                    numbers_next=numbers_except+[numbers[j]/numbers[i]]
                    calculate(numbers_next)
                    times+=1
    return

#main
while True:
    outrange=False
    read=input("Please input numbers to compute 24:(use ',' to divide them)\n")
    cards= read.split(',')
    
    for i in range(0,len(cards)):
        cards[i]=int(cards[i])
        if cards[i]<1 or cards[i]>23:
            outrange=True
            print('The input number must be integers from 1 to 23')
            break
    if outrange==False:
        break
found=False
times=0
calculate(cards)
times+=1
if found:
    print('Yes')
else:
    print('No')
print('Recursion times: '+str(times))