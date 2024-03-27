import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)
    # 实例化QWidget类
    w = QWidget()
    w.resize(1000, 500)
    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之QLabel展示图片')
    # 创建一个位图变量
    photo = QPixmap('imgs/Florian.jpg')
    # 按比例缩放至1000*500
    scaled_photo = photo.scaled(1000, 500, Qt.KeepAspectRatio)
    # 创建一个标签控件实例
    label = QLabel(w)
    # 将位图变量绑定到标签控件实例上
    label.setPixmap(scaled_photo)
    # 设置窗口显示
    w.show()
    # 程序进行循环等待状态
    app.exec_()