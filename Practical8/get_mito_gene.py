import re
print('progressing...')
read=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
wri=open('mito_gene.fa','w')
line=read.readline()
count=0
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
                out='Length:'+str(count)
                wri.write(out)
                break
            if line.startswith('>'):
                out='Length:'+str(count)+'\n'
                wri.write(out)
                count=0
                break
            count+=len(line)-1
    if not line:
        break
read.close()
wri.close()
print('done!')