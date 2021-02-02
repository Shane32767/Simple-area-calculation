import sys
from PyQt5 import QtWidgets, uic
from easygui import choicebox

msg = choicebox(msg='你要计算什么的面积？',title='计算',choices=['矩形','三角形','梯形'])

if msg == None:
    sys.exit()

if msg == '矩形':
    from_class = uic.loadUiType("C:/Users/Lenovo/Desktop/蜜汁python文件夹/tast/计算/jx.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类
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
    from_class = uic.loadUiType("C:/Users/Lenovo/Desktop/蜜汁python文件夹/tast/计算/sj.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类
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
    from_class = uic.loadUiType("C:/Users/Lenovo/Desktop/蜜汁python文件夹/tast/计算/tx.ui")[0]
    class js(QtWidgets.QMainWindow, from_class):
        #为窗口定义一个类
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
