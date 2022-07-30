from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类


class 单行编辑框(组件公共类):
    """
    事件

    cursorPositionChanged(int,int) - 当光标位置发生变化时触发
    editingFinished() - 当编辑结束时触发
    inputRejected() - 当输入被拒绝时触发
    returnPressed () - 当用户按下回车键时触发
    selectionChanged() - 当选择区域发生变化时触发
    textChanged(QString) - 当文本发生变化时触发
    textEdited(QString) - 当文本被编辑时触发

    """
    对象 = None  # type: QtWidgets.QLineEdit

    # 获取标题
    @property
    def 内容(self):
        return self.对象.text()

    # 设置内容
    @内容.setter
    def 内容(self, value: str):
        print("设置标题", value)
        return self.对象.setText(value)

    def 绑定事件内容被改变(self, 回调函数):
        """
        当文本被编辑时触发
        :param 回调函数: 回调函数(文本)
        """
        return self.对象.textChanged.connect(回调函数)

    def 绑定事件编辑完成(self, 回调函数):
        return self.对象.editingFinished.connect(回调函数)

    def 绑定事件输入被拒绝(self, 回调函数):
        return self.对象.inputRejected.connect(回调函数)

    def 绑定事件回车键被按下(self, 回调函数):
        return self.对象.returnPressed.connect(回调函数)

    def 绑定事件选择区域发生变化(self, 回调函数):
        return self.对象.selectionChanged.connect(回调函数)

    def 绑定事件文本被编辑(self, 回调函数):
        """
        当文本被编辑时触发
        :param 回调函数: 回调函数(文本)
        """
        return self.对象.textEdited.connect(回调函数)
