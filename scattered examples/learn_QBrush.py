import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 100)
        self.setWindowTitle('QBrush 示例')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.drawRect(10, 15, 90, 60)

        painter.setBrush(QBrush(Qt.yellow, Qt.Dense1Pattern))
        painter.drawRect(130, 15, 90, 60)

        painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
        painter.drawRect(250, 15, 90, 60)

        painter.setBrush(QBrush(Qt.blue, Qt.BDiagPattern))
        painter.drawRect(370, 15, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())