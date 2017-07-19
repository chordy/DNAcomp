__author__ = 'yangyang5'

from PyQt5 import QtCore, QtGui, QtWidgets                              #导入模块

class Ui_Form(object):                                                  #创建窗口类，继承object

    def setupUi(self, Form):
        Form.setObjectName("Form")                                        #设置窗口名
        Form.resize(400, 300)                                              #设置窗口大小
        self.pushButton = QtWidgets.QPushButton(Form)                       #新建按钮，并加入到窗口中
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 75, 23))         #设置按钮的大小和位置
        self.pushButton.setObjectName("pushButton")                         #设置按钮名
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 20, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)                         #点击按钮，关闭窗体
        QtCore.QMetaObject.connectSlotsByName(Form)                         #关联信号槽

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))                     #设置窗口标题
        self.pushButton.setText(_translate("Form", "Quit"))                 #设置按钮名
        self.pushButton_2.setText(_translate("Form", "Print"))