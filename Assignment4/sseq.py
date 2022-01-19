from Bio import SeqIO
#store sequences 
sequences = []
#open data 
f = open('dati.txt', 'r')
#reading fasta format
for x in SeqIO.parse(f, 'fasta'):
    sequences.append(str(x.seq))

#identify sequence and substring
sequence = sequences[0] #sequence 
substring = sequences[1] #substring

#storage
count = 0 
#storage numbers
positions = []
#searching in the substring
for y in range(len(substring)):
    #searching in sequence 
    for z in range(count, len(sequence)):
        count += 1
        if len(positions) < len(substring): #continue
            if substring[y] == sequence[z]: #if they are equal 
                positions.append(count) #add and break and then start again
                break

#fixing output 
result = str(positions)
result = result.replace(',','').replace('[','').replace(']','')
#print result
print(result)
