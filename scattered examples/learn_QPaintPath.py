from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath, QPen
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(560, 220, 800, 600)
        self.setWindowTitle('QPainterPath 示例')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # 可以理解为是一个路径绘制者，可以逐条曲线得‘画’
        # （我更愿意称之为构筑）各种复杂图形。
        # 当最后构筑完毕后，再通过painter类绘制出来。

        path = QPainterPath()
        # 奠定初始点(20，20)
        path.moveTo(20, 20)
        # 画直线到第二个点(200,20)
        path.lineTo(200, 20)
        # 画贝赛尔曲线到第三个点（220，220）
        path.cubicTo(220, 5, 275, 150, 220, 220)
        # 画直线到最后一个点（20，220）
        path.lineTo(20, 220)
        # 闭合路径，会自动连接当前的点和初始点。
        path.closeSubpath()

        # 上面其实只是完成了路径的规划，最后还是得靠painter类来画在画布上。
        painter.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())