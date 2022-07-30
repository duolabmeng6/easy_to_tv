import sys

from PySide6.QtWidgets import *

from qtefun.组件.树形框 import 树形框


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle("树形框组件学习")
        self.show()

        self.树形框 = QTreeWidget(self)
        self.树形框.setGeometry(0, 0, 400, 300)
        self.树形框.show()
        self.树形框.setColumnCount(3)
        self.树形框.setHeaderLabels(['分类', "产品名称", '价格', '说明'])

        root = QTreeWidgetItem(self.树形框)
        root.setText(0, '产品')

        # 设置子节点1
        电子产品 = QTreeWidgetItem(root)
        电子产品.setText(0, '电子产品')

        水果 = QTreeWidgetItem(root)
        水果.setText(0, '水果')

        书籍 = QTreeWidgetItem(root)
        书籍.setText(0, '书籍')

        电子产品子项 = QTreeWidgetItem(电子产品)
        电子产品子项.setText(1, '苹果')
        电子产品子项.setText(2, '999')
        电子产品子项.setText(3, '真香')
        电子产品子项 = QTreeWidgetItem(电子产品)
        电子产品子项.setText(1, '华为')
        电子产品子项.setText(2, '999')
        电子产品子项.setText(3, '爱国')
        电子产品子项 = QTreeWidgetItem(电子产品)
        电子产品子项.setText(1, '小米')
        电子产品子项.setText(2, '999')
        电子产品子项.setText(3, '过保就坏')

        水果子项 = QTreeWidgetItem(水果)
        水果子项.setText(1, '苹果')
        水果子项.setText(2, '999')
        水果子项.setText(3, '好吃')
        水果子项 = QTreeWidgetItem(水果)
        水果子项.setText(1, '香蕉')
        水果子项.setText(2, '999')
        水果子项.setText(3, '好吃')
        水果子项 = QTreeWidgetItem(水果)
        水果子项.setText(1, '西瓜')
        水果子项.setText(2, '999')
        水果子项.setText(3, '好吃')

        书籍子项 = QTreeWidgetItem(书籍)
        书籍子项.setText(1, 'python入门')
        书籍子项.setText(2, '999')
        书籍子项.setText(3, '学习')
        书籍子项 = QTreeWidgetItem(书籍)
        书籍子项.setText(1, 'php入门')
        书籍子项.setText(2, '999')
        书籍子项.setText(3, '学习')
        书籍子项 = QTreeWidgetItem(书籍)
        书籍子项.setText(1, 'js入门')
        书籍子项.setText(2, '999')
        书籍子项.setText(3, '学习')

        self.树形框.expandAll()

        # self.树形框.clear()

        self.树形框1 = 树形框(self.树形框)
        self.树形框1.设置列数(3)
        self.树形框1.设置表头(['分类', "产品名称", '价格', '说明'])
        根节点 = self.树形框1.添加节点(None, 0, '产品')
        电子产品 = self.树形框1.添加节点(根节点, 0, '电子产品')
        水果 = self.树形框1.添加节点(根节点, 0, '水果')
        self.书籍 = 书籍 = self.树形框1.添加节点(根节点, 0, '书籍')

        水果子项 = self.树形框1.添加节点(水果, 0, '')
        水果子项.置标题(1, '苹果')
        水果子项.置标题(2, '999')
        水果子项.置标题(3, '好吃')

        书籍子项 = self.树形框1.添加节点(书籍)
        书籍子项.置标题多列(['python入门', '999', '学习'], 1)

        书籍子项 = self.树形框1.添加节点(书籍)
        书籍子项.置标题多列(['php入门', '999', '学习'], 1)

        书籍子项 = self.树形框1.添加节点(书籍)
        书籍子项.置标题多列(['js入门', '999', '学习'], 1)

        self.树形框1.删除节点(书籍子项)
        # self.树形框1.删除节点(书籍)
        p = self.树形框1.查询节点(书籍, 1, "python入门")  # type: QTreeWidgetItem
        print(p.text(1))
        self.树形框1.删除节点(p)

        self.树形框1.全部展开()

        print("取根节点数量", self.树形框1.取根节点数量())
        print("取列数", self.树形框1.取列数())

        # 绑定事件
        # currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous) 当前项目已更改
        # itemActivated(QTreeWidgetItem *item, int column) 项目已激活
        # itemChanged(QTreeWidgetItem *item, int column) 项目已更改
        # itemClicked(QTreeWidgetItem *item, int column) 已单击项目
        # itemCollapsed(QTreeWidgetItem *item) 项目已折叠
        # itemDoubleClicked(QTreeWidgetItem *item, int column) 项目被双击
        # itemEntered(QTreeWidgetItem *item, int column) 已输入的项目
        # itemExpanded(QTreeWidgetItem *item) 项目已展开
        # itemPressed(QTreeWidgetItem *item, int column) 按下的项目
        # itemSelectionChanged() 选择项目已更改
        self.树形框1.绑定事件当前项目已更改(self.当前项目已更改)
        self.树形框1.绑定事件项目已激活(self.项目已激活)
        self.树形框1.绑定事件项目已更改(self.项目已更改)
        self.树形框1.绑定事件已单击项目(self.已单击项目)
        self.树形框1.绑定事件项目已折叠(self.项目已折叠)
        self.树形框1.绑定事件项目被双击(self.项目被双击)
        self.树形框1.绑定事件已输入的项目(self.项目已输入)
        self.树形框1.绑定事件项目已展开(self.项目已展开)
        self.树形框1.绑定事件项目已按下(self.项目按下)

        # 创建按钮
        self.按钮 = QPushButton(self)
        self.按钮.clicked.connect(self.按钮点击)
        self.按钮.move(0, 300)
        self.按钮.resize(100, 40)
        self.按钮.setText('查找')
        self.按钮.show()

    def 按钮点击(self):
        p = self.树形框1.查询节点(self.书籍, 1, "php入门")  # type: QTreeWidgetItem
        print(p.text(1))
        self.树形框1.选中节点(p)
        self.树形框1.保证显示()

    def 当前项目已更改(self, 当前选中: QTreeWidgetItem, 上一个: QTreeWidgetItem):
        print("当前项目已更改", 当前选中.text(1))

    def 项目已激活(self, 选中项目: QTreeWidgetItem, 列: int):
        print("项目已激活", 选中项目.text(1))

    def 项目已更改(self, 选中项目: QTreeWidgetItem, 列: int):
        print("项目已更改", 选中项目.text(1))

    def 已单击项目(self, 选中项目: QTreeWidgetItem, 列: int):
        print("已单击项目", 选中项目.text(1))

    def 项目已折叠(self, 选中项目: QTreeWidgetItem):
        print("项目已折叠", 选中项目.text(1))

    def 项目被双击(self, 选中项目: QTreeWidgetItem, 列: int):
        print("项目被双击", 选中项目.text(1))

    def 项目已输入(self, 选中项目: QTreeWidgetItem, 列: int):
        print("项目已输入", 选中项目.text(1))

    def 项目已展开(self, 选中项目: QTreeWidgetItem):
        print("项目已展开", 选中项目.text(1))

    def 项目按下(self, 选中项目: QTreeWidgetItem, 列: int):
        print("项目按下", 选中项目.text(1),self.树形框1.现行选中项.column(),self.树形框1.现行选中项.row())

app = QApplication([])
# 创建窗口 400x400
win = Main()

sys.exit(app.exec())
