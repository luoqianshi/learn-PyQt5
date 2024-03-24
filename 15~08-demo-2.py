import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()
        # 把对当前的窗口控件的具体的UI布局写到有个专门的方法中，以免初始化的方法内容太臃肿
        self.init_ui()

    def init_ui(self):
        # 设置大小
        self.resize(400, 400)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之XXXX')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 垂直布局
        outer_container = QVBoxLayout()

        # 让当前的窗口使用布局器
        self.setLayout(outer_container)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()

    app.exec_()