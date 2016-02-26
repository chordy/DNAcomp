# function: filter initial generated seqs
# by OL , Feb 23, 2016
f=open('cDomain.txt','r')
##print(f.readline().strip('\n'))

i=0
for line in f :
##    print (line)
    if 'AAAA'  in line:
        #print(line)
        continue
    elif 'CCC' in line:
        continue
    elif 'GGG' in line :
        continue
    elif 'TTTT' in line:
        continue
    elif line.count('C')+line.count('G')<2 or line.count('C')+line.count('G')>5:
        continue
    else :
        print(line)
        i=i+1
print(i)
