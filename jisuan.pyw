import sys
from PyQt5 import QtWidgets, uic
from easygui import choicebox
#导入需要的模块  Import the required modules

msg = choicebox(msg='你要计算什么的面积？',title='计算',choices=['矩形','三角形','梯形'])#询问图形  Query graphics

if msg == None:
    sys.exit()

#以下为计算/图形界面  The following is the calculation/graphic interface
if msg == '矩形':
    from_class = uic.loadUiType("jx.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类  Define a class for the window
        def __init__(self, parent=None):
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.start.clicked.connect(self.start_)
        def start_(self):
            try:
                h = float(self.h.text())
                a = float(self.a.text())
                s = str(a * h)
                self.sjx.setText(s)
            except:
                pass
    app = QtWidgets.QApplication(sys.argv)
    win = js(None)
    win.show()
    app.exec_()

elif msg == '三角形':
    from_class = uic.loadUiType("sj.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类  Define a class for the window
        def __init__(self, parent=None):
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.start.clicked.connect(self.start_)
        def start_(self):
            try:
                h = float(self.h.text())
                a = float(self.a.text())
                s = str(a * h / 2)
                self.s.setText(s)
            except:
                pass
    app = QtWidgets.QApplication(sys.argv)
    win = js(None)
    win.show()
    app.exec_()

else:
    from_class = uic.loadUiType("tx.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类  Define a class for the window
        def __init__(self, parent=None):
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.start.clicked.connect(self.start_)
        def start_(self):
            try:
                h = float(self.h.text())
                a = float(self.a.text())
                b = float(self.b.text())
                s = str((a + b)* h / 2)
                self.s.setText(s)
            except:
                pass
    app = QtWidgets.QApplication(sys.argv)
    win = js(None)
    win.show()
    app.exec_()
