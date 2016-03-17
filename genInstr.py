#function: generate one instruction
#input : changeable domain
#output : one DNA sequence
f=open('cDomain.txt','r')
tmp=str(f.readline().strip('\n')) # read in seq
#具体的序列需要根据运算的要求自动对比
alpha='TGAGA'
gamma='GTAGA'
cal='TG'
cg='GT'
beta=cal+tmp+cg
#print(beta)

ins=alpha+beta+gamma #instruction
print('WIR3(5,2): ',ins)
