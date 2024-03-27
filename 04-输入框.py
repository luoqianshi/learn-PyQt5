import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)
    # 实例化QWidget类
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之输入框')
    # 纯文本
    label = QLabel("账号：", w)
    label.setGeometry(100, 100, 50, 30)
    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(150, 100, 200, 30)
    # 在窗口里面添加控件
    btn = QPushButton("注册", w)
    btn.setGeometry(200, 150, 80, 30)
    # 设置窗口显示
    w.show()
    # 程序进行循环等待状态
    app.exec_()