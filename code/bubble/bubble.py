from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QDialog
from PyQt5.QtCore import Qt, QTimer, QRect
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(244, 223)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../images/image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 101, 71))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(
            _translate("Dialog", "<html><head/><body><p>预计到达时间：</p><p>1h32min</p><p><br/></p></body></html>"))


class Ui_test(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        desktop = QApplication.desktop()
        self.setGeometry(QRect(400, 500, 244, 223))
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)

    def show_tip(self):
        # TipUi.show_tip.tip = TipUi(text,desktop.width() / 2, desktop.height() / 2)
        # TipUi.show_tip.tip.show()
        # self.ui.pushButton.setText(text)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    t = Ui_test()
    t.show_tip()
    sys.exit(app.exec_())
