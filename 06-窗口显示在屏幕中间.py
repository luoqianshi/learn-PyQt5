import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)

    # 实例化QWidget类
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle('PyQt5程序之调整窗口大小')

    # 重置窗口大小
    w.resize(800, 600)

    # 调整窗口在屏幕中央显示
    # 获取我当前屏幕桌面的中心点的位置信息
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)
    x = center_pointer.x()
    y = center_pointer.y()
    print(x, y)

    # 打印窗口默认的几何信息（位置和大小）
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    # 获取窗口的默认几何信息
    old_x, old_y, width, height = w.frameGeometry().getRect()
    print(old_x, old_y, width, height)

    # 基于屏幕中心点和窗口的默认大小来调至合适的屏幕中央（自适应）
    w.move(x - int(width / 2), y - int(height / 2))

    # 设置窗口显示
    w.show()

    # 程序进行循环等待状态
    app.exec_()