import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    # 自定义一个信号，自定义的信号只可以放在类变量这里
    # 后面的str表示该信号将会传递一个str类型的数据变量
    my_signal = pyqtSignal(str)

    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()
        # 把对当前的窗口控件的具体的UI布局写到有个专门的方法中，以免初始化的方法内容太臃肿
        self.init_ui()

    def init_ui(self):
        # 设置大小
        self.resize(500, 300)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之信号和槽2——自定义信号')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 创建了一个按钮
        btn = QPushButton("测试自定义信号", self)
        # 设置窗口的宽度和高度
        btn.setGeometry(200, 200, 100, 30)

        # 为按钮的单击信号绑定对应的槽函数
        btn.clicked.connect(self.on_btn_clicked)
        # 为自定义的信号绑定他对应的槽函数
        self.my_signal.connect(self.find_error)

    def on_btn_clicked(self):
        for index, ip in enumerate(["192.168.21.%d" % x for x in range(1, 255)]):
            print(f"正在检查：{ip}...", end="")
            if index % 5 == 0:
                self.my_signal.emit("【发现错误！！】")  # 相当于啊调用了自定义信号my_signal的槽函数
            else:
                self.my_signal.emit("")
            # 延时0.01s
            time.sleep(0.01)

    def find_error(self, msg):
        print(msg)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()

    app.exec_()
