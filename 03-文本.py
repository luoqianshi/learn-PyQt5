import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget类
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之文本')

    # 在窗口里面添加按钮控件，并绑定到w窗口
    btn = QPushButton("按钮", w)
    # 把按钮绑定到对应的窗口，等于是添加到窗口中显示
    # 设置按钮的位置
    btn.move(100, 100)

    # 在窗口里面添加文本标签，并绑定到w窗口
    label = QLabel("文本标签", w)
    # 设置文本标签的位置
    # label.move(100, 150)
    # 设置位置与大小 (x,y)(左上角0，0；横x，纵y) (w,h)(宽度，高度)
    label.setGeometry(100, 150, 150, 50)

    # 设置窗口背景色
    w.setStyleSheet("background-color: rgb(255, 255, 255);")

    # 设置窗口显示
    w.show()

    # 程序进行循环等待状态
    app.exec_()