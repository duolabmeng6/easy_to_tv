import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMenu, QMenuBar, QToolBar, QToolButton
import pyefun as efun

from qtefun.组件.组件公共类 import 组件公共类


class 工具条(组件公共类):
    parent = None
    对象 = None  # type: QToolButton
    菜单项列表={}
    资源文件绝对路径 = ""
    def 添加分隔条(self):
        self.addSeparator()

    def 添加项目(self, 名字, 图标, 帮助文本, 图标宽度=32, 图标高度=32, 回调函数=None):
        菜单项 = QAction(名字, self.parent)
        if 图标:
            菜单项.setIcon(图标)
        # if 快捷键:
        #     菜单项.setShortcut(快捷键)
        菜单项.setToolTip(帮助文本)
        if 回调函数:
            菜单项.triggered.connect(回调函数)
        self.菜单项列表[名字] = 菜单项
        self.addAction(菜单项)

    def 从工具条数据中创建(self, 工具条数据, 图标宽度=32, 图标高度=32, 回调函数=None):
        toolJson = json.loads(工具条数据)
        for 第一层的值 in toolJson:
            # id = 第一层的值.get("id")
            名称 = 第一层的值.get("名称")
            图标 = 第一层的值.get("图标")
            帮助文本 = 第一层的值.get("帮助文本")
            if 名称 == "-":
                self.添加分隔条()
                continue

            if 帮助文本 is None:
                帮助文本 = 名称

            if 图标 is not None:
                图标 = efun.子文本替换(图标, "./", self.资源文件绝对路径 + "/")
                图标 = efun.路径优化(图标)
                if efun.文件是否存在(图标):
                    image = QIcon(图标)
                    self.添加项目(名称, image, 帮助文本, 图标宽度, 图标高度, 回调函数)
                else:
                    print("工具条图标文件不存在无法创建[{}]文件路径[{}]".format(名称, 图标, ))
