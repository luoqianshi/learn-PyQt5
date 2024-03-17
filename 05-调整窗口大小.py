import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget类
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之调整窗口大小')

    # 重置窗口大小
    w.resize(800, 600)

    # 将窗口设置在屏幕的左上角
    # w.move(0, 0)

    # 设置窗口显示
    w.show()

    # 程序进行循环等待状态
    app.exec_()