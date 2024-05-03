from PyQt5.QtGui import QPainterPath

# 创建一个 QPainterPath 对象
path = QPainterPath()
path.moveTo(10, 10)
path.lineTo(50, 10)
path.lineTo(50, 50)
path.lineTo(10, 50)
path.closeSubpath()

# 获取路径的边界矩形
bounding_rect = path.boundingRect()

# 打印边界矩形的坐标和尺寸
print("Bounding Rect:")
print("Top Left Point: ({}, {})".format(bounding_rect.topLeft().x(), bounding_rect.topLeft().y()))
print("Bottom Right Point: ({}, {})".format(bounding_rect.bottomRight().x(), bounding_rect.bottomRight().y()))
print("Width: {}".format(bounding_rect.width()))
print("Height: {}".format(bounding_rect.height()))