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
        self.setWindowTitle('QPainter translate 示例')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # 绘制原始图形
        painter.drawRect(10, 10, 50, 50)

        # 移动坐标系统
        painter.translate(100, 0)

        # 在新位置绘制相同的图形
        painter.drawRect(10, 10, 50, 50)

        # 再次移动坐标系统
        painter.translate(0, 100)

        # 再次在新位置绘制相同的图形
        painter.drawRect(10, 10, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())