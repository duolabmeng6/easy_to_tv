from PySide6.QtWidgets import QMenu, QMenuBar


class 菜单栏(QMenuBar):
    parent = None

    def __init__(self, parent=None, 对象名称=None):
        super().__init__(parent)
        self.parent = parent
        if 对象名称:
            self.setObjectName(对象名称)

    def 添加项目(self, 菜单):
        self.addAction(菜单)

    def 设置位置(self, rect):
        # self.菜单栏.设置位置(QRect(0, 0, 563, 24))  # 设置菜单栏位置和大小
        self.setGeometry(rect)
