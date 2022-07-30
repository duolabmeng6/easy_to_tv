from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qlistwidget.html
# 列表框 添加项目 删除项目 取项目数量 取项目文本 取项目索引 取当前选中项目索引 取当前选中项目文本
# 事件
# void	currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous) # 当前选中项目改变时触发
# void	currentRowChanged(int currentRow) # 当前选中项目索引改变时触发
# void	currentTextChanged(const QString &currentText) # 当前选中项目改变时触发
# void	itemActivated(QListWidgetItem *item) # 项目被点击时触发
# void	itemChanged(QListWidgetItem *item) # 项目改变时触发
# void	itemClicked(QListWidgetItem *item) # 项目被点击时触发
# void	itemDoubleClicked(QListWidgetItem *item) # 项目被双击时触发
# void	itemEntered(QListWidgetItem *item) # 项目被鼠标进入时触发
# void	itemPressed(QListWidgetItem *item) # 项目被按下时触发
# void	itemSelectionChanged() # 选中项目改变时触发

class 列表框(组件公共类):
    对象 = None  # type: QtWidgets.QListWidget

    # 添加项目
    def 添加项目(self, 文本: str):
        return self.对象.addItem(文本)

    # 删除项目
    def 删除项目(self, 索引: int):
        return self.对象.takeItem(索引)

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

    def 绑定事件当前项目已更改(self, 回调函数):
        """
        回调函数(当前选中:QListWidgetItem, 上一个:QListWidgetItem)
        """
        self.对象.currentItemChanged.connect(回调函数)

    def 绑定事件当前行已更改(self, 回调函数):
        """
        回调函数(当前行:int)
        """
        self.对象.currentRowChanged.connect(回调函数)

    # void	currentTextChanged(const QString &currentText) # 当前选中项目改变时触发
    def 绑定事件当前文本已更改(self, 回调函数):
        """
        回调函数(当前文本:str)
        """
        self.对象.currentTextChanged.connect(回调函数)

    # void	itemActivated(QListWidgetItem *item) # 项目被点击时触发
    def 绑定事件项目被点击(self, 回调函数):
        """
        回调函数(项目:QListWidgetItem)
        """
        self.对象.itemActivated.connect(回调函数)

    # void	itemChanged(QListWidgetItem *item) # 项目改变时触发
    def 绑定事件项目已更改(self, 回调函数):
        """
        回调函数(项目:QListWidgetItem)
        """
        self.对象.itemChanged.connect(回调函数)

    # void	itemClicked(QListWidgetItem *item) # 项目被点击时触发
    def 绑定事件项目被双击(self, 回调函数):
        """
        回调函数(项目:QListWidgetItem)
        """
        self.对象.itemDoubleClicked.connect(回调函数)

    # void	itemEntered(QListWidgetItem *item) # 项目被鼠标进入时触发
    def 绑定事件项目被鼠标进入(self, 回调函数):
        """
        回调函数(项目:QListWidgetItem)
        """
        self.对象.itemEntered.connect(回调函数)

    # void	itemPressed(QListWidgetItem *item) # 项目被鼠标按下时触发
    def 绑定事件项目被鼠标按下(self, 回调函数):
        """
        回调函数(项目:QListWidgetItem)
        """
        self.对象.itemPressed.connect(回调函数)

    # void	itemSelectionChanged() # 选中项目改变时触发
    def 绑定事件选中项目已更改(self, 回调函数):
        self.对象.itemSelectionChanged.connect(回调函数)

    # 获取和设置属性 现行选中项
    @property
    def 现行选中项(self):
        return self.取选中项目索引()

    @现行选中项.setter
    def 现行选中项(self, 索引: int):
        return self.设置选中项目索引(索引)
