seq='ATGCGACTACGATCGAGGGCCAT'
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
print(rc)