from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(150, 54)
        Dialog.setStyleSheet("background: transparent;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setAutoFillBackground(False)
        # 在这里设置气泡的stylesheet
        self.pushButton.setStyleSheet("background-color:rgb(250, 255, 213);\n"
                                      "border-style:none;\n"
                                      "padding:8px;\n"
                                      "border-radius:25px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "提示框"))


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_Dialog()  # 创建主窗体对象，实例化Ui_MainWindow

    # aw.show()  # 显示主窗体
    sys.exit(App.exec_())  # 循环中等待退出程序
