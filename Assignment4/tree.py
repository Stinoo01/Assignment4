#storing data 
data = []
#opening file
f = open('dati.txt', 'r').readlines()

#line in file 
for y in f:
    #number in line divided 
    for x in y.split():
        #is integer
        number = [int(x)]
    #append it 
    data.append(number)

#first line of data
first_line = data[0][0] #first line, first two numbers 
#all other lines 
other = data[1:] #skip first line 
#result 
print(first_line - len(other) - 1)