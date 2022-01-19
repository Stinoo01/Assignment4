#taking inputs from rosalind
a = 94
b = 9

count = 1
for x in range(b):
    count = count * (a - x)
#print divided by modulo 
print(count % 1000000)