import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

from qtefun.组件.标签 import 标签


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle("标签组件学习")
        self.show()

        # 创建标签
        self.label = QLabel(self)
        # 设置标签的位置
        self.label.move(50, 50)
        # 设置标签的文本
        self.label.setText("Hello World!")
        # 显示标签
        self.label.show()

        self.标签1 = 标签(self.label)
        self.标签1.标题 = "祖国您好!"
        self.标签1.绑定事件被按下(self.点击事件)
        self.标签1.绑定事件被松开(self.松开事件)

    def 点击事件(self,e):
        print("点击事件")


    def 松开事件(self,e):
        print("松开事件")

app = QApplication([])
# 创建窗口 400x400
win = Main()



sys.exit(app.exec())
