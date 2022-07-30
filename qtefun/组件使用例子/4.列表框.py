import sys

from PySide6.QtWidgets import *

from qtefun.组件.列表框 import 列表框


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle("列表框组件学习")
        self.show()

        self.列表框 = QListWidget(self)
        self.列表框.setGeometry(50, 50, 200, 200)
        self.列表框.show()

        self.列表框1 = 列表框(self.列表框)

        self.列表框1.添加项目("祖国您好!1")
        self.列表框1.添加项目("祖国您好!2")
        self.列表框1.添加项目("祖国您好!3")
        self.列表框1.添加项目("祖国您好!4")
        self.列表框1.添加项目("祖国您好!5")

        self.列表框1.删除项目(4)
        self.列表框1.删除项目(0)

        # 插入项目
        self.列表框1.插入项目(0, "祖国您好!6")

        项目数量 = self.列表框1.取项目数量()
        print("项目数量", 项目数量)

        项目文本 = self.列表框1.取项目文本(0)
        print("项目文本", 项目文本)

        # 取项目索引
        项目索引 = self.列表框1.取项目索引("祖国您好!3")
        print("项目索引", 项目索引)

        # 取当前选中项目索引
        选中项目索引 = self.列表框1.取选中项目索引()
        print("选中项目索引", 选中项目索引)

        # 绑定事件选中项目被改变
        self.列表框1.绑定事件选中项目已更改(self.项目选择已更改)
        # 绑定事件项目被点击
        self.列表框1.绑定事件项目被点击(self.项目被点击)
        # 绑定事件当前项目已更改
        self.列表框1.绑定事件当前项目已更改(self.当前项目已更改)
        # 绑定事件当前行已更改
        self.列表框1.绑定事件当前行已更改(self.当前行已更改)
        # 绑定事件当前文本已更改 绑定事件项目已更改 绑定事件项目被双击 绑定事件项目被鼠标进入 绑定事件项目被鼠标按下
        self.列表框1.绑定事件当前文本已更改(self.当前文本已更改)
        self.列表框1.绑定事件项目已更改(self.项目已更改)
        self.列表框1.绑定事件项目被双击(self.项目被双击)
        self.列表框1.绑定事件项目被鼠标进入(self.项目被鼠标进入)
        self.列表框1.绑定事件项目被鼠标按下(self.项目被鼠标按下)

        self.列表框1.现行选中项 = 2




    def 项目选择已更改(self):
        print("项目选择已更改", self.列表框1.取选中项目索引())

    def 项目被点击(self):
        print("项目被点击", self.列表框1.取选中项目索引())

    def 当前项目已更改(self, 当前选中: QListWidgetItem, 上一个: QListWidgetItem):
        print("当前项目已更改", 当前选中.text(), 上一个.text())

    def 当前行已更改(self, 当前行: int):
        print("当前行已更改", 当前行)

    def 当前文本已更改(self, 当前文本: str):
        print("当前文本已更改", 当前文本)

    def 项目已更改(self, 项目索引: int, 项目文本: str):
        print("项目已更改", 项目索引, 项目文本)

    def 项目被双击(self, 项目索引: int):
        print("项目被双击", 项目索引)

    def 项目被鼠标进入(self, 项目索引: int):
        print("项目被鼠标进入", 项目索引)

    def 项目被鼠标按下(self, 项目索引: int):
        print("项目被鼠标按下", 项目索引)


app = QApplication([])
# 创建窗口 400x400
win = Main()

sys.exit(app.exec())
