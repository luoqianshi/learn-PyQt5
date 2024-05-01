'''
QImage 和 QPixmap 是 PyQt 中用于处理图像的两个重要类，它们之间的主要区别在于 QImage 是用于处理图像数据的类，而 QPixmap 是用于在界面上显示图像的类。
区别：
QImage：QImage 是用于处理图像数据的类，它可以直接操作图像的像素数据，支持对图像进行像素级别的操作和处理。QImage 可以用于图像的加载、保存、编辑和处理等操作。
QPixmap：QPixmap 是用于在界面上显示图像的类，它通常用于在窗口、标签等控件上显示图像。QPixmap 可以从 QImage、文件或资源中加载图像，并在界面上进行显示。
'''

from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QImage, QPixmap
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建一个 QImage 对象并加载图像
image = QImage('image.jpg')

# 创建一个 QPixmap 对象并从 QImage 中创建
pixmap = QPixmap.fromImage(image)

# 创建一个标签控件并显示图像
label = QLabel()
label.setPixmap(pixmap)
label.show()

# 运行应用程序
sys.exit(app.exec_())