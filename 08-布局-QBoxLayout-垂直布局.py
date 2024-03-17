import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()

        # 设置大小
        self.resize(300, 300)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之垂直布局')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 垂直布局(限制)
        layout = QVBoxLayout()

        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零
        # 会将你放在layout中的空间压缩成默认的大小
        # 下面的空白区域的比例为：1：1：1：2
        # 加了一个伸缩器（可以理解为一个弹簧）
        layout.addStretch(1)

        # 设置布局的方向
        layout.setDirection(QBoxLayout.TopToBottom)
        # 设置布局的间距
        layout.setContentsMargins(10, 10, 10, 10)
        # 设置布局的内边距
        layout.setSpacing(10)
        # 设置布局
        self.setLayout(layout)

        # 按钮1
        btn1 = QPushButton("按钮1")
        # 添加到布局器中
        layout.addWidget(btn1, Qt.AlignmentFlag.AlignTop)
        # 把按钮添加到布局中
        layout.addWidget(btn1)

        # 加了一个伸缩器（可以理解为一个弹簧）
        layout.addStretch(1)

        # 按钮2
        btn2 = QPushButton("按钮2")
        # 把按钮添加到布局中
        layout.addWidget(btn2)

        # 加了一个伸缩器（可以理解为一个弹簧）
        layout.addStretch(1)

        # 按钮3
        btn3 = QPushButton("按钮3")
        # 把按钮添加到布局中
        layout.addWidget(btn3)

        # 加了一个伸缩器（可以理解为一个弹簧）
        layout.addStretch(2)

        # 让当前的窗口使用这个排列的布局器
        self.setLayout(layout)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()

    app.exec_()