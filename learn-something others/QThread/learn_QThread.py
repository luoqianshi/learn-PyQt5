from PyQt5.QtCore import QThread, pyqtSignal

class MyThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        print("Thread is running")
        # 在这里定义线程的执行逻辑

        self.finished_signal.emit()  # 发射执行完成的信号


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    thread = MyThread()

    def on_thread_finished():
        print("Thread execution completed")

    thread.finished_signal.connect(on_thread_finished)  # 连接信号和槽

    thread.start()  # 启动线程

    sys.exit(app.exec_())
