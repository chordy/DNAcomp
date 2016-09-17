import d_lexer1
import d_parser
import d_ast1
import d_inte_gene_2bit_bus as d_inte_gene
import d_gene_v3 as d_gene
##mypro=' for i = 1 : 1 i = i + 1 '
mypro=' i = 1 < 2 '
print('*'*30)
print('user program:')
print()
print(mypro)
tokens=d_lexer1.d_lex(mypro)
print()
print('*'*30)
print('token stream :')
for token in tokens:
    print(token)
print()  
root=d_ast1.tree('headers')
headers=d_parser.d_par(tokens)
  
for header in headers:
    print(type(header),header.data,header.id )
    if header.id==1:
        root.add(header)
        #print(header)
#print(root.getchildren())
print(headers[0].rchild )
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
