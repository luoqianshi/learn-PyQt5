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
        self.resize(400, 300)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之QFormLayout')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 创建一个垂直布局作为窗口的主要布局
        mainLayout = QVBoxLayout()
        # 创建一个表单布局（本质上就是一行一行的部分）
        formLayout = QFormLayout()

        # 创建标签和对应的字段控件
        # 姓名行及其输入框
        nameLabel = QLabel('姓名:')
        nameLineEdit = QLineEdit()
        formLayout.addRow(nameLabel, nameLineEdit)
        # 电子邮箱行及其输入框
        emailLabel = QLabel('电子邮箱:')
        emailLineEdit = QLineEdit()
        formLayout.addRow(emailLabel, emailLineEdit)
        # 将表单布局添加到主布局中
        mainLayout.addLayout(formLayout)

        # 创建一个提交按钮，并添加到主布局中
        submitButton = QPushButton('提交')
        mainLayout.addWidget(submitButton)

        # 设置窗口的主布局
        self.setLayout(mainLayout)


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)
    # 实例化QWidget子类——MyWindow
    w = MyWindow()
    w.show()
    app.exec_()