from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor, QPixmap, QIcon

from qtefun.组件.组件汉化基类 import 组件汉化基类


class 组件公共类(组件汉化基类):
    """
    配置组件方法和属性
    对象名称

    标题
    宽度
    高度
    顶边
    左边
    右边
    底边
    大小
    位置
    可视
    移动
    背景颜色
    背景图片
    字体颜色
    鼠标样式
    禁用
    可选 配合选中属性使用
    选中
    图标
    图标大小
    提示文本
    状态栏文本
    状态栏图标
    状态栏图标大小
    最大宽度
    最大高度
    最小宽度
    最小高度





    """
    对象 = None # type: QtWidgets.QWidget

    # 获取对象名称
    @property
    def 名称(self):
        return self.对象.getObjectName()

    # 设置对象名称
    @名称.setter
    def 名称(self, value: str):
        return self.对象.setObjectName(value)


    # 获取窗口宽度
    @property
    def 宽度(self):
        return self.对象.width()

    # 设置窗口宽度
    @宽度.setter
    def 宽度(self, value: int):
        return self.对象.setFixedWidth(value)

    # 获取窗口高度
    @property
    def 高度(self):
        return self.对象.height()

    # 设置窗口高度
    @高度.setter
    def 高度(self, value: int):
        return self.对象.setFixedHeight(value)

    # 获取窗口左边
    @property
    def 左边(self):
        return self.对象.x()

    # 设置窗口左边
    @左边.setter
    def 左边(self, value: int):
        return self.对象.move(value, self.对象.y())

    # 获取窗口上边
    @property
    def 顶边(self):
        return self.对象.y()

    # 设置窗口顶边
    @顶边.setter
    def 顶边(self, value: int):
        return self.对象.move(self.对象.x(), value)

    # 获取窗口右边
    @property
    def 右边(self):
        return self.对象.x() + self.对象.width()

    # 设置窗口右边
    @右边.setter
    def 右边(self, value: int):
        return self.对象.move(value - self.对象.width(), self.对象.y())

    # 获取窗口底边
    @property
    def 底边(self):
        return self.对象.y() + self.对象.height()

    # 设置窗口底边
    @底边.setter
    def 底边(self, value: int):
        return self.对象.move(self.对象.x(), value - self.对象.height())

    # 获取窗口大小
    @property
    def 大小(self):
        return self.对象.size()

    # 设置窗口大小
    @大小.setter
    def 大小(self, value: tuple):
        return self.对象.setFixedSize(value)

    # 获取窗口位置
    @property
    def 位置(self):
        return self.对象.pos()

    # 设置窗口位置
    @位置.setter
    def 位置(self, value: tuple):
        return self.对象.move(value)

    # 获取窗口是否可见
    @property
    def 可视(self):
        return self.对象.isVisible()

    # 设置窗口是否可见
    @可视.setter
    def 可视(self, value: bool):
        return self.对象.setVisible(value)

    # 移动
    def 移动(self, x: int, y: int):
        return self.对象.move(x, y)

    # 获取背景颜色
    @property
    def 背景颜色(self):
        return self.对象.palette().color(QPalette.Background)

    # 设置背景颜色
    @背景颜色.setter
    def 背景颜色(self, value: QColor):
        return self.对象.setPalette(QPalette(value))
    # 设置背景图片
    @property
    def 背景图片(self):
        return self.对象.background()

    # 设置背景图片
    @背景图片.setter
    def 背景图片(self, value: QPixmap):
        return self.对象.setBackground(value)

    # 获取字体
    @property
    def 字体(self):
        return self.对象.font()

    # 设置字体
    @字体.setter
    def 字体(self, value: QFont):
        return self.对象.setFont(value)

    # 获取字体大小
    @property
    def 字体大小(self):
        return self.对象.font().pointSize()

    # 设置字体大小
    @字体大小.setter
    def 字体大小(self, value: int):
        return self.对象.setFont(QFont(self.对象.font().family(), value))


    # 获取鼠标样式
    @property
    def 鼠标样式(self):
        return self.对象.cursor()

    @鼠标样式.setter
    def 鼠标样式(self, 样式: Qt.CursorShape):
        '''
        https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=cursorshape#PySide6.QtCore.PySide6.QtCore.Qt.CursorShape
        '''
        return self.对象.setCursor(样式)

    # 获取提示文本
    @property
    def 提示文本(self):
        return self.对象.toolTip()

    # 设置提示文本
    @提示文本.setter
    def 提示文本(self, value: str):
        return self.对象.setToolTip(value)

    # 获取标题
    @property
    def 标题(self):
        return self.对象.windowTitle()

    # 设置标题
    @标题.setter
    def 标题(self, value: str):
        return self.对象.setWindowTitle(value)

    # 获取状态栏文本
    @property
    def 状态栏文本(self):
        return self.对象.statusTip()

    # 设置状态栏文本
    @状态栏文本.setter
    def 状态栏文本(self, value: str):
        return self.对象.setStatusTip(value)

    # 获取状态栏图标
    @property
    def 状态栏图标(self):
        return self.对象.windowIcon()

    # 设置状态栏图标
    @状态栏图标.setter
    def 状态栏图标(self, value: QIcon):
        return self.对象.setWindowIcon(value)

    @property
    def 禁用(self):
        return not self.对象.isEnabled()

    @禁用.setter
    def 禁用(self, value):
        return self.对象.setEnabled(not value)

    # 检查是否可选
    @property
    def 可选(self):
        return self.对象.isCheckable()

    # 设置是否可选
    @可选.setter
    def 可选(self, value: bool):
        return self.对象.setCheckable(value)

    @property
    def 选中(self):
        return self.对象.isChecked()

    @选中.setter
    def 选中(self, value):
        return self.对象.setChecked(value)

    @property
    def 图标(self):
        return self.对象.icon()

    @图标.setter
    def 图标(self, value):
        return self.对象.setIcon(value)

    # 设置图标大小
    @property
    def 图标大小(self):
        return self.对象.iconSize()

    @图标大小.setter
    def 图标大小(self, value):
        return self.对象.setIconSize(value)

    # 获取 最大宽度
    @property
    def 最大宽度(self):
        return self.对象.maximumWidth()

    # 设置 最大宽度
    @最大宽度.setter
    def 最大宽度(self, value):
        return self.对象.setMaximumWidth(value)

    # 获取 最大高度
    @property
    def 最大高度(self):
        return self.对象.maximumHeight()

    # 设置 最大高度
    @最大高度.setter
    def 最大高度(self, value):
        return self.对象.setMaximumHeight(value)

    # 获取 最小宽度
    @property
    def 最小宽度(self):
        return self.对象.minimumWidth()

    # 设置 最小宽度
    @最小宽度.setter
    def 最小宽度(self, value):
        return self.对象.setMinimumWidth(value)

    # 获取 最小高度
    @property
    def 最小高度(self):
        return self.对象.minimumHeight()

    # 设置 最小高度
    @最小高度.setter
    def 最小高度(self, value):
        return self.对象.setMinimumHeight(value)
