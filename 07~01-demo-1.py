import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget类
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之XXX')
    # 设置窗口图标
    w.setWindowIcon(QIcon('imgs/clock.png'))
    # PyQt5隐藏上方的标签栏
    # w.setWindowFlag(Qt.FramelessWindowHint)

    """
    在这里面去写具体的代码
    """

    # 设置窗口显示
    w.show()
    # 程序进行循环等待状态
    app.exec_()