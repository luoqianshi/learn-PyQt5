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
        self.resize(300, 300)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之Gird布局——计算器')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 最外层是一个垂直布局布局
        outer_container = QVBoxLayout()

        # 创建一个输入框
        input_box = QLineEdit()
        input_box.setPlaceholderText('请输入内容')
        # 把输入框和按钮放到布局中
        outer_container.addWidget(input_box)

        # 创建计算器的网络布局
        grid = QGridLayout()
        # 计算器网格布局的数据准备（这里刻意使用一种类似json格式的键值对的数据形式）
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', '<-'],
            3: ['0', '.', '=', '/', 'C']
        }
        # 把网格布局添加到外层的垂直布局中
        outer_container.addLayout(grid)
        for key_row, numbers in data.items():
            for index_column, value in enumerate(numbers):
                btn = QPushButton(value)
                grid.addWidget(btn, key_row, index_column)

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