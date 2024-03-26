"""
动态加载ui文件
"""
import sys
import time

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.myThread = None
        self.ui = None
        self.ui_thread_btn = None
        self.QThread_btn = None
        self.text_edit = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("ui/QThread-1.ui")
        self.ui_thread_btn = self.ui.pushButton
        self.QThread_btn = self.ui.pushButton_2
        self.text_edit = self.ui.textEdit

        # 给登录按钮绑定信号和槽函数
        self.ui_thread_btn.clicked.connect(self.click1)
        # 给忘记密码按钮绑定信号和槽函数
        self.QThread_btn.clicked.connect(self.click2)

    def click1(self):
        for i in range(5):
            time.sleep(1)
            print(f"正在使用UI线程，......{i+1}")

    def click2(self):
        # 这里的子线程必须要写成self的属性！！否则无法实现异步的效果！
        # 因为我们并不希望myThread线程在click2函数运行结束的时候就被销毁，我们希望它可以根据它的需求继续留存着。
        self.myThread = MyQThread()
        self.myThread.start()


class MyQThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            time.sleep(1)
            print(f"正在使用子线程，......{i+1}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget()
    # 展示窗口
    # w.show()  # 在这种情况下这是一个错误示范
    w.ui.show()  # 这才是正确的操作

    sys.exit(app.exec_())
