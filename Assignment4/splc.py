from Bio import SeqIO
#dictionary with protein correspondant to triplets 
codice =  {
        'UUU' : 'F', 'UUC': 'F', 
        'UUA' : 'L', 'UUG' : 'L', 
        'UCU' : 'S', 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 
        'UAU' : 'Y', 'UAC': 'Y', 
        'UAA': 'STOP', 'UAG': 'STOP', 
        'UGU' : 'C', 'UGC': 'C', 
        'UGA' : 'STOP', 
        'UGG': 'W', 
        'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 
        'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 
        'CAU' : 'H', 'CAC':'H', 
        'CAA':'Q','CAG':'Q',
        'CGU': 'R','CGC':'R','CGA':'R','CGG':'R',
        'AUU':'I','AUC':'I','AUA':'I',
        'AUG':'M',
        'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
        'AAU':'N','AAC':'N',
        'AAA':'K','AAG':'K',
        'AGU':'S','AGC':'S',
        'AGA':'R','AGG':'R',
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
        'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAU':'D','GAC':'D',
        'GAA':'E','GAG':'E',
        'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
}

#store sequences 
sequences = []
#open file
f = open('dati.txt', 'r')
#reading fasta format
for x in SeqIO.parse(f, 'fasta'):
    sequences.append(str(x.seq))

dna_string = sequences[0] #sequence 
introns = sequences[1:] #introns 

for intron in introns:
    dna_string = dna_string.replace(intron,"") #erase introns
dna_string = dna_string.replace("T","U") #turn dna into rna. convert T in U 

#print result
for x in range(0, len(dna_string) -3, 3): #stop codon is removed --> - 3
    print(codice[dna_string[x: x+3]], end='') #print on one line