import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 实例化QApplication类
    app = QApplication(sys.argv)

    # 实例化QWidget类
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle('第一个PyQt5')

    # 设置窗口大小
    # w.resize(1400, 1300)

    # 设置窗口位置
    # w.move(400, 400)

    # 设置窗口背景色
    w.setStyleSheet("background-color: rgb(255, 255, 255);")

    # 设置窗口显示
    w.show()

    # 程序进行循环等待状态
    app.exec_()
