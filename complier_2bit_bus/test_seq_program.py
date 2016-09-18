import d_lexer1
import d_parser
import d_ast1
import d_inte_gene_2bit_bus as d_inte_gene
import d_gene_v3 as d_gene
mypro=['a = 1 ', 'b = a + 1 ']
print('*'*30)
print('user program:')
print()
seq_ins=[]
print(len(mypro))
tokens=[]
for i in range(len(mypro)):
    print(mypro[i])
    tokens=(d_lexer1.d_lex(mypro[i]))
  
    root=d_ast1.tree('headers')
    headers=d_parser.d_par(tokens)

    for header in headers:
        #print(type(header),header.data,header.id )
        if header.id==1:
            root.add(header)
            #print(header)
    #print(root.getchildren())
    cod=d_inte_gene.in_gene(headers)
##print('*'*30)
##print('intermediate code :')
##print()
##for co in cod:
##    print(co.num,co.type ,co.in1 ,co.in2, co.in3 )          
##

ins=d_gene.d_gene(cod)
print()
print('*'*30)
print('instructions:')
for inn in ins:
    print(inn)
##seq_ins.append(ins)
##print('*'*30)
##for i in range(1,len(seq_ins)):
##    for ins in seq_ins[i]:
##        if 'INP' in ins: # 如果是一个输入命令
##            inp=ins.split('INP(')[1].split(',')[0]
##            in_port=ins.split(')')[0].split(',')[1]
##            for j in range(i):
##                for inn in seq_ins[j]:
##                    if 'VAR' in inn:
##                        oup=inn.split('VAR(')[1].split(',')[0]
##                        ou_port=inn.split(',')[1]
##                        if oup==inp:
##                            for inns in seq_ins[i]:
##                                if inns.split(',')[0].split('(')[1]==in_port:
##                                    pos=seq_ins[i].index(inns)
##                                    seq_ins[i][pos]='WIR2('+ou_port+inns.split(',')[1]+inns.split(',')[2]
##                            seq_ins[j].remove(inn)
##                            seq_ins[i].remove(ins)
##        
##            
##print(seq_ins)
##nins=[]
##for ins in seq_ins:
##    nins.extend(ins)
##
##for inn in nins:
##    print (inn)
