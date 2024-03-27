import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton


class FormLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        # 创建表单布局
        layout = QFormLayout()

        # 添加控件到布局中
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Age:", QLineEdit())

        # 在同一行添加不同类型的控件
        button1 = QPushButton("Submit")
        button2 = QPushButton("Cancel")
        layout.addRow(button1, button2)

        # 设置窗口的基本属性
        self.resize(400, 100)
        self.setLayout(layout)
        self.setWindowTitle('QFormLayout 示例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FormLayoutExample()
    ex.show()
    sys.exit(app.exec_())