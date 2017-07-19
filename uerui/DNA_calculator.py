#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
DNA computer User GUI
by ol
Mar 28, 2017

"""

import d_parser
import d_ast1
import d_inte_gene_2bit_bus as d_inte_gene
import d_gene_v3 as d_gene
import sys
from PyQt5.QtWidgets import (QWidget,  QToolTip,
    QPushButton, QApplication,QTextBrowser)
from PyQt5.QtGui import (QFont)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.comlist=[]
        
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 40))
        
        # grid = QGridLayout()
        # self.setLayout(grid)
 
        # names = ['NOT', 'AND', '0', '1', 
        #         'OR', 'XOR', '2', '3',
        #        '>', '<', '/', '*',
        #         '!=', '==', '+', '-',
        #        '(', ')', '@', 'DEL']
#        
        # positions = [(i,j) for i in range(5) for j in range(4)]
        
        self.buno= QPushButton('NOT',self)
        self.buno.resize(60,35)
        self.buno.move(0*70+30,0*52+85)
        self.buno.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buno.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buno.clicked.connect(self.commandBuno)

        self.buand= QPushButton('AND',self)
        self.buand.resize(60,35)
        self.buand.move(1*70+30,0*52+85)
        self.buand.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buand.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buand.clicked.connect(self.commandBuand)

        self.bu0= QPushButton('0',self)
        self.bu0.resize(60,35)
        self.bu0.move(2*70+30,0*52+85)
        self.bu0.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bu0.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bu0.clicked.connect(self.commandBu0)

        self.bu1= QPushButton('1',self)
        self.bu1.resize(60,35)
        self.bu1.move(3*70+30,0*52+85)
        self.bu1.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bu1.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bu1.clicked.connect(self.commandBu1)

        self.buor= QPushButton('OR',self)
        self.buor.resize(60,35)
        self.buor.move(0*70+30,1*52+85)
        self.buor.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buor.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buor.clicked.connect(self.commandBuor)

        self.buxor= QPushButton('XOR',self)
        self.buxor.resize(60,35)
        self.buxor.move(1*70+30,1*52+85)
        self.buxor.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buxor.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buxor.clicked.connect(self.commandBuxor)

        self.bu2= QPushButton('2',self)
        self.bu2.resize(60,35)
        self.bu2.move(2*70+30,1*52+85)
        self.bu2.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bu2.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bu2.clicked.connect(self.commandBu2)

        self.bu3= QPushButton('3',self)
        self.bu3.resize(60,35)
        self.bu3.move(3*70+30,1*52+85)
        self.bu3.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bu3.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bu3.clicked.connect(self.commandBu3)

        self.bul= QPushButton('>',self)
        self.bul.resize(60,35)
        self.bul.move(0*70+30,2*52+85)
        self.bul.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bul.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bul.clicked.connect(self.commandBul)

        self.bus= QPushButton('<',self)
        self.bus.resize(60,35)
        self.bus.move(1*70+30,2*52+85)
        self.bus.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bus.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bus.clicked.connect(self.commandBus)

        self.bud= QPushButton('/',self)
        self.bud.resize(60,35)
        self.bud.move(2*70+30,2*52+85)
        self.bud.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bud.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bud.clicked.connect(self.commandBud)

        self.bum= QPushButton('*',self)
        self.bum.resize(60,35)
        self.bum.move(3*70+30,2*52+85)
        self.bum.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bum.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bum.clicked.connect(self.commandBum)

        self.buneq= QPushButton('!=',self)
        self.buneq.resize(60,35)
        self.buneq.move(0*70+30,3*52+85)
        self.buneq.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buneq.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buneq.clicked.connect(self.commandBuneq)

        self.bueq= QPushButton('==',self)
        self.bueq.resize(60,35)
        self.bueq.move(1*70+30,3*52+85)
        self.bueq.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bueq.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bueq.clicked.connect(self.commandBueq)

        self.bup= QPushButton('+',self)
        self.bup.resize(60,35)
        self.bup.move(2*70+30,3*52+85)
        self.bup.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bup.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bup.clicked.connect(self.commandBup)

        self.bumi= QPushButton('-',self)
        self.bumi.resize(60,35)
        self.bumi.move(3*70+30,3*52+85)
        self.bumi.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bumi.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bumi.clicked.connect(self.commandBumi)

        self.bulf= QPushButton('(',self)
        self.bulf.resize(60,35)
        self.bulf.move(0*70+30,4*52+85)
        self.bulf.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bulf.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bulf.clicked.connect(self.commandBulf)

        self.buri= QPushButton(')',self)
        self.buri.resize(60,35)
        self.buri.move(1*70+30,4*52+85)
        self.buri.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buri.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buri.clicked.connect(self.commandBuri)

        self.buf= QPushButton('Clear',self)
        self.buf.resize(60,35)
        self.buf.move(2*70+30,4*52+85)
        self.buf.setFont(QFont('Calibri', 14, QFont.Normal))
        self.buf.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.buf.clicked.connect(self.commandBucl)

        self.bude= QPushButton('DEL',self)
        self.bude.resize(60,35)
        self.bude.move(3*70+30,4*52+85)
        self.bude.setFont(QFont('Calibri', 14, QFont.Normal))
        self.bude.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        self.bude.clicked.connect(self.commandDel)







        # for position, name in zip(positions,names):
        #     self.button=QPushButton(name,self)
        #     self.button.resize(60,35)
        #     self.button.setText(name)
        #     self.button.move(position[1]*70+30,position[0]*52+85)
        #     self.button.setFont(QFont('Calibri', 14, QFont.Normal))
        #     self.button.setStyleSheet("QPushButton{color:'#212121';background:'#e1e1e1'}")
        #     self.button.clicked.connect(self.commandInp)

        ex_button=QPushButton('Exit',self)
        ex_button.resize(130,40)
        ex_button.move(30,350)
        ex_button.setFont(QFont('Calibri', 14, QFont.Bold))
        ex_button.setStyleSheet("QPushButton{color:'#016d5d';background:'#e1e1e1'}")
        ex_button.clicked.connect(self.exclicked)


        en_button=QPushButton('Enter',self)
        en_button.resize(130,40)
        en_button.move(170,350)
        en_button.setFont(QFont('Calibri', 14, QFont.Bold))
        en_button.setStyleSheet("QPushButton{color:'#016d5d';background:'#e1e1e1'}")
        # en_button.setFlat(True)
        # grid.addWidget(button, 5, 1)
        self.toshow = QTextBrowser(self)
        self.toshow.resize(270,50)
        self.toshow.move(30,20)
        #self.toshow.append('enter1')
        en_button.clicked.connect(self.enButtonClicked)
        # inpEdit.setFixedWidth(400) 
        

        #self.move(300, 150)
        self.setGeometry(300,250,360,400)
        self.setWindowTitle('Calculator')
        self.show()
    def enButtonClicked(self):
        self.comlist.append("=")
        print('commlist',self.comlist)
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        print('Instructions:')
        self.comlist.pop()
        tokens=[['id','s'],['=','reserved']]
        for com in self.comlist:
            
            if com in ['0','1','2','3']:
                tokens.append(['num',com])
            elif com in ['NOT','AND','OR','XOR']:
                tokens.append([com.lower(),'reserved'])
            else:
                tokens.append([com,'reserved'])
        print(tokens)
        root=d_ast1.tree('headers')
        headers=d_parser.d_par(tokens)
        
        for header in headers:
            #print(type(header),header.data)
            if header.id==1:
                root.add(header)
                #print(header)
        #print(root.getchildren())
        cod=d_inte_gene.in_gene(headers)
        ins=d_gene.d_gene(cod)
        print(ins)
        for inn in ins:
            print(inn)
        newWindow = Example1()
        newWindow.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        for inn in ins:
            newWindow.s.append(inn)
        newWindow.showIns()    
        newWindow.exec_()
        
    def commandBuno(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buno.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        # for ele in self.comlist:
        #     self.toshow.append(ele)
    def commandBuand(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buand.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)

    def commandBu0(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bu0.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBu1(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bu1.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)

    def commandBuor(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buor.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBuxor(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buxor.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBu2(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bu2.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBu3(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bu3.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBul(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bul.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBus(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bus.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBud(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bud.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBum(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bum.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBuneq(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buneq.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBueq(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bueq.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBup(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bup.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBumi(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bumi.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        


    def commandBulf(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.bulf.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        
    def commandBuri(self):
        # print('commlist',self.comlist)
        self.comlist.append(self.buri.text())
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        

    def commandBucl(self):
        # print('commlist',self.comlist)
        self.comlist=[]
        str1 = '0'
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
        

    def commandDel(self):
        self.comlist.pop()
        str1 = ' '.join(self.comlist)
        self.toshow.setFont(QFont('Calibri', 14, QFont.Bold))
        self.toshow.setText(str1)
    def exclicked(self):
    	sys.exit()
        
class Example1(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.s=[]
        
        
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 40))
        self.setGeometry(300,250,360,400)
        self.setWindowTitle('Instructions')
        self.toshow = QTextBrowser(self)
        self.toshow.resize(270,300)
        self.toshow.move(30,20)
        self.toshow.setText('good')
        
#        self.toshow.setText('\n'.join(self.s))
        self.show()
    def showIns(self):
        self.toshow.setText('\n'.join(self.s))
           
        


        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    #ex = Example()
    ex = Example()
    sys.exit(app.exec_())
# to Jul 11, 需补充按enter键后弹出窗口，并给出instruction的部分。