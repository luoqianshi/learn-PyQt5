"""
动态加载ui文件
"""
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.user_name = None
        self.password = None
        self.login_btn = None
        self.forget_btn = None
        self.text_browser = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("ui/login.ui")
        # self.explain_function()  # 这是一个用来对ui文件进行输出测试的测试方法
        self.user_name = self.ui.lineEdit  # 这是获取用户名输入框
        self.password = self.ui.lineEdit_2  # 这是获取用户密码输入框
        self.login_btn = self.ui.pushButton  # 这是获取登录按钮
        self.forget_btn = self.ui.pushButton_2  # 这是获取忘记密码按钮
        self.text_browser = self.ui.textBrowser  # 这是获取文本浏览器

        # 给登录按钮绑定信号和槽函数
        self.login_btn.clicked.connect(self.login)
        # 给忘记密码按钮绑定信号和槽函数
        self.forget_btn.clicked.connect(self.forget)
        # 给文本浏览器绑定信号和槽函数
        self.text_browser.textChanged.connect(self.show_text)

    def login(self):
        user_name = self.user_name.text()
        password = self.password.text()
        print("您当前输入的用户名为：" + user_name)
        print("您当前输入的密码为：" + password)
        print("登录成功！")
        # self.text_browser.setText("登录成功！")

    def forget(self):
        print("找回密码成功！")
        # self.text_browser.setText("找回密码成功！")

    def show_text(self):
        # 获取当前时间的字符串
        self.text_browser.setText("文本信息改变" + time.gmtime().__str__())

    def explain_function(self):
        # 往下是使用print输出来尝试了解我们所载入的ui对象中到底有些什么东西？
        print(self.ui)  # 打印ui文件中的最顶层的对象
        print(self.ui.__dict__)  # 获取ui文件中最顶层的对象中的所有的属性
        """
        以下是ui文件中最顶层的对象中的所有的属性，以键值对的方式给出：
        {'label': <PyQt5.QtWidgets.QLabel object at 0x0000014D5EE89750>,
         'lineEdit': <PyQt5.QtWidgets.QLineEdit object at 0x0000014D5EE89870>, 
         'lineEdit_2': <PyQt5.QtWidgets.QLineEdit object at 0x0000014D5EE89900>, 
         'label_2': <PyQt5.QtWidgets.QLabel object at 0x0000014D5EE89990>, 
         'pushButton': <PyQt5.QtWidgets.QPushButton object at 0x0000014D5EE89A20>, 
         'pushButton_2': <PyQt5.QtWidgets.QPushButton object at 0x0000014D5EE89AB0>, 
         'textBrowser': <PyQt5.QtWidgets.QTextBrowser object at 0x0000014D5EE89B40>}
        """
        print(self.ui.label.text())  # ui文件中最顶层的对象中的label对象的text()方法

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget()
    # 展示窗口
    # w.show()  # 在这种情况下这是一个错误示范
    w.ui.show()  # 这才是正确的操作

    sys.exit(app.exec_())