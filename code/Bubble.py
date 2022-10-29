from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

global Bubble_Opacity
Bubble_Opacity = 0.5


class MyDialog(QDialog):
    def __init__(self, text):
        super(MyDialog, self).__init__(text)

    def enterEvent(self, a0: QEvent) -> None:
        self.setWindowOpacity(1)

    def leaveEvent(self, a0: QEvent) -> None:
        self.setWindowOpacity(Bubble_Opacity)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(244, 223)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 240, 210))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 100, 70))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(
            _translate("Dialog", "<html><head/><body><p>预计到达时间：</p><p>1h32min</p><p><br/></p></body></html>"))


class UI_Bubble(MyDialog):
    def __init__(self, i, Opacity):
        super().__init__(None)
        self.x = []
        self.y = []
        self.ReadAxis()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setGeometry(QRect(self.x[i] - 200 - 226, self.y[i] - 70, 240, 210))
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        global Bubble_Opacity
        Bubble_Opacity = Opacity

    def ReadAxis(self):
        with open('../address/axis_x.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.x.append(int(item))

        with open('../address/axis_y.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.y.append(int(item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    t = UI_Bubble(17)
    t.show()
    sys.exit(app.exec_())
