#opening files
with open("dati.txt","r") as f:
    f.readline()
    dna=''
    for line in f:
        dna+=line.strip()

#defining function 
def protein(inp):
            
    #dictionary with corresponding triplets
    codons = {
        "TTT":"F", "CTT":"L", "ATT":"I", "GTT":"V",
        "TTC":"F", "CTC":"L", "ATC":"I", "GTC":"V",
        "TTA":"L", "CTA":"L", "ATA":"I", "GTA":"V",
        "TTG":"L", "CTG":"L", "ATG":"M", "GTG":"V",
        "TCT":"S", "CCT":"P", "ACT":"T", "GCT":"A",
        "TCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
        "TCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
        "TCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
        "TAT":"Y", "CAT":"H", "AAT":"N", "GAT":"D",
        "TAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
        "TAA":"STOP", "CAA":"Q", "AAA":"K", "GAA":"E",
        "TAG":"STOP", "CAG":"Q", "AAG":"K", "GAG":"E",
        "TGT":"C", "CGT":"R", "AGT":"S", "GGT":"G",
        "TGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
        "TGA":"STOP", "CGA":"R", "AGA":"R", "GGA":"G",
        "TGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
        }

    #reversing dna and complementing it
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rnareverse = ''.join(complement[c] for c in reversed(dna))
    
    #rna
    rna=''.join(dna)
    
    answer= []

    for x in range(len(rna)-2):
        #start codon 
        if rna[x:x+3]=='ATG':
            k=x
            #storage
            solution=''
            triplet='ATG'
            #until we find stop codon
            while codons[triplet]!="STOP":
                solution+=codons[triplet]
                k+=3
                if k>len(rna)-3:
                    break
                triplet=rna[k:k+3]
            if codons[triplet]=="STOP" and solution not in answer:
                answer.append(solution)

    #same but for the reverse
    for i in range(len(rnareverse)-2):
        #start codon 
        if rnareverse[i:i+3]=='ATG':
            z=i
            prot=''
            triplet='ATG'
            #stop codon
            while codons[triplet]!="STOP":
                prot+=codons[triplet]
                z+=3
                if z>len(rnareverse)-3:
                    break
                triplet=rnareverse[z:z+3]
            if codons[triplet]=="STOP" and prot not in answer:
                answer.append(prot)

    for result in answer:
        print(result)

#taking input
#print rna of the input 
a =(protein(f))
print(a)