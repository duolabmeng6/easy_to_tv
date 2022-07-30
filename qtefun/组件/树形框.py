from PySide6 import QtWidgets
from PySide6.QtWidgets import QTreeWidgetItem

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qtreewidget.html
# 树形框
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

class 树形框节点类(QTreeWidgetItem):

    def 置标题(self, 第几列, 标题):
        self.setText(第几列, 标题)

    def 置标题多列(self, 标题列表, 从第几列开始=0):
        i = 从第几列开始
        for 标题 in 标题列表:
            self.setText(i, 标题)
            i = i + 1


class 树形框(组件公共类):
    对象 = None  # type: QtWidgets.QTreeWidget

    # 设置列数
    def 设置列数(self, 列数):
        self.对象.setColumnCount(列数)

    # 设置表头
    def 设置表头(self, 表头=[]):
        self.对象.setHeaderLabels(表头)

    # 添加节点
    def 添加节点(self, 父节点=None, 第几列=None, 文本=None):
        if 父节点 is None:
            父节点 = self.对象
        节点 = 树形框节点类(父节点)
        if 第几列 is not None:
            节点.setText(第几列, 文本)
        return 节点

    # 删除节点
    def 删除节点(self, 节点):
        节点.parent().removeChild(节点)

    # 查询节点
    def 查询节点(self, 父节点=None, 第几列=0, 文本=None):
        if 父节点 is None:
            父节点 = self.对象
        for i in range(父节点.childCount()):
            节点 = 父节点.child(i)
            if 节点.text(第几列) == 文本:
                return 节点  # type : QTreeWidgetItem
        return None

    # 查询节点
    def 查询节点列表(self, 父节点=None, 文本列表=None):
        if 父节点 is None:
            父节点 = self.对象
        节点列表 = []
        for i in range(父节点.childCount()):
            节点 = 父节点.child(i)
            if 节点.text(0) in 文本列表:
                节点列表.append(节点)
        return 节点列表

    # 选中节点
    def 选中节点(self, 节点):
        self.对象.setCurrentItem(节点)

    # 保证显示
    def 保证显示(self):
        # 把选择的项目显示出来
        self.对象.scrollToItem(self.对象.currentItem())

    # 取项目数量
    def 取根节点数量(self):
        return self.对象.topLevelItemCount()

    def 取列数(self):
        return self.对象.columnCount()

    # 全部展开
    def 全部展开(self):
        self.对象.expandAll()

    # 获取和设置属性 现行选中项
    @property
    def 现行选中项(self):
        return self.对象.currentIndex()

    @现行选中项.setter
    def 现行选中项(self, 索引: int):
        return self.对象.setCurrentIndex(索引)

    # currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous) 当前项目已更改
    def 绑定事件当前项目已更改(self, 回调函数):
        """
        回调函数(当前选中:QTreeWidgetItem, 上一个:QTreeWidgetItem)
        """
        self.对象.currentItemChanged.connect(回调函数)

    # itemActivated(QTreeWidgetItem *item, int column) 项目已激活
    def 绑定事件项目已激活(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemActivated.connect(回调函数)

    # itemChanged(QTreeWidgetItem *item, int column) 项目已更改
    def 绑定事件项目已更改(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemChanged.connect(回调函数)

    # itemCollapsed(QTreeWidgetItem *item) 项目已折叠
    def 绑定事件项目已折叠(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem)
        """
        self.对象.itemCollapsed.connect(回调函数)

    # itemExpanded(QTreeWidgetItem *item) 项目已展开
    def 绑定事件项目已展开(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem)
        """
        self.对象.itemExpanded.connect(回调函数)

    # itemPressed(QTreeWidgetItem *item, int column) 项目已按下
    def 绑定事件项目已按下(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemPressed.connect(回调函数)

    # itemSelectionChanged() 选择已更改
    def 绑定事件选择已更改(self, 回调函数):
        """
        回调函数()
        """
        self.对象.itemSelectionChanged.connect(回调函数)

    # itemDoubleClicked(QTreeWidgetItem *item, int column) 项目被双击
    def 绑定事件项目被双击(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemDoubleClicked.connect(回调函数)

    # itemEntered(QTreeWidgetItem *item, int column) 已输入的项目
    def 绑定事件已输入的项目(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemEntered.connect(回调函数)

    # # itemClicked(QTreeWidgetItem *item, int column) 已单击项目
    def 绑定事件已单击项目(self, 回调函数):
        """
        回调函数(节点:QTreeWidgetItem, 列:int)
        """
        self.对象.itemClicked.connect(回调函数)
