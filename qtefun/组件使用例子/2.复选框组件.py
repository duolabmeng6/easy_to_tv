import sys

from PySide6.QtWidgets import *

from qtefun.组件.复选框 import 复选框


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle("复选框组件学习")
        self.show()

        self.复选框 = QCheckBox(self)
        self.复选框.move(50, 50)
        self.复选框.setText("Hello World!")
        self.复选框.show()

        self.复选框1 = 复选框(self.复选框)
        self.复选框1.标题 = "祖国您好!"
        self.复选框1.选中 = True
        self.复选框1.绑定事件选中状态切换(self.选中状态切换)
        self.复选框1.绑定事件状态改变(self.绑定事件状态改变)
        self.复选框1.绑定事件被点击(self.绑定事件被点击)

    def 选中状态切换(self, 选中状态):
        print("选中状态切换", 选中状态)

    def 绑定事件状态改变(self, 状态):
        print("绑定事件状态改变", 状态)

    def 绑定事件被点击(self):
        print("绑定事件被点击")


app = QApplication([])
# 创建窗口 400x400
win = Main()

sys.exit(app.exec())
