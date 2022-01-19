from Bio import SeqIO
from math import factorial 

#store here the sequence
sequence = ''
#opening file 
f = open('dati.txt', 'r')
#adjusting fasta formata
for line in SeqIO.parse(f, 'fasta'):
    sequence = str(line.seq)

#store values
AU = 0
GC = 0

for x in sequence:
    #A will be same number of U
    if x == 'A':
        AU += 1
    #G will be same number of C
    elif x == 'G':
        GC += 1

#doing calculations
result = (factorial(AU) * factorial(GC))

#printing result
print(result)