from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


class 标签(组件公共类):
    对象 = None # type: QtWidgets.QLabel

    # 获取标题
    @property
    def 标题(self):
        return self.对象.text()

    # 设置标题
    @标题.setter
    def 标题(self, value: str):
        return self.对象.setText(value)

    # 绑定事件 鼠标按下事件 一直按住不松开就会触发
    def 绑定事件被按下(self, 回调函数):
        """
        回调函数(e: QMouseEvent)
        """
        self.对象.mousePressEvent = 回调函数

    # 绑定事件 鼠标抬起事件 按住按住后松开就会触发
    def 绑定事件被松开(self, 回调函数):
        """
        回调函数(e: QMouseEvent)
        """
        self.对象.mouseReleaseEvent = 回调函数

    def 绑定事件点击链接(self, 回调函数):
        """
        当用户单击链接时，会发出此信号。锚点引用的URL在/ink中传递。

        回调函数(链接)
        """
        self.对象.linkActivated.connect(回调函数)
    def 绑定事件鼠标在链接上停留(self, 回调函数):
        """
        当用户悬挂在链接上时，会发出此信号。锚点引用的URL在链接中传递。

        回调函数(链接)
        """
        self.对象.linkHovered.connect(回调函数)