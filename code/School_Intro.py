import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Intro_UI(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('学校简介')  # 窗口标题
        self.setGeometry(5, 30, 1355, 730)  # 窗口的大小和位置设置
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('https://www.bjut.edu.cn/xxgk/xxjj1.htm'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Intro_UI()
    win.show()
    app.exit(app.exec_())
