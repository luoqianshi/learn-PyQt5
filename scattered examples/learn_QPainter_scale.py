from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(560, 220, 800, 600)
        self.setWindowTitle('QPainter scale 示例')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # 绘制原始图形
        painter.drawRect(10, 10, 50, 50)

        # 缩放坐标系统
        painter.scale(2.0, 2.0)

        # 在缩放后的坐标系统中绘制相同的图形
        painter.drawRect(10, 10, 50, 50)

        # 再次缩放坐标系统
        # 这次的缩放是在前面有扩大了2倍的情况下再次缩放，所以其实是变回了原倍率
        # 每次调用 scale 方法时，当前的缩放比例会与新的缩放比例相乘。
        # 这意味着，如果你连续调用 scale 方法，每次的缩放都是基于上一次缩放后的结果进行的。
        # 也就是说，painter。scale的每次使用的效果是会叠加的！！！！
        # 也就是说，painter。scale的每次使用的效果是会叠加的！！！！
        # 也就是说，painter。scale的每次使用的效果是会叠加的！！！！
        painter.scale(0.5, 0.5)

        # 再次在缩放后的坐标系统中绘制相同的图形
        painter.drawRect(10, 10, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())