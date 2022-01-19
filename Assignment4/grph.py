#importing for reading fasta format
from Bio import SeqIO

#last symbols
suffixes = []  
#first symbols 
prefixes = []

#opeing file
f = open('dati.txt', 'r')  

for k in SeqIO.parse(f, 'fasta'):
    #count for O
    count1 = 0
    count2 = 0

    prefix = [k.id]
    suffix = [k.id]

    #storage
    pre = ''
    suf = ''

    #for each DNA sequence in the file 
    for x in k.seq:
        #O3 given by rosalind 
        if count1 < 3:
            pre += x
            count1 += 1
    prefix.append(pre)

    #for each reversed DNA sequence in the file
    for y in reversed(k.seq):
        #O3 given by rosalind
        if count2 < 3:
            suf += y
            count2 += 1                                                
    suffix.append(''.join(reversed(suf)))

    prefixes.append(prefix)
    suffixes.append(suffix)
#close file 
f.close()
                                                                       
for a, b in enumerate(suffixes):
    suff = suffixes[a][1]
    id = suffixes[a][0]
    for c, d in enumerate(prefixes):
        if suff == prefixes[c][1] and id != prefixes[c][0]:
            print(id, prefixes[c][0])