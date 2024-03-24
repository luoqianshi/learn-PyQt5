import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    # 自定义一个信号，自定义的信号只可以放在类变量这里
    # 后面的str表示该信号将会传递一个str类型的数据变量
    my_signal = pyqtSignal(str)
    # 用于更新显示框处的信息的文本变量
    info = ""

    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()
        # 把对当前的窗口控件的具体的UI布局写到有个专门的方法中，以免初始化的方法内容太臃肿
        self.init_ui()

    def init_ui(self):
        # 设置大小
        self.resize(500, 350)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之信号和槽3——练习')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 创建了一个多行文本框
        self.text = QTextEdit(self)
        # 设置 QTextEdit 为只读
        self.text.setReadOnly(True)
        # 设置字体大小为20
        font = QFont()
        font.setPointSize(10)
        self.text.setFont(font)
        # 设置多行文本框的窗口的宽度和高度
        self.text.setGeometry(50, 20, 400, 250)

        # 创建了一个按钮
        btn = QPushButton("测试自定义信号", self)
        # 设置窗口的宽度和高度
        btn.setGeometry(200, 280, 100, 30)

        # 为按钮的单击信号绑定对应的槽函数
        btn.clicked.connect(self.on_btn_clicked)
        # 为自定义的信号绑定他对应的槽函数
        self.my_signal.connect(self.find_error)

    def on_btn_clicked(self):
        # 每次启动前先清空输入框
        self.info = ""
        self.text.setText("")
        for index, ip in enumerate(["192.168.21.%d" % x for x in range(1, 255)]):
            signal_line = "模拟，正在检查：" + ip + "..."
            if index % 5 == 0:
                self.my_signal.emit(signal_line + "【发现错误！！】")  # 相当于啊调用了自定义信号my_signal的槽函数
            else:
                self.my_signal.emit(signal_line)
            # 延时0.01s
            time.sleep(0.01)

    def find_error(self, msg):
        self.info += msg + '\n'
        self.text.setText(self.info)
        # self.text.append(msg+'\n')
        print(msg)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()

    app.exec_()
