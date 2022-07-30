from PySide6.QtCore import Signal
from PySide6.QtCore import QObject


class 消息通信(QObject):
    """
    消息通信类

    例如:
        # 主窗口 main.py  定义
        主窗口信号 = 消息通信(str)

        # 接收消息
        self.主窗口信号.接收消息(self.win_login.父窗口消息)
        self.win_login.子窗口信号.接收消息(self.子窗口消息)

        # 定义接收函数
        def 子窗口消息(self, 消息内容):
            print("子窗口消息", 消息内容)

        # 发送消息
        self.主窗口信号.发送消息("发送给子窗口")

        # 子窗口 win_login.py  定义
        子窗口信号 = 消息通信(str)

        # 定义接收函数
        def 父窗口消息(self, 消息内容):
            print("父窗口消息",消息内容)

        # 发送消息
        self.子窗口信号.发送消息("发送给主窗口")


    """
    信号 = Signal(object)

    def __init__(self):
        super(消息通信, self).__init__()

    def 接收消息(self, 函数):
        self.信号.connect(函数)

    def 发送消息(self, param):
        pass
        self.信号.emit(param)
