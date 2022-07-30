import sys

from PySide6.QtWidgets import *

from qtefun.组件.表格 import 表格


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("表格组件学习")
        self.show()

        self.表格 = QTableWidget(self)
        self.表格1 = 表格(self.表格)
        self.表格.setGeometry(0, 0, 600, 400)
        self.表格.show()
        self.表格1.设置列数(4)
        # self.表格1.设置行数(100)
        self.表格1.设置表头(['分类', "产品名称", '价格', '说明'])
        self.表格1.设置整行选择()
        self.表格1.设置单一选择()

        # 插入10行测试数据
        for i in range(5):
            self.表格1.插入行(i)
            self.表格1.设置项目文本(i, 0, "分类1")
            self.表格1.设置项目文本(i, 1, "产品名称1")
            self.表格1.设置项目文本(i, 2, "价格1")
            self.表格1.设置项目文本(i, 3, "说明1")

        for i in range(5):
            self.表格1.插入行(i)
            self.表格1.设置单元格按钮(i, 0, "操作", lambda 行号, 列号: print(行号, 列号))
            self.表格1.设置单元格复选框(i, 1, True, "选择", lambda 行号, 列号, 状态: print(行号, 列号, 状态))
            self.表格1.设置单元格文本框(i, 2, "价格1", lambda 行号, 列号, 文本: print(行号, 列号, 文本))
            self.表格1.设置单元格组合框(i, 3, ['真', '假'], 0, lambda 行号, 列号, 文本: print(行号, 列号, 文本))

            # 创建按钮
            self.按钮 = QPushButton(self)
            self.按钮.clicked.connect(self.按钮点击)
            self.按钮.move(0, 400)
            self.按钮.resize(100, 40)
            self.按钮.setText('查找')
            self.按钮.show()

    def 按钮点击(self):
        pass
        数据 = self.表格1.导出数据()
        print(数据)



app = QApplication([])
# 创建窗口 400x400
win = Main()

sys.exit(app.exec())
