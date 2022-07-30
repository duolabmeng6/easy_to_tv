from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView, QLineEdit, QComboBox, QPushButton, QCheckBox, QWidget

from qtefun.组件.组件汉化基类 import 组件汉化基类


class 容器(组件汉化基类):
    对象 = None  # type: # QWidget

    def 设置边框颜色(self, 颜色):
        self.对象.setStyleSheet("QWidget{border:1px solid %s}" % 颜色)

    def 设置边框宽度(self, 宽度):
        self.对象.setStyleSheet("QWidget{border:%spx solid black}" % 宽度)

    def 设置边框(self, 宽度, 颜色):
        self.对象.setStyleSheet("QWidget{border:%spx solid %s}" % (宽度, 颜色))

    def 设置背景颜色(self, 颜色):
        self.对象.setStyleSheet("QWidget{background-color:%s}" % 颜色)

    def 设置背景图片(self, 图片):
        self.对象.setStyleSheet("QWidget{background-image:url(%s)}" % 图片)

    def 设置背景图片填充(self, 图片):
        self.对象.setStyleSheet(
            "QWidget{background-image:url(%s);background-repeat:no-repeat;background-position:center;background-size:contain}" % 图片)

    def 设置背景图片平铺(self, 图片):
        self.对象.setStyleSheet(
            "QWidget{background-image:url(%s);background-repeat:repeat;background-position:center;background-size:contain}" % 图片)
