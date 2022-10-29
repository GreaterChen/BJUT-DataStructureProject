from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
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
        self.mat_floyd = []
        self.read_mat()
        Dialog.setObjectName("Dialog")
        Dialog.resize(244, 223)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 240, 210))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 100, 80))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def read_mat(self):
        with open('../address/adj_floyd_mat.txt') as f:
            entire_text = f.read()
            for row in entire_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat_floyd.append(float(item))
            self.mat_floyd = np.array(self.mat_floyd).reshape((47, 47))


class UI_Bubble(MyDialog):
    def __init__(self, i, Opacity, city_name, distance):
        super().__init__(None)
        print(i, Opacity, city_name)
        self.distance = distance
        self.city_name =city_name
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
        self.ui.label_2.setText(f"""
                                <html>
                                <head/>
                                    <body>
                                        <p align=\"center\"><span style=\"font-weight:600; font-size:10pt\">{self.city_name}</span></p>
                                        <p><br/></p>
                                    </body>
                                </html>"""
                                )

    def ReadAxis(self):
        with open('../address/axis_x.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.x.append(int(item))

        with open('../address/axis_y.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.y.append(int(item))

    def GoGoGo(self):
        now = QTime.currentTime()
        second = int(self.distance / 6.66)
        time = now.addSecs(second).toString(Qt.DefaultLocaleLongDate)
        print("222")
        self.ui.label_2.setText(f"""
                                <html>
                                <head/>
                                    <body>
                                        <p align=\"center\"><span style=\"font-weight:600; font-size:10pt\">{self.city_name}</span></p>
                                        <p>预计到达时间：</p>
                                        <p style=\"font-weight:600;\">{time}</p>
                                        <p><br/></p>
                                    </body>
                                </html>"""
                                )
        print("333")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    s = "test"
    print(s)
    t = UI_Bubble(17, 0.5, s)
    t.show()
    sys.exit(app.exec_())
