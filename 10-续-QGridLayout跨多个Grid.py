import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # 创建网格布局
        layout = QGridLayout(self)
        # 创建按钮并添加到布局中
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '=', '+'
        ]
        row = 0
        col = 0
        for btnText in buttons:
            if btnText == '0':
                # 为数字“0”的按钮设置 columnSpan 为 2
                button = QPushButton(btnText, self)
                layout.addWidget(button, row, col, 1, 2)  # 占据1行2列
                col += 2  # 跳过下一列
            else:
                button = QPushButton(btnText, self)
                layout.addWidget(button, row, col)
                col += 1
                # 换行条件：当到达每行的最后一个按钮时
            if col == 4 and btnText != '0':
                row += 1
                col = 0
                # 设置窗口的基本属性
        self.setLayout(layout)
        self.setWindowTitle('计算器示例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
