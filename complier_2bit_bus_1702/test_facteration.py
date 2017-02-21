import d_gene_v3 as d_gene
import d_inte_gene_2bit_bus as d_inte_gene
#进行因式分解的主程序
# from intermiate code
cod=[]
co=d_inte_gene.incd()

co.num=2
co.type='@'
co.in1=['num',0]
co.in2=['num',3]
#print(co.num,co.type ,co.in1 ,co.in2, co.in3 )
cod.append(co)

co1=d_inte_gene.incd()
co1.num=1
co1.type='<='
co1.in1=['id','b']
co1.in2=['id',2]
#print(co.num,co.type ,co.in1 ,co.in2, co.in3 )
cod.append(co1)

ins=d_gene.d_gene(cod)
print()
print('*'*30)
print('instructions:')
for inn in ins:
    print(inn)
