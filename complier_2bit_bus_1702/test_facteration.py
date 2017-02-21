import d_gene_v3 as d_gene
import d_inte_gene_2bit_bus as d_inte_gene
# from intermiate code
cod=[]
co=d_inte_gene.incd()

co.num=2
co.type='@'
co.in1=['num',1]
co.in2=['num',2]
#print(co.num,co.type ,co.in1 ,co.in2, co.in3 )
cod.append(co)

co.num=1
co.type='<='
co.in1=['id','b']
co.in2=['id',2]
#print(co.num,co.type ,co.in1 ,co.in2, co.in3 )
cod.append(co)

ins=d_gene.d_gene(cod)
print()
print('*'*30)
print('instructions:')
for inn in ins:
    print(inn)
