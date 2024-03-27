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
        self.setWindowTitle('PyQt5程序之水平布局')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 垂直布局
        # outer_container = QVBoxLayout()
        outer_container = QHBoxLayout()

        # 垂直布局器中有两个组，一个是爱好组，另一个是性别组
        hobby_group = QGroupBox("爱好")
        # 创建一个垂直布局器
        v_inner_layout = QVBoxLayout()
        # 在爱好组中加入可选的爱好
        choice1 = QRadioButton("文明6")
        choice2 = QRadioButton("云顶之弈")
        choice3 = QRadioButton("毕业设计")
        # 把组件添加到布局器中
        v_inner_layout.addWidget(choice1)
        v_inner_layout.addWidget(choice2)
        v_inner_layout.addWidget(choice3)
        # 将布局器绑定到组
        hobby_group.setLayout(v_inner_layout)
        # 把当前的爱好组加入到垂直布局中
        outer_container.addWidget(hobby_group)

        gender_group = QGroupBox("性别")
        # 创建一个水平布局器
        h_inner_layout = QHBoxLayout()
        # 在爱好组中加入可选的爱好
        boy = QRadioButton("男")
        girl = QRadioButton("女")
        # 把组件添加到布局器中
        h_inner_layout.addWidget(boy)
        h_inner_layout.addWidget(girl)
        # 将布局器绑定到组
        gender_group.setLayout(h_inner_layout)
        # 把当前的性别组加入到垂直布局中
        outer_container.addWidget(gender_group)

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