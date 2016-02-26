#test function module
#[ng,nn]=gen_lgat(1)
#print (nn)

import logicGate_c
import inpAndOupt
import modules_c
cdomain=['AAAAA','AAAAG','CCCCC','GGGGG','AAGGG','AACCC','CAACC']
s1=(logicGate_c.gen_lgat(1,1,cdomain))
s2=(logicGate_c.gen_lgat(2,2,cdomain))
s3=(logicGate_c.gen_lgat(3,3,cdomain))
s4=(logicGate_c.gen_lgat(4,4,cdomain))
mods=[] # for saving modules
mods.append(s1)
mods.append(s2)
mods.append(s3)
mods.append(s4)
inpts=[]
oupts=[]
for i in range(4):
    inp=inpAndOupt.gen_inp (i,cdomain)
    inpts.append(inp)
    oup=inpAndOupt.gen_oup (i,cdomain)
    oupts.append(oup)
print('************************************')
for inp in inpts:
    inp.show()
print('************************************')
for oup in oupts:
    oup.show()
print('************************************')
ad1=modules_c.adap(2,3,4,0)
ctl='CCCC'
ad1.setCtlSeq(ctl)
ad1.setSeq2(mods)
ad1.show()
print('************************************')
ad2=modules_c.adap(1,1,2,0)
ctl='CCCC'
ad2.setCtlSeq(ctl)
ad2.setSeq1(inpts,mods)
ad2.show()
print('************************************')
ad3=modules_c.adap(3,1,2,0)
ctl='CCCC'
ad3.setCtlSeq(ctl)
ad3.setSeq3(mods,oupts)
ad3.show()
print('************************************')
