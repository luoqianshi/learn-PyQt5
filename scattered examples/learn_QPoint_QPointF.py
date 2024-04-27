from PyQt5.QtCore import QPoint, QPointF

# 创建一个点
point = QPoint(10, 20)

# 访问坐标
print("X coordinate:", point.x())  # 输出: X coordinate: 10
print("Y coordinate:", point.y())  # 输出: Y coordinate: 20

# 修改坐标
point.setX(30)
point.setY(40)
print("Modified point:", point.x(), point.y())  # 输出: Modified point: 30 40


''''''''''''''''''''''''

# 创建一个浮点坐标点
pointF = QPointF(10.5, 20.5)

# 访问坐标
print("X coordinate:", pointF.x())  # 输出: X coordinate: 10.5
print("Y coordinate:", pointF.y())  # 输出: Y coordinate: 20.5

# 修改坐标
pointF.setX(30.1)
pointF.setY(40.2)
print("Modified point:", pointF.x(), pointF.y())  # 输出: Modified point: 30.1 40.2

''''''''''''''''''''''''

# QPoint 加法和减法
point1 = QPoint(10, 20)
point2 = QPoint(5, 3)
result_add = point1 + point2
result_sub = point1 - point2
print("QPoint Addition:", result_add)  # 输出: QPoint Addition: PyQt5.QtCore.QPoint(15, 23)
print("QPoint Subtraction:", result_sub)  # 输出: QPoint Subtraction: PyQt5.QtCore.QPoint(5, 17)

# QPointF 加法和减法
pointF1 = QPointF(10.5, 20.5)
pointF2 = QPointF(5.5, 3.5)
resultF_add = pointF1 + pointF2
resultF_sub = pointF1 - pointF2
print("QPointF Addition:", resultF_add)  # 输出: QPointF Addition: PyQt5.QtCore.QPointF(16.0, 24.0)
print("QPointF Subtraction:", resultF_sub)  # 输出: QPointF Subtraction: PyQt5.QtCore.QPointF(5.0, 17.0)

# QPoint 乘法
point = QPoint(10, 20)
result_mul = point * 2
print("QPoint Multiplication:", result_mul)  # 输出: QPoint Multiplication: PyQt5.QtCore.QPoint(20, 40)

# QPointF 乘法和除法
pointF = QPointF(10.5, 20.5)
resultF_mul = pointF * 2
resultF_div = pointF / 2
print("QPointF Multiplication:", resultF_mul)  # 输出: QPointF Multiplication: PyQt5.QtCore.QPointF(21.0, 41.0)
print("QPointF Division:", resultF_div)  # 输出: QPointF Division: PyQt5.QtCore.QPointF(5.25, 10.25)

# 等于和不等于
point1 = QPoint(10, 20)
point2 = QPoint(10, 20)
point3 = QPoint(5, 5)
print("QPoint Equal:", point1 == point2)  # 输出: QPoint Equal: True
print("QPoint Not Equal:", point1 != point3)  # 输出: QPoint Not Equal: True