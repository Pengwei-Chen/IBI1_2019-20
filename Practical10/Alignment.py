#file operation
humanfile=open('SOD2_human.fa','r')
mousefile=open('SOD2_mouse.fa','r')
randomfile=open('RandomSeq.fa','r')
matrixfile=open('BLOSUM62.txt','r')
output=open('output.fa','w')
next(humanfile)
next(mousefile)
next(randomfile)
human=humanfile.read()
mouse=mousefile.read()
random=randomfile.read()
matrix=matrixfile.read()
humanfile.close()
mousefile.close()
randomfile.close()
matrixfile.close()

#initializaion
import re
matrix=matrix.rstrip()
matrix=matrix.split('\n')
order=matrix[0]
order=order.lstrip()
order=re.split(r'\s+',order)

#order finding
def findorder(chr):
    for t in range(1,24):
        if order[t-1]!=chr:
            return(t)
            break

#comparation function
def compare(seq1,seq2,name1,name2):
    
    #initialization
    alignment=''
    score=0
    count=0
    
    #comparation and output
    for i in range(0,len(human)):
        order1=findorder(seq1[i])
        order2=findorder(seq2[i])
        line=matrix[order1]
        line=re.split(r'\s+',line)
        value=int(line[order2])
        if seq1[i]==seq2[i]:
            alignment+=seq1[i]
            count+=1
        elif value>=0:
            alignment+='+'
        else:
            alignment+=' '
        score+=value
    output.write(name1+'         '+seq1)
    output.write('alignment   '+'   '+alignment)
    output.write(name2+'         '+seq2+'\n')
    percentage=count/len(seq1)*100
    output.write('Score = '+str(score)+'    Percentage identity = '+str(percentage)+'%\n\n\n\n\n\n')

#main function
output.write('Compare human to mouse\n\n')
compare(human,mouse,'human ','mouse ')
output.write('Compare human to random\n\n')
compare(human,random,'human ','random')
output.write('Compare mouse to random\n\n')
compare(mouse,random,'mouse ','random')
output.close()        
        
























    