from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


class 按钮(组件公共类):
    """
    绑定事件方法
    被点击事件 clicked()
    被按下事件 pressed()
    被松开事件 released()
    选中状态切换事件 toggled()

    """
    对象 = None # type: QtWidgets.QPushButton

    # 获取标题
    @property
    def 标题(self):
        return self.对象.text()

    # 设置标题
    @标题.setter
    def 标题(self, value: str):
        print("设置标题", value)
        return self.对象.setText(value)

    # 绑定事件 按钮点击事件 完成一次鼠标点击就会触发
    def 绑定事件被点击(self, 回调函数):
        self.对象.clicked.connect(回调函数)

    # 绑定事件 鼠标按下事件 一直按住不松开就会触发
    def 绑定事件被按下(self, 回调函数):
        self.对象.pressed.connect(回调函数)

    # 绑定事件 鼠标抬起事件 按住按住后松开就会触发
    def 绑定事件被松开(self, 回调函数):
        self.对象.released.connect(回调函数)

    # 绑定事件 按钮选中状态切换 按钮为可选时事件时触发 可选 = True 选中 = True 选中的状态改变时就会触发
    def 绑定事件选中状态切换(self, 回调函数):
        self.对象.toggled.connect(回调函数)
