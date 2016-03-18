nf=open('nccDomain.txt','r')
nnndomain=[]
ndomain=[]
nnndomain.append(nf.readline().strip('\n'))
for line in nf:
    flag=0
    dom=line.strip('\n')
    ndomain.append(dom)
##    for ddom in nnndomain:
##        if ddom[0:6]==dom[0:6] or ddom[9:15]==dom[9:15]:
##            flag=1
##            print(dom,ddom)
##            break
##    if flag==0:
##        nnndomain.append(dom)
nf.close()
##nnf=open('af4Domain.txt','w')
##nnf.write('\n'.join(nnndomain))
##nnf.close()
a='CAATAATACTCTAAC'
b='CCTATTACTTCTAAC'
def same_length(x,y):
    l=len(x)
    cmp=[]
    tmp=0
    le=0
    for i in range(l):
        if x[i]==y[i]:
            cmp.append(1)
        else:
            cmp.append(0)
    st=0
    print(cmp)
    for i in range(len(cmp)):
        if (i==0 and cmp[i]==1) or (i>0 and cmp[i-1]==0 and cmp[i]==1):
            st=i
        if i==l-1 and cmp[i]==1:
            le=l-st
        elif i>1 and cmp[i]==0 and cmp[i-1]==1:
            le=i-st
        if le>tmp:
            tmp=le
    return tmp
print(same_length(a,b))
