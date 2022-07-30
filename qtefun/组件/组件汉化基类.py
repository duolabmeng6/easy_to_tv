"""
组件汉化基类

使得原有对象可以轻松的汉化

由于猴子补丁的模式,导致ide没有中文命令提示,所以采用该方式

封装组件时继承该类即可
"""
from PySide6.QtWidgets import  QWidget


class 组件汉化基类(object):
    对象 = QWidget

    def __init__(self, 对象):
        self.对象 = 对象

    def __getattr__(self, 方法名):
        # 将调用不存在的方法转移到对象中 兼容原来的写法
        def 检查方法是否存在(*args, **kwargs):
            # 调用对象中的方法
            if 方法名 in dir(self.对象):
                return getattr(self.对象, 方法名)(*args, **kwargs)
            # print(f'调用方法不存在 方法名：{方法名} 参数为：{args}, {kwargs}')
            raise Exception(f'调用方法不存在 方法名：{方法名} 参数为：{args}, {kwargs}')

        if 方法名 in dir(self):
            return getattr(self, 方法名)
        return 检查方法是否存在
