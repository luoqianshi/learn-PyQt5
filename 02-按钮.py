import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)
    # 实例化QWidget类
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之按钮')
    # 在窗口里面添加按钮控件
    btn = QPushButton("按钮")
    # 把按钮绑定到对应的窗口，等于是添加到窗口中显示
    btn.setParent(w)
    # 设置窗口背景色
    w.setStyleSheet("background-color: rgb(255, 255, 255);")
    # 设置窗口显示
    w.show()
    # 程序进行循环等待状态
    app.exec_()