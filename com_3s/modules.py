# function: for defination of modules, adaptors, instructions

import rev_comp_of_seq as rec

class modul : #modules
    def __init__ (self,num):
        self.num=num
        self.typ=''
        self.inp=[] #0,1
        #self.in2=[]
        self.out=[]
        self.gate_seq=[]
    def show(self):
        print('LGateN0.%d TYP : %s'%(self.num,self.typ))
        print('seq: ',self.gate_seq)
class inpt : # inputs
    def __init__(self,num):
        self.num=num
        self.seq=[]#0,1
    def show(self):
        print('NO.%d input: %s'%(self.num,self.seq))

class outp :
    def __init__(self,num):
        self.num=num
        self.seq=[]
    def show(self):
        print('NO.%d output: %s'%(self.num,self.seq))
class adap:
    def __init__(self,typ,bf,af,portnum):
        self.num=0
        self.typ=typ
        self.bfnum=bf
        self.afnum=af
        self.portnum=portnum
        self.seq=[]
    def show(self):
        print('type%d adaptor %d : %d to %d, %d'%(self.typ,self.num,self.bfnum,self.afnum,self.portnum))
        print('sequence:',self.seq)
    def setSeq1(self,modules):# type2 adaptor
        alpha='TCT'
        gamma='TAC'
        cal='CA' #close to alpha
        cg='TC'  #close to gamma
        for module in modules:#for storing list
            if module.num==self.bfnum:#out module
                om=module
            if module.num==self.afnum:
                inm=module
        rs1=cg+gamma+cg+om.out[0]+cal+alpha+cal
        s1=rec.rev_comp(rs1)
        
        rs3=cg+gamma+cg+om.out[1]+cal+alpha+cal
        s3=rec.rev_comp(rs3)
        
##        rs5=om.out[0]+cal+alpha+cal #threshold 
##        s5=rec.rev_comp(rs5)
##        s6=om.out[0]+cal
##        rs7=om.out[1]+cal+alpha+cal #!threshold needs reconsidering
##        s7=rec.rev_comp(rs7)
##        s8=om.out[1]+cal
        s9=cg+gamma+cg+om.out[0]+cal
        s10=cg+gamma+cg+om.out[1]+cal
        if self.portnum==0:
            s2=cal+alpha+cal+inm.inp[self.portnum][0]+cg+gamma+cg+om.out[0]+cal #0
            s4=cal+alpha+cal+inm.inp[self.portnum][1]+cg+gamma+cg+om.out[1]+cal#1
        else:
            if inm.typ=='xor':
                s2=cal+inm.inp[self.portnum][0]+cg+gamma+cg+om.out[0]+cal
                s4=cal+inm.inp[self.portnum][1]+cg+gamma+cg+om.out[1]+cal
            elif inm.typ=='and':
                s2=cal+alpha+cal+inm.inp[self.portnum][0]+cg+gamma+cg+om.out[0]+cal #0
                s4=cal+inm.inp[self.portnum][1]+cg+gamma+cg+om.out[1]+cal
            elif inm.typ=='or':
                s2=cal+inm.inp[self.portnum][0]+cg+gamma+cg+om.out[0]+cal
                s4=cal+alpha+cal+inm.inp[self.portnum][1]+cg+gamma+cg+om.out[1]+cal#1
            else:
                s2=cal+alpha+cal+inm.inp[self.portnum][0]+cg+gamma+cg+om.out[0]+cal #0
                s4=cal+alpha+cal+inm.inp[self.portnum][1]+cg+gamma+cg+om.out[1]+cal#1          
        self.seq.append(s1)
        self.seq.append(s2)
        self.seq.append(s3)
        self.seq.append(s4)
##        self.seq.append(s5)
##        self.seq.append(s6)
##        self.seq.append(s7)
##        self.seq.append(s8)
        self.seq.append(s9)
        self.seq.append(s10)       

    def setSeq2(self,modules,oupts):# type2 adaptor
        alpha='TCT'
        gamma='TAC'
        cal='CA' #close to alpha
        cg='TC'  #close to gamma
        for module in modules:
            if module.num==self.bfnum:
                om=module
        for oupt in oupts:
            
            if oupt.num==self.afnum:
                inm=oupt
        
        rs1=cg+gamma+cg+om.out[0]+cal+alpha+cal
        s1=rec.rev_comp(rs1)
        s2=cal+inm.seq[0][7:19]+cg+gamma+cg+om.out[0]+cal
        rs3=cg+gamma+cg+om.out[1]+cal+alpha+cal
        s3=rec.rev_comp(rs3)
        s4=cal+inm.seq[1][7:19]+cg+gamma+cg+om.out[1]+cal
##        rs5=om.out[0]+cal+alpha+cal #threshold 
##        s5=rec.rev_comp(rs5)
##        s6=om.out[0]+cal
##        rs7=om.out[1]+cal+alpha+cal #threshold 
##        s7=rec.rev_comp(rs7)
##        s8=om.out[1]+cal
        s9=cg+gamma+cg+om.out[0]+cal
        s10=cg+gamma+cg+om.out[1]+cal
        self.seq.append(s1)
        self.seq.append(s2)
        self.seq.append(s3)
        self.seq.append(s4)
##        self.seq.append(s5)
##        self.seq.append(s6)
##        self.seq.append(s7)
##        self.seq.append(s8)
        self.seq.append(s9)
        self.seq.append(s10)
