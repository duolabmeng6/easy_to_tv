from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QColor
from PySide6.QtWidgets import QApplication, QMainWindow


class 主窗口(QMainWindow):

    def 消息框(self, 内容="", 标题="", 类型=1, 按钮: list = None):
        """
        消息框

        :param 内容: 提示的内容
        :param 标题: 窗口的标题
        :param 类型: 1.消息框 2.错误框 3.警告框 4.问题框
        :param 按钮: 按钮的文本 参数 ["确定","取消","是","否","重试","忽略"] 如果为空则为确定按钮

        :return: 返回点击的按钮文本
        """
        if 按钮 is None:
            按钮 = ["确定"]

        按钮列表 = {
            "确定": QtWidgets.QMessageBox.Ok,
            "取消": QtWidgets.QMessageBox.Cancel,
            "是": QtWidgets.QMessageBox.Yes,
            "否": QtWidgets.QMessageBox.No,
            "重试": QtWidgets.QMessageBox.Retry,
            "忽略": QtWidgets.QMessageBox.Ignore,
        }
        # key value 互换
        按钮列表2 = {value: key for key, value in 按钮列表.items()}

        # 检查按钮的参数 循环 按钮列表 组合参数
        按钮参数 = None
        for 按钮文本 in 按钮:
            if 按钮参数 is None:
                按钮参数 = 按钮列表[按钮文本]
            else:
                按钮参数 = 按钮参数 | 按钮列表[按钮文本]

        if 类型 == 1:
            返回结果 = QtWidgets.QMessageBox.information(self, 标题, 内容, buttons=按钮参数)
        elif 类型 == 2:
            返回结果 = QtWidgets.QMessageBox.warning(self, 标题, 内容, buttons=按钮参数)
        elif 类型 == 3:
            返回结果 = QtWidgets.QMessageBox.critical(self, 标题, 内容, buttons=按钮参数)
        elif 类型 == 4:
            返回结果 = QtWidgets.QMessageBox.question(self, 标题, 内容, buttons=按钮参数)
        # print(返回结果)
        # 匹配 按钮列表 和 返回结果
        返回结果 = 按钮列表2[返回结果]
        # print(返回结果)

        return 返回结果

    def 打开文件选择器(self, 文件类型: str = None, 标题="打开文件", 初始目录="."):
        """
        打开文件选择器

        :param 文件类型: 例如:  "所有文件 (*);;文本文件 (*.txt)"
        :param 标题:
        :param 初始目录: 默认当前目录
        :return: 返回选择的文件路径
        """
        if 文件类型 is None:
            文件类型 = "所有文件 (*);;文本文件 (*.txt)"
        文件路径, _ = QtWidgets.QFileDialog.getOpenFileName(self, 标题, 初始目录, 文件类型)
        return 文件路径

    def 打开文件夹选择器(self, 标题="打开文件夹", 初始目录="."):
        """
        打开文件夹选择器

        :param 标题:
        :param 初始目录: 默认当前目录
        :return: 返回选择的文件夹路径
        """
        文件夹路径 = QtWidgets.QFileDialog.getExistingDirectory(self, 标题, 初始目录)
        return 文件夹路径

    def 打开文件保存选择器(self, 文件类型: str = None, 标题="保存文件", 初始目录="."):
        """
        打开文件保存选择器

        :param 文件类型:  例如:  "所有文件 (*);;文本文件 (*.txt)"
        :param 标题:
        :param 初始目录:  默认当前目录
        :return: 返回选择的文件路径
        """
        文件路径 = QtWidgets.QFileDialog.getSaveFileName(self, 标题, 初始目录, 文件类型)
        return 文件路径

    def 打开颜色选择器(self):
        """
        打开颜色选择器

        :return:  返回选择的颜色 例如 PySide6.QtGui.QColor.fromRgbF(0.362097, 0.190341, 0.397406, 1.000000)
        """
        color = QtWidgets.QColorDialog.getColor()
        return color

    def 打开字体选择器(self):
        """
        打开字体选择器

        :return: 返回选择的字体 例如 <PySide6.QtGui.QFont(.AppleSystemUIFont,13,-1,5,400,0,0,0,0,0,0,0,0,0,0,1) at 0x12522d6c0>
        """
        _, font = QtWidgets.QFontDialog.getFont()
        return font

    def 打开输入框(self, 标题="输入", 内容="请输入", 初始值="", 密码=False):
        """
        打开输入框

        :param 标题: 标题
        :param 内容: 内容
        :param 初始值: 默认为空
        :param 密码: 是否是密码框
        :return: 返回输入的值 例如 "123" , True
        """
        if 密码:
            输入结果, 确定 = QtWidgets.QInputDialog.getText(self, 标题, 内容, QtWidgets.QLineEdit.Password, 初始值)
        else:
            输入结果, 确定 = QtWidgets.QInputDialog.getText(self, 标题, 内容, QtWidgets.QLineEdit.Normal, 初始值)

        return 输入结果, 确定

    # 获取窗口标题
    @property
    def 标题(self):
        return self.windowTitle()

    # 设置窗口标题
    @标题.setter
    def 标题(self, value: str):
        return self.setWindowTitle(value)

    # 获取窗口宽度
    @property
    def 宽度(self):
        return self.width()

    # 设置窗口宽度
    @宽度.setter
    def 宽度(self, value: int):
        return self.setMinimumWidth(value)

    # 获取窗口高度
    @property
    def 高度(self):
        return self.height()

    # 设置窗口高度
    @高度.setter
    def 高度(self, value: int):
        return self.setMinimumHeight(value)

    # 获取窗口左边
    @property
    def 左边(self):
        return self.x()

    # 设置窗口左边
    @左边.setter
    def 左边(self, value: int):
        return self.move(value, self.y())

    # 获取窗口上边
    @property
    def 顶边(self):
        return self.y()

    # 设置窗口顶边
    @顶边.setter
    def 顶边(self, value: int):
        return self.move(self.x(), value)

    # 获取窗口右边
    @property
    def 右边(self):
        return self.x() + self.width()

    # 设置窗口右边
    @右边.setter
    def 右边(self, value: int):
        return self.move(value - self.width(), self.y())

    # 获取窗口下边
    @property
    def 下边(self):
        return self.y() + self.height()

    # 设置窗口下边
    @下边.setter
    def 下边(self, value: int):
        return self.move(self.x(), value - self.height())

    # 获取窗口大小
    @property
    def 大小(self):
        return self.size()

    # 设置窗口大小
    @大小.setter
    def 大小(self, value: tuple):
        return self.resize(QSize(value[0], value[1]))

    # 获取窗口位置
    @property
    def 位置(self):
        return self.pos()

    # 设置窗口位置
    @位置.setter
    def 位置(self, value: tuple):
        return self.move(value)

    # 获取窗口是否可见
    @property
    def 可视(self):
        return self.isVisible()

    # 设置窗口是否可见
    @可视.setter
    def 可视(self, value: bool):
        return self.setVisible(value)

    # 获取屏幕宽度
    def 取屏幕宽度(self):
        return self.screen().physicalSize().width()

    # 获取屏幕高度
    def 取屏幕高度(self):
        return self.screen().physicalSize().height()

    # 获取屏幕分辨率
    def 取屏幕分辨率(self):
        return self.screen().physicalSize()

    # 移动
    def 移动(self, x: int, y: int):
        return self.move(x, y)

    # 移动到屏幕中间
    def 移动到屏幕中间(self):

        return self.move(self.取屏幕宽度() / 2 - self.width() / 2, self.取屏幕高度() / 2 - self.height() / 2)

    # 移动到屏幕右下角
    def 移动到屏幕右下角(self):
        return self.move(self.取屏幕宽度() - self.width(), self.取屏幕高度() - self.height())

    # 移动到屏幕左上角
    def 移动到屏幕左上角(self):
        return self.move(0, 0)

    # 移动到屏幕左下角
    def 移动到屏幕左下角(self):
        return self.move(0, self.取屏幕高度() - self.height())

    # 移动到屏幕右上角
    def 移动到屏幕右上角(self):
        return self.move(self.取屏幕宽度() - self.width(), 0)

    # 移动到屏幕中间
    def 移动到屏幕中间(self):
        return self.move(self.取屏幕宽度() / 2 - self.width() / 2, self.取屏幕高度() / 2 - self.height() / 2)

    # 设置背景颜色
    def 设置背景颜色(self, color: QColor):
        return self.setStyleSheet("background-color: %s;" % color.name())

    # 设置背景图片
    def 设置背景图片(self, image: QImage):
        return self.setStyleSheet("background-image: url(%s);" % image.toImage().toBase64().decode())

    def 置鼠标样式(self, 样式: Qt.CursorShape):
        '''
        https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=cursorshape#PySide6.QtCore.PySide6.QtCore.Qt.CursorShape
        '''
        return self.setCursor(样式)

    # 设置提示文本
    def 设置提示文本(self, text: str):
        return self.setToolTip(text)

    def 显示(self):
        self.showNormal()

    def 隐藏(self):
        self.hide()

    def 窗口居中(self):
        #  获取程序所在屏幕是第几个屏幕 获取程序所在屏幕的尺寸 居中窗口
        screen = QApplication.screens()
        screenSize = screen[0].size()
        # self.resize(screenSize.width() * 0.8, screenSize.height() * 0.8)
        self.move((screenSize.width() - self.width()) / 2, (screenSize.height() - self.height()) / 2)

    def 设置菜单栏(self, 菜单栏):
        self.setMenuBar(菜单栏)
