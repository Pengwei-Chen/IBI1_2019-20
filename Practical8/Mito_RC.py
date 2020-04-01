import re
rea=input('Please enter a filename for the new fasta file      ')
print('Progressing...')
read=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
wri=open(rea,'w')
line=read.readline()
lines=''
count=0
def RC(seq):
    com=''
    rc=''
    for i in range (0,len(seq)):
        if seq[i]=='A':
            com+='T'
        elif seq[i]=='T':
            com+='A'
        elif seq[i]=='C':
            com+='G'
        elif seq[i]=='G':
            com+='C'
    for i in range (len(seq)-1,-1,-1):
        rc+=com[i]
    return(rc)

while True:
    if line.startswith('>'):
        write=re.findall(r' gene:(.+) gene_biotype:',line)
        name=write[0]
        name.lstrip('['"'")
        name.rstrip(']'"'")
        n=30-len(name)
        out='Name:'+name
        wri.write(out)
        for i in range (0,n):
            out=' '
            wri.write(out)
        while True:
            line=read.readline()
            if not line:
                out='Length:'+str(count)+'\n'
                wri.write(out)
                out=lines
                wri.write(out)
                break
            if line.startswith('>'):
                out='Length:'+str(count)+'\n'
                wri.write(out)
                out=lines+'\n\n'
                wri.write(out)
                count=0
                lines=''
                break
            lines+=RC(line.rstrip())
            count+=len(line)-1
    if not line:
        break
read.close()
wri.close()
print('done!')