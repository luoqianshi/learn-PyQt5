import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        # 设置大小
        self.resize(200, 200)
        self.setWindowTitle('自定义对话框')

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel('请输入一些文本:', self)
        layout.addWidget(self.label)

        # 创建按钮
        self.ok_button = QPushButton('确定', self)
        self.ok_button.clicked.connect(self.accept)  # 点击按钮时接受对话框
        layout.addWidget(self.ok_button)

        # 设置对话框的布局
        self.setLayout(layout)

    def get_text(self):
        # 此处仅为示例，实际上你可能需要从某个输入框获取文本
        return "示例文本"  # 假设这是用户输入的文本

class MyQMainWindow(QMainWindow):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()
        # 把对当前的窗口控件的具体的UI布局写到有个专门的方法中，以免初始化的方法内容太臃肿
        self.init_ui()

    def init_ui(self):
        # 设置大小
        self.resize(400, 400)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之QDialog')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 添加一个按钮用于打开对话框
        self.open_dialog_button = QPushButton('打开对话框', self)
        self.open_dialog_button.clicked.connect(self.show_dialog)
        self.setCentralWidget(self.open_dialog_button)

    def show_dialog(self):
        # 创建并显示自定义对话框
        dialog = CustomDialog()
        if dialog.exec_():  # 执行对话框，如果用户点击了确定按钮则返回True
            text = dialog.get_text()  # 获取用户输入的文本
            print(f"用户输入的文本是: {text}")


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QMainWindow子类——MyQMainWindow
    w = MyQMainWindow()
    w.show()

    app.exec_()