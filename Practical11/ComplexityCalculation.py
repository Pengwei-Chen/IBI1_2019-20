#recursive function
def calculate(numbers):
    global times
    if len(numbers)==1:
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
            if numbers[i]>numbers[j]:
                numbers_next=numbers_except+[numbers[i]-numbers[j]]
                calculate(numbers_next)
                times+=1
            else:
                numbers_next=numbers_except+[numbers[j]-numbers[i]]
                calculate(numbers_next)
                times+=1
                    
            #*
            numbers_next=numbers_except+[numbers[i]*numbers[j]]
            calculate(numbers_next)
            times+=1
                
            #/
            numbers_next=numbers_except+[numbers[i]/numbers[j]]
            calculate(numbers_next)
            times+=1
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

    if outrange==False:
            break
times=0
calculate(cards)
times+=1
print('Recursion times: '+str(times))