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
        # 设置 QLineEdit 为密文模式
        self.password.setEchoMode(QLineEdit.Password)
        self.login_btn = self.ui.pushButton  # 这是获取登录按钮
        self.forget_btn = self.ui.pushButton_2  # 这是获取忘记密码按钮
        self.text_browser = self.ui.textBrowser  # 这是获取文本浏览器

        # 给登录按钮绑定信号和槽函数
        self.login_btn.clicked.connect(self.login)
        # 给忘记密码按钮绑定信号和槽函数
        self.forget_btn.clicked.connect(self.forget)

    def login(self):
        """这是登录按钮对应的槽函数"""
        user_name = self.user_name.text()
        password = self.password.text()
        # print("您当前输入的用户名为：" + user_name)
        # print("您当前输入的密码为：" + password)

        # 模拟正在进行云服务器的登录,手动延时
        for i in range(3):
            time.sleep(1)
            print(f"正在进行云服务器的登录，......{i+1}")

        # 进行简单的登录密码的验证
        if user_name == "admin" and password == "123456":
            self.text_browser.setText("登录成功！\n"
                                      f"欢迎{user_name}...\n"
                                      f"这里手动模拟出来的卡顿感其实是在提醒说最好使用多线程的方案来实现...")
            self.text_browser.repaint()  # 刷新
        else:
            self.text_browser.setText("用户名或密码错误，请重试...")
            self.text_browser.repaint()  # 刷新

    def forget(self):
        print("找回密码成功！")
        self.text_browser.setText("找回密码成功！")

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
