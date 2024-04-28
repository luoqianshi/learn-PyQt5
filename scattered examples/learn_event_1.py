from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

CURSOR_DRAW = Qt.CrossCursor

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Canvas 示例')

    def enterEvent(self, event):
        self.override_cursor(CURSOR_DRAW)

    def leaveEvent(self, event):
        self.restore_cursor()

    def focusOutEvent(self, event):
        self.restore_cursor()

    def override_cursor(self, cursor_type):
        self.setCursor(cursor_type)

    def restore_cursor(self):
        self.unsetCursor()


if __name__ == '__main__':
    app = QApplication([])
    canvas = Canvas()
    canvas.show()
    app.exec_()