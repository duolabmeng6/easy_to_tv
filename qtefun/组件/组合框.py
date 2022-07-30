from PySide6 import QtWidgets
from qtefun.组件.组件公共类 import 组件公共类


class 组合框(组件公共类):
    对象 = None  # type: QtWidgets.QComboBox
    # 清空
    def 清空(self):
        self.对象.clear()
    # 添加项目
    def 添加项目(self, 文本: str):
        return self.对象.addItem(文本)

    # 删除项目
    def 删除项目(self, 索引: int):
        return self.对象.removeItem(索引)

    # 插入项目
    def 插入项目(self, 索引: int, 文本: str):
        return self.对象.insertItem(索引, 文本)

    # 取项目数量
    def 取项目数量(self):
        return self.对象.count()

    # 取项目文本
    def 取项目文本(self, 索引: int):
        return self.对象.item(索引).text()

    # 取项目索引
    def 取项目索引(self, 文本: str):
        for i in range(self.对象.count()):
            if self.对象.item(i).text() == 文本:
                return i
        return -1

    # 取选中项目索引
    def 取选中项目索引(self):
        return self.对象.currentRow()

    # 设置选中项目索引
    def 设置选中项目索引(self, 索引: int):
        return self.对象.setCurrentRow(索引)

    def 绑定事件项目被选择(self, 回调函数):
        """
        回调函数(索引:int)
        """
        self.对象.currentIndexChanged.connect(回调函数)

    # 获取和设置属性 现行选中项
    @property
    def 现行选中项(self):
        return self.取选中项目索引()

    @现行选中项.setter
    def 现行选中项(self, 索引: int):
        return self.设置选中项目索引(索引)
