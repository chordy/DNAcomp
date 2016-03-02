#function: generate changable domain 15 nt
#output: all possible sequence with initial filtering
# by O.L. Mar 2,2016
dic={0:'A',1:'C',2:'T'}
a=[]
l=[] # for storing letters
ccDomain=[]
f=open('ccDomain.txt','w')
for i in range(15) :
    a.append(i)
    l.append('')
for i in range(3**15) :
    tmp=0
    for j in range(15) :
        a[j]=int(((i-tmp)/3**j)%(3))
        tmp=tmp+a[j]*3**j
        #print(a[j])
        l[j]=dic[a[j]]
    #print(l)
    c=''.join(l)
    if 'AAAA' not in c:
        if 'TTTT' not in c:
            if 'CCC' not in c:
                if c[0]!=c[1] and c[0]=='C' or c[1]=='C':
                    if c[13]!=c[14] and c[13]=='C' or c[14]=='C':
                        ccDomain.append(c)
    #f.writelines(c)

#print(cDomain)

f.write('\n'.join(ccDomain))
f.close()
