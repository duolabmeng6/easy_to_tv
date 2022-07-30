from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView, QLineEdit, QComboBox, QPushButton, QCheckBox

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qtreewidget.html
# 表格
# 绑定事件
class 表格节点类(QTableWidgetItem):

    def 置标题(self, 第几列, 标题):
        self.setText(第几列, 标题)

    def 置标题多列(self, 标题列表, 从第几列开始=0):
        i = 从第几列开始
        for 标题 in 标题列表:
            self.setText(i, 标题)
            i = i + 1


class 表格(组件公共类):
    对象 = None  # type: QtWidgets.QTableWidget

    # 设置列数
    def 设置列数(self, 列数):
        self.对象.setColumnCount(列数)

    # 设置行数
    def 设置行数(self, 行数):
        self.对象.setRowCount(行数)

    # 设置表头
    def 设置表头(self, 表头=[]):
        self.对象.setHorizontalHeaderLabels(表头)

    # 设置整行选择
    def 设置整行选择(self):
        self.对象.setSelectionBehavior(QAbstractItemView.SelectRows)

    # 设置单一选择
    def 设置单一选择(self):
        self.对象.setSelectionMode(QAbstractItemView.SingleSelection)

    # 设置不可编辑
    def 设置不可编辑(self):
        self.对象.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def 插入行(self, 行号):
        self.对象.insertRow(行号)

    def 插入列(self, 列号):
        self.对象.insertColumn(列号)

    def 设置项目文本(self, 行号, 列号, 文本):
        self.对象.setItem(行号, 列号, 表格节点类(文本))

    def 设置单元格组件(self, 行号, 列号, 组件):
        self.对象.setCellWidget(行号, 列号, 组件)

    def 设置单元格文本框(self, 行号, 列号, 初始文本: str, 回调函数):
        inputText = QLineEdit()
        inputText.setText(初始文本)

        def 完成编辑():
            回调函数(行号, 列号, inputText.text())

        inputText.editingFinished.connect(完成编辑)
        self.设置单元格组件(行号, 列号, inputText)

    def 设置单元格复选框(self, 行号, 列号, 初始状态: bool, 初始文本: str, 回调函数):
        checkBox = QtWidgets.QCheckBox()
        checkBox.setText(初始文本)
        checkBox.setChecked(初始状态)

        # 绑定选择事件
        def 选择事件():
            回调函数(行号, 列号, checkBox.isChecked())

        checkBox.stateChanged.connect(选择事件)
        self.设置单元格组件(行号, 列号, checkBox)

    def 设置单元格组合框(self, 行号, 列号, 项目列表: list, 默认选择索引, 回调函数):
        if 默认选择索引 is None:
            默认选择索引 = 0

        comboBox = QComboBox()
        for item in 项目列表:
            comboBox.addItem(item)

        def 选择项目():
            回调函数(行号, 列号, comboBox.currentText())

        comboBox.setCurrentIndex(默认选择索引)
        comboBox.activated.connect(选择项目)
        self.设置单元格组件(行号, 列号, comboBox)

    # 设置单元格按钮
    def 设置单元格按钮(self, 行号, 列号, 文本, 回调函数):
        button = QPushButton(self.对象)
        button.setText(文本)

        def 被点击():
            回调函数(行号, 列号)

        button.clicked.connect(被点击)
        self.设置单元格组件(行号, 列号, button)

    def 取行数(self):
        return self.对象.rowCount()

    def 取列数(self):
        return self.对象.columnCount()

    def 导出数据(self):
        整体数据 = []
        for x in range(self.取行数()):
            组合数据 = []
            for y in range(self.取列数()):
                obj = self.对象.cellWidget(x, y)
                if obj is None:
                    数据 = self.对象.item(x, y).text()
                else:
                    数据 = None
                    if isinstance(obj, QLineEdit):
                        数据 = obj.text()
                    elif isinstance(obj, QCheckBox):
                        数据 = obj.isChecked()
                    elif isinstance(obj, QComboBox):
                        数据 = obj.currentText()
                组合数据.append(数据)
            整体数据.append(组合数据)
        return 整体数据
