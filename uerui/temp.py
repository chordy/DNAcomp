# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets,QtCore                        #从pyqt库导入QtWindget通用窗口类
from formnew import Ui_Form

class mywindow(QtWidgets.QWidget,Ui_Form):                  #自己建的类，继承QtWidgets.Qwidget类方法和Ui_Form界面类

    _signal = QtCore.pyqtSignal(str)                #定义信号，定义参数类型为str

    def __init__(self):
        super(mywindow,self).__init__()             #首先找到子类（mywindow）的父类（QWidget），然后把my的对象self转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)                          #直接继承界面类，调用类的setupUi方法

        self.pushButton_2.clicked.connect(self.myPrint)       #连接自己的槽函数
        self._signal.connect(self.mySignal)               #将信号连接到函数mySignal

    def myPrint(self):                                     #自定义的槽函数。槽其实就是个函数（方法）
        self.textBrowser.setText("")
        self.textBrowser.append("我是槽函数")
        self._signal.emit("发射信号，传递字符串")

    def mySignal(self,string):                                  #自定义信号函数
        self.textBrowser.append(string)                                           #接受到字符串，打印出来
        self.textBrowser.append("我是信号函数")


if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)            #pyqt窗口必须在QApplication方法中使用
    myshow=mywindow()                               #生成mywindow类的实例 myshow
    myshow.show()                                   #myshow调用show方法
    sys.exit(app.exec())                            #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序