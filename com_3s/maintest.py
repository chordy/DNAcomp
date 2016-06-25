#for exercise 
#[ng,nn]=gen_lgat(1)
#print (nn)

#generate hardware from 'ncDomain.txt'
import logicGate3s
import inpAndOupt
import modules
import genTh


f=open('af_5base.txt','r')
cdomain=[] 
po=0 #position

for line in f:
    cdomain.append(line.strip('\n\r'))
    #cdomain.append(line.strip('\r'))
print('lib length',len(cdomain))

##########################
# Logic gate
mods=[] # for saving modules
for i in range(4):
    print(cdomain[po:po+5])
    mods.append(logicGate3s.gen_lgat(1,i,cdomain[po:po+5]))
    po=po+5

for i in range(4):
    mods.append(logicGate3s.gen_lgat(2,i+4,cdomain[po:po+5]))
    po=po+5
for i in range(4):
    mods.append(logicGate3s.gen_lgat(3,i+8,cdomain[po:po+6]))
    po=po+6
for i in range(4):
    mods.append(logicGate3s.gen_lgat(4,i+12,cdomain[po:po+4]))
    po=po+4
##for mod in mods:
##    print (mod.out)
th_lib=genTh.gen_th(mods)
print (th_lib)


