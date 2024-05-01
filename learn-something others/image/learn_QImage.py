from PyQt5.QtGui import QImage
import sys

# 创建一个 QImage 对象并加载图像
image = QImage('image.jpg')

# 获取图像的宽度和高度
width = image.width()
height = image.height()

# 获取图像的格式
format_str = image.format()

print(f"Image Width: {width}")
print(f"Image Height: {height}")
print(f"Image Format: {format_str}")