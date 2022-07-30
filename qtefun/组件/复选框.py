from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-5/qcheckbox.html

class 复选框(组件公共类):
    对象 = None # type: QtWidgets.QCheckBox

    # 获取标题
    @property
    def 标题(self):
        return self.对象.text()

    # 设置标题
    @标题.setter
    def 标题(self, value: str):
        return self.对象.setText(value)

    # 设置选中属性
    @property
    def 选中(self):
        return self.对象.isChecked()

    # 设置选中属性
    @选中.setter
    def 选中(self, value: bool):
        return self.对象.setChecked(value)

    # 绑定事件 复选框点击事件 完成一次鼠标点击就会触发
    def 绑定事件被点击(self, 回调函数):
        self.对象.clicked.connect(回调函数)

    # 绑定事件 复选框选中状态切换 选中 = True 选中的状态改变时就会触发
    def 绑定事件选中状态切换(self, 回调函数):
        """
        回调函数(选中状态: bool)
        """
        self.对象.toggled.connect(回调函数)

    def 绑定事件状态改变(self, 回调函数):
        """
        Qt::Unchecked	0	项目未选中。项目未选中。
        Qt::PartiallyChecked	1	项目已部分检查。如果检查了一些（但不是全部）孩子，可以部分检查分层模型中的项目。
        Qt::Checked	2	项目已选中。

        回调函数(状态)
        """
        self.对象.stateChanged.connect(回调函数)