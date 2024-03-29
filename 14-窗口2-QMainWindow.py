import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyQMainWindow(QMainWindow):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI控件的初始化操作
        super().__init__()
        # 把对当前的窗口控件的具体的UI布局写到有个专门的方法中，以免初始化的方法内容太臃肿
        self.init_ui()

    def init_ui(self):
        # 设置大小
        self.resize(700, 400)
        # 设置窗口标题
        self.setWindowTitle('PyQt5程序之QMainWindow')
        # 设置窗口图标
        self.setWindowIcon(QIcon('imgs/clock.png'))

        # 创建菜单和动作
        file_menu = QMenu('文件', self)
        new_action = QAction('新建', self)
        open_action = QAction('打开', self)
        save_action = QAction('保存', self)
        exit_action = QAction('退出', self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # 创建了一个分割的横线
        file_menu.addAction(exit_action)

        # 创建菜单栏并添加菜单
        menu_bar = QMenuBar(self)
        menu_bar.addMenu(file_menu)
        self.setMenuBar(menu_bar)

        # 创建工具栏
        tool_bar = self.addToolBar('工具')
        edit_action = QAction('编辑', self)
        tool_bar.addAction(edit_action)

        # 设置中心部件
        central_MainWidget = QWidget(self)  # 使得中心区域可以容纳多个以上的组件。
        v_layout = QVBoxLayout()
        # 创建一个文本编辑框
        text_edit = QTextEdit(self)
        # 创建一个标签
        label = QLabel("我是PyQt5的三种重要窗口之一,"
                       "\n是QMainWindow窗口的示例~"
                       "\n我的特点是自带菜单栏，工具栏，状态栏和中心内容区。", self)
        # 调整label的字体大小为30，颜色为green
        label.setFont(QFont("微软雅黑", 20, QFont.Bold))
        label.setStyleSheet("color: green")
        # 创建一个按钮，点击时更新状态栏信息
        self.button = QPushButton('点击更新状态栏', self)
        # 将控件绑定到布局
        v_layout.addWidget(text_edit)
        v_layout.addWidget(label)
        v_layout.addWidget(self.button)
        # 将布局绑定到主控件
        central_MainWidget.setLayout(v_layout)
        # 将主控件绑定到QMainWindow的中心内容区
        self.setCentralWidget(central_MainWidget)

        # 创建状态栏
        self.status_bar = QStatusBar(self)
        self.status_bar.showMessage('欢迎使用应用程序')
        # 设置状态栏的永久显示项
        permanent_label = QLabel('永久信息：当前模式')
        self.status_bar.addPermanentWidget(permanent_label)
        self.setStatusBar(self.status_bar)

        # 连接动作的信号和槽
        # （连接上了事件，有事件相关的控件都加了self变成了当前类的属性：类变量，
        # 这样才可以在当前类的其它方法中直接使用。）
        exit_action.triggered.connect(self.close)
        self.button.clicked.connect(self.update_statusbar)

    """
    * 这是中心内容区的按钮点击了之后用来更新状态栏的信息的方法。
    """
    def update_statusbar(self):
        # 更新状态栏的临时信息
        self.status_bar.showMessage('新的风暴已经出现！', 5000)  # 5秒后消失


if __name__ == '__main__':
    # 实例化QApplication类
    # sys.argv是命令行的参数
    app = QApplication(sys.argv)
    # 实例化QMainWindow子类——MyQMainWindow
    w = MyQMainWindow()
    w.show()
    app.exec_()