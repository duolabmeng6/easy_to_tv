from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类


class 富文本编辑框(组件公共类):
    """
    事件

    copyAvailable(bool) - 当前文本被拷贝到剪贴板时触发
    currentCharFormatChanged(QTextCharFormat) - 当前文本格式发生变化时触发 内容被改变
    cursorPositionChanged () - 当前光标位置发生变化时触发
    redoAvailable(bool) - 当前文本可以重做时触发
    selectionChanged() - 当前文本选择发生变化时触发
    textChanged () - 当前文本发生变化时触发
    undoAvailable(bool) - 当前文本可以撤销时触发

    """
    对象 = None  # type: QtWidgets.QTextEdit

    # 获取标题
    @property
    def 内容(self):
        return self.对象.toPlainText()

    # 设置内容
    @内容.setter
    def 内容(self, value: str):
        print("设置标题", value)
        return self.对象.setText(value)

    def 绑定事件内容被改变(self, 回调函数):
        return self.对象.textChanged.connect(回调函数)

    def 绑定事件文本可复制(self, 回调函数):
        """
        回调函数(是否选择文本:bool)
        """
        # 该信号在文本编辑中选择或取消选择文本时发出。
        # 当选择文本时，将发出该信号，并将yes设置为true。如果未选择任何文本或取消选择所选文本，则发出该信号，并将yes设置为false。
        # 如果yes为true，则可以使用copy（）将所选内容复制到剪贴板。如果yes为false，则copy（）不执行任何操作。
        return self.对象.copyAvailable.connect(回调函数)

    def 绑定事件字符格式更改(self, 回调函数):
        # 如果当前字符格式已更改，例如由于光标位置的更改而导致，则会发出该信号。
        return self.对象.currentCharFormatChanged.connect(回调函数)

    def 绑定事件光标位置被改变(self, 回调函数):
        return self.对象.cursorPositionChanged.connect(回调函数)

    def 绑定事件文本可重做(self, 回调函数):
        # 每当重做操作可用（可用为true）或不可用（可用为false）时，就会发出此信号。
        return self.对象.redoAvailable.connect(回调函数)

    def 绑定事件选择文本(self, 回调函数):
        # 每当选择发生变化时，都会发出此信号。
        return self.对象.selectionChanged.connect(回调函数)

    def 绑定事件文本可撤销(self, 回调函数):
        """
        回调函数(是否可撤销:bool)
        """
        return self.对象.undoAvailable.connect(回调函数)
