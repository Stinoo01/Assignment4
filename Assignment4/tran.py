from Bio import SeqIO

#store sequences              
lines = []

#opening file
f = open('dati.txt', 'r') 
#takes name file and format
for x in SeqIO.parse(f, 'fasta'):
    #appending sequecnes 
    lines.append(str(x.seq))

#defining the two sequences
sequence1 = lines[0] #first 
sequence2 = lines[1] #second

#dictionaries with transition and transvertion
transition = {
    'A':'G', 
    'G':'A', 
    'T':'C', 
    'C':'T'
    }

transversion = {
    'A':('T','C'), 
    'G':('T','C'), 
    'T':('A','G'), 
    'C':('A','G')
    }

#defining function
def conversion(sequence1, sequence2):
    #storing values
    #tot transitions
    tot_transitions = 0
    #tot transversions
    tot_transversion = 0

    for y,i in zip(sequence1, sequence2):
        if transition[y] == i:
          tot_transitions += 1 
        elif i in transversion[y]:
          tot_transversion += 1
    #ratio tot n transition and transversions 
    return (tot_transitions/tot_transversion)

print(conversion(sequence1, sequence2))