import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("这里是窗口1", self)
        self.setStyleSheet("background-color: red")
        # 设置标签内的字体的属性
        font = QFont()
        font.setPointSize(20)
        label.setFont(font)


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("这里是窗口2", self)
        self.setStyleSheet("background-color: green")
        # 设置标签内的字体的属性
        font = QFont()
        font.setPointSize(20)
        label.setFont(font)

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
        self.setWindowTitle('PyQt5程序之QStackLayout')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 垂直布局
        outer_container = QVBoxLayout()
        # 展示区控件
        display = QWidget()
        display.setStyleSheet("background-color:grey")
        # 为展示区控件绑定抽屉布局(加上self的含义是让它变成一个全局变量)
        self.windows_stack = QStackedLayout()
        # 创建两个新的窗口对象
        window1 = Window1()
        window2 = Window2()
        self.windows_stack.addWidget(window1)
        self.windows_stack.addWidget(window2)
        # 将抽屉布局绑定到展示控件上
        display.setLayout(self.windows_stack)
        # 按钮控件
        btn1 = QPushButton("切换到窗口一")
        btn2 = QPushButton("切换到窗口二")
        # 为按钮设置单击事件
        btn1.clicked.connect(self.show_window1)
        btn2.clicked.connect(self.show_window2)
        # 绑定控件
        outer_container.addWidget(display)
        outer_container.addWidget(btn1)
        outer_container.addWidget(btn2)

        # 让当前的窗口使用布局器
        self.setLayout(outer_container)

    def show_window1(self):
        self.windows_stack.setCurrentIndex(0)

    def show_window2(self):
        self.windows_stack.setCurrentIndex(1)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()

    app.exec_()