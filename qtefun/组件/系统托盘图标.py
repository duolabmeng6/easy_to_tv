from PySide6.QtWidgets import QSystemTrayIcon


class 系统托盘图标(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)

    def 设置托盘菜单(self, 菜单):
        self.setContextMenu(菜单)

    def 设置托盘图标(self, icon):
        self.setIcon(icon)

    def 设置提示文本(self, 提示文本):
        self.setToolTip(提示文本)

    def 显示(self):
        self.show()
        
    def 隐藏(self):
        self.hide()