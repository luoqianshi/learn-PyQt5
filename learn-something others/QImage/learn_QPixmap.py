from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建一个 QPixmap 对象并加载图像
pixmap = QPixmap('image.jpg')

# 获取图像的尺寸信息
size = pixmap.size()
print(size)

# 创建一个标签控件并显示图像
label = QLabel()
label.setPixmap(pixmap)
label.show()

# 运行应用程序
sys.exit(app.exec_())