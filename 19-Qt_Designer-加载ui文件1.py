"""
动态加载ui文件
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("ui/AuxiliaryImageTagging.ui")
    # 展示窗口
    ui.show()
    sys.exit(app.exec_())