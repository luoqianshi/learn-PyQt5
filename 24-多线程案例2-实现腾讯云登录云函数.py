"""
动态加载ui文件
"""
import json
import sys
import time

import requests
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class login_QThread(QThread):
    # 定义一个用于子线程负责的登录相关操作的自定义信号，可以传入一个字符串参数
    login_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print("登录线程正在循环等待登录指令中.....")
            time.sleep(1)

    def handle_login_signal(self, username_password_json):
        username_password_json = json.loads(username_password_json)
        print(username_password_json.get("username"))
        print(username_password_json.get("password"))

        # 使用requests模块发送请求（POST）,基于腾讯云的云函数模块
        r = requests.post(url="https://service-kj2o34wc-1309141760.gz.tencentapigw.com.cn/release/pyqt_login", json=username_password_json)
        print("接收到腾讯云服务器的响应：", r.content.decode())
        ret = r.json()
        print(ret)


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.user_name = None
        self.password = None
        self.login_btn = None
        self.forget_btn = None
        self.text_browser = None
        self.login_thread = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("ui/login.ui")
        self.user_name = self.ui.lineEdit  # 这是获取用户名输入框
        self.password = self.ui.lineEdit_2  # 这是获取用户密码输入框
        # 设置 QLineEdit 为密文模式
        self.password.setEchoMode(QLineEdit.Password)
        self.login_btn = self.ui.pushButton  # 这是获取登录按钮
        self.forget_btn = self.ui.pushButton_2  # 这是获取忘记密码按钮
        self.text_browser = self.ui.textBrowser  # 这是获取文本浏览器

        # 创建一个用来专门进行登录操作的子线程
        self.login_thread = login_QThread()
        # 在UI初始化的时候就让登录线程处于启动的状态
        self.login_thread.start()

        # 给登录按钮绑定信号和槽函数
        self.login_btn.clicked.connect(self.login)
        # 给子线程中处理登录操作的信号绑定专门的响应函数
        self.login_thread.login_signal.connect(self.login_thread.handle_login_signal)

    def login(self):
        """这是登录按钮对应的槽函数"""
        user_name = self.user_name.text()
        password = self.password.text()
        # 主UI线程把当前获取到的用户名和密码的信息交给登录子线程专门去做登录相关的操作。
        # 以json字符串的形式来发送用户名和密码串
        self.login_thread.login_signal.emit(json.dumps({'username': user_name, 'password': password}))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    # 展示窗口
    # w.show()  # 在这种情况下这是一个错误示范
    w.ui.show()  # 这才是正确的操作
    sys.exit(app.exec_())
