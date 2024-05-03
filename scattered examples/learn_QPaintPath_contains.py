from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QColor
from PyQt5.QtCore import Qt, QPointF

class Canvas(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.moveTo(50, 50)
        path.lineTo(150, 50)
        path.lineTo(100, 150)
        path.closeSubpath()

        painter.setBrush(QColor(Qt.blue))
        painter.drawPath(path)

        # 判断点是否在闭合图形内部
        point = QPointF(100, 100)
        if path.contains(point):
            painter.drawText(point, "Point Inside")


if __name__ == '__main__':
    app = QApplication([])
    canvas = Canvas()
    canvas.resize(200, 200)
    canvas.show()
    app.exec_()