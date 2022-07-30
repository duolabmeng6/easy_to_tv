import sys

from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtWidgets import *

from qtefun.组件.容器 import *
from qtefun.组件.表格 import 表格


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("容器组件学习")
        self.show()

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.容器 = 容器(self.widget)
        self.容器.设置背景颜色("#ffffff")

        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 401, 101))
        print(self.widget)
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(160, 20, 99, 20))
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 20, 99, 20))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 130, 371, 80))
        self.radioButton_3 = QRadioButton(self.widget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 20, 99, 20))
        self.radioButton_4 = QRadioButton(self.widget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(200, 20, 99, 20))

        self.setCentralWidget(self.centralwidget)

        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
app = QApplication([])
# 创建窗口 400x400
win = Main()

sys.exit(app.exec())
