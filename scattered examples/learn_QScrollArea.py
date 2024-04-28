from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QMainWindow
import sys

class ScrollExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滚动条示例')
        self.setGeometry(100, 100, 400, 300)

        # 加载一个巨大的图片
        pixmap = QPixmap(r"..\imgs\huge_img.jpg")

        # 创建一个标签用于显示图片
        image_label = QLabel()
        image_label.setPixmap(pixmap)

        # 创建一个滚动区域并设置内容
        scroll_area = QScrollArea()
        scroll_area.setWidget(image_label)
        scroll_area.setWidgetResizable(True)

        self.setCentralWidget(scroll_area)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScrollExample()
    sys.exit(app.exec_())