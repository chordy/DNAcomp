import sqlite3
nfile=open('seq0420.txt','w')
conn=sqlite3.connect('hardwaredb.sqlite')
cur= conn.cursor()

cur.execute('SELECT * from LogicGates where num=8')
#print  cur.fetchall()
#conn.commit()
f=cur.fetchall()
for i in range(12):
    print '8s%d: %s' %(i+1,f[0][i+2])
    nfile.write('8s%d, %s\n' %(i+1,f[0][i+2]))
    
    
cur.execute('SELECT * from LogicGates where num = 12')
f1=cur.fetchall()
for i in range (4):
    print '12s%d: %s' %(i+1,f1[0][i+2])
    nfile.write('12s%d, %s\n' %(i+1,f1[0][i+2]))
    
cur.execute('SELECT * from Adaptors where type=1 and onum=12 and inum=8 and portnumber=1')
f2=cur.fetchall()
for i in range(10):
    print 'a%ds%d: %s'%(f2[0][0],i+1,f2[0][i+5])
    nfile.write('a%ds%d, %s\n'%(f2[0][0],i+1,f2[0][i+5]))
    
cur.execute('SELECT *from Adaptors where type=1 and onum=8 and inum=1 and portnumber=0')
f3=cur.fetchall()
for i in range(10):
    print 'a%ds%d: %s'%(f3[0][0],i+1,f3[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f3[0][0],i+1,f3[0][i+5]))

cur.execute('SELECT *from Adaptors where type=1 and onum=8 and inum=12 and portnumber=0')
f4=cur.fetchall()
for i in range(10):
    print 'a%ds%d: %s'%(f4[0][0],i+1,f4[0][i+5])
    nfile.write('a%ds%d:,%s\n'%(f4[0][0],i+1,f4[0][i+5]))
    
cur.execute('SELECT * from Adaptors where type=1 and onum=8 and inum=0 and portnumber=1')
f5=cur.fetchall()
for i in range(10):
    print 'a%ds%d: %s' %(f5[0][0],i+1,f5[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f5[0][0],i+1,f5[0][i+5]))
    
cur.execute('SELECT *from Adaptors where type=2 and onum=8 and inum=0')
f6=cur.fetchall()
for i in range(10):
    print'a%ds%d: %s' %(f6[0][0],i+1,f6[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f6[0][0],i+1,f6[0][i+5]))
    
cur.execute('SELECT *from Adaptors where type=2 and onum=1 and inum=1')
f6=cur.fetchall()
for i in range(10):
    print'a%ds%d: %s' %(f6[0][0],i+1,f6[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f6[0][0],i+1,f6[0][i+5]))


cur.execute('SELECT *from Adaptors where type=2 and onum=0 and inum=0')
f6=cur.fetchall()
for i in range(10):
    print'a%ds%d: %s' %(f6[0][0],i+1,f6[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f6[0][0],i+1,f6[0][i+5]))


cur.execute('SELECT *from Adaptors where type=2 and onum=12 and inum=1')
f6=cur.fetchall()
for i in range(10):
    print'a%ds%d: %s' %(f6[0][0],i+1,f6[0][i+5])
    nfile.write('a%ds%d,%s\n'%(f6[0][0],i+1,f6[0][i+5]))
conn.close()
