import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('drawLine 示例')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(168, 34, 3))  # 设置画笔颜色
        # drawLine(x1, y1, x2, y2)
        painter.drawLine(10, 10, 100, 140)  # 绘制一条直线

        painter.setPen(QColor(34, 168, 3))  # 改变画笔颜色
        # drawLine(x1, y1, x2, y2)
        painter.drawLine(100, 140, 200, 10)  # 绘制另一条直线


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())