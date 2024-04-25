from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘图示例')
        self.setGeometry(560, 220, 800, 600)
        self.points = []  # 用于存储绘制点的列表

    def mousePressEvent(self, event):
        # 鼠标按下时，开始记录点
        self.points = [event.pos()]

    def mouseMoveEvent(self, event):
        # 鼠标移动时，添加点并更新绘图
        self.points.append(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        # 鼠标释放时，完成当前线条的绘制
        self.points.append(event.pos())
        self.update()

    def paintEvent(self, event):
        if self.points:
            qp = QPainter(self)
            qp.setPen(QPen(Qt.black, 2))
            for i in range(len(self.points) - 1):
                qp.drawLine(self.points[i], self.points[i + 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DrawingWidget()
    demo.show()
    sys.exit(app.exec_())