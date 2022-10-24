import sys

from widget import *

if __name__ == "__main__":
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    aw = MainWindow()  # 创建主窗体对象，实例化Ui_MainWindow

    aw.show()  # 显示主窗体
    sys.exit(App.exec_())  # 循环中等待退出程序
