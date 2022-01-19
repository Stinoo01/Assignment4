#importing
from urllib.request import urlopen
from Bio import SeqIO
import re

#storing lines here 
ID = []

#fasta format
with open('dati.txt') as f:
    for line in f:
        ID.append(line.strip())


for x in range(len(ID)):
    #creating link for each input 
    URL = 'http://www.uniprot.org/uniprot/' + ID[x] + '.fasta'
    data = urlopen(URL)
    #decoding
    fasta = data.read().decode()
    #creating and writing a new file 
    with open('dati.fasta', 'a') as text_file:
        text_file.write(fasta) 

#opening the newly created file                                                              
file = open('dati.fasta', 'r')

#n-glycosylation motif   
#motif is given by rosalind
motifs = re.compile(r'(?=(N[^P][ST][^P]))')

count = 0  

for y in SeqIO.parse(file, 'fasta'): 
    #extracting sequences
    sequence = y.seq 
    positions = []

    for k in re.finditer(motifs, str(sequence)):     
            #starts from 0 so have to add 1                 
            positions.append(k.start() + 1) 

    if len(positions) > 0:                  
        print(ID[count]) 
        print(' '.join(map(str, positions))) 
    count += 1 
 