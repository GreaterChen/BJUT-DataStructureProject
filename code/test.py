from PyQt5.QtCore import *
if __name__ == '__main__':
    now = QTime.currentTime()
    print(now.addSecs(200).toString(Qt.DefaultLocaleLongDate))
