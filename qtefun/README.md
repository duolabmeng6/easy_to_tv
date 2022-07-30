# qtefun qt版易函数

中文函数简单易用~

# 使用方法

## 主窗口 引入 qtefun.部件公共类

该类继承 QtWidgets.QWidget 提供了窗口操作的中文函数

```python
import qtefun


class myApp(qtefun.部件公共类):
```

# 组件中文化

将ui对象包装一下即可实现中文化 不会丢失原有的对象的功能

例如 `self.ui.textEdit.对象.setText("中文") `

这种写法 `对象.` ide会有提示 `对象` 为 `QtWidgets.QPushButton` 的类

也可以改为 `self.ui.textEdit.setText("中文") `

```python
import qtefun
from qtefun.组件.富文本编辑框 import 富文本编辑框
from qtefun.组件.按钮 import 按钮
from qtefun.公共函数 import 异常检测, 加载ui文件


@异常检测
class myApp(qtefun.部件公共类):
    def __init__(self):
        super().__init__()

        self.ui = 加载ui文件("app.ui", self)
        self.ui.show()

        self.标题 = "祖国 您好~"
        self.ui.pushButton = 按钮(self.ui.pushButton)
        self.ui.textEdit = 富文本编辑框(self.ui.textEdit)

        self.ui.pushButton.标题 = "祖国 您好~"
        self.ui.pushButton.宽度 = 148
        self.ui.pushButton.高度 = 48
        self.ui.pushButton.图标 = qtawesome.icon("fa5s.flag", color="red")
        self.ui.pushButton.图标大小 = QtCore.QSize(24, 24)
        self.ui.pushButton.绑定事件_按下(self.按钮被点击)

        self.ui.textEdit.内容 = "祖国 您好~"
        self.ui.textEdit.绑定事件_内容被改变(self.内容被改变)

    def 按钮被点击(self):
        pass
        print("祖国 您好~")

    def 内容被改变(self):
        print("内容被改变", self.ui.textEdit.内容)
```

# 组件对应的英文

| 英文 | 中文       |
| ---- |----------|
| `QtWidgets.QPushButton` | `按钮`     |
| `QtWidgets.QLineEdit` | `单行文本框`  |
| `QtWidgets.QPlainTextEdit` | `纯文本编辑框` |
| `QtWidgets.QTextEdit` | `富文本编辑框` |

# 窗口通讯

引入简化版的 消息通信 类 就可以实现窗口间的通讯


```python
from qtefun.消息通信 import 消息通信
```

## 主窗口 main.py  定义

```python
主窗口信号 = 消息通信(str)
```

### 接收消息

```python
self.主窗口信号.接收消息(self.win_login.父窗口消息)
self.win_login.子窗口信号.接收消息(self.子窗口消息)
```

### 定义接收函数

```python
def 子窗口消息(self, 消息内容):
    print("子窗口消息", 消息内容)
```

### 发送消息

```python
self.主窗口信号.发送消息("发送给子窗口")
```

## 子窗口 win_login.py  定义

```python
子窗口信号 = 消息通信(str)
```

### 定义接收函数

```python
def 父窗口消息(self, 消息内容):
    print("父窗口消息",消息内容)
```

### 发送消息

```python
self.子窗口信号.发送消息("发送给主窗口")
```

## 代码示例

### 父窗口 main.py

```
import sys

import qtawesome
from PySide6 import QtWidgets, QtCore

from PySide6.QtCore import QLocale, QTranslator, Signal
from qtpy.uic import loadUi
import qtefun
import win_login
from qtefun.消息通信 import 消息通信


class MyWidget(qtefun.公共类):
    主窗口信号 = 消息通信()
    用户名 = ""
    密码 = ""
    token=""

    def __init__(self):
        super().__init__()
        # 加载ui
        self.ui = loadUi("app.ui", self)
        # self.ui.show()
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        self.ui.pushButton.setText("祖国 您好~")
        self.ui.textEdit.setText("祖国 您好~")
        self.setWindowTitle("祖国 您好~")

        fa5_icon = qtawesome.icon('fa5s.flag',
                                  color=('red', 100))
        self.ui.pushButton.setIcon(fa5_icon)

        self.win_login = win_login.MyWidget()
        # self.win_login.子窗口信号.connect(self.子窗口消息)  # 子窗口信号绑定主窗口的函数
        # self.主窗口信号.connect(self.win_login.父窗口消息)  # 主窗口信号绑定子窗口的函数

        self.主窗口信号.接收消息(self.win_login.父窗口消息)
        self.win_login.子窗口信号.接收消息(self.子窗口消息)

        self.测试代码()

    def closeEvent(self, event):
        # 关闭窗口时，关闭子窗口
        sys.exit(0)

    def 子窗口消息(self, 消息内容):
        print("子窗口消息", 消息内容)
        if 消息内容['消息类型'] == "登录成功":
            self.用户名 = 消息内容['用户名']
            self.密码 = 消息内容['密码']
            self.token = 消息内容['密码']
            self.ui.show()

        print("账户密码 {} {}".format(self.用户名,self.密码))
        print("消息内容.消息类型 {}".format(消息内容['消息类型']))
        self.setWindowTitle("欢迎回来，{}".format(self.用户名))


    def 测试代码(self):
        pass
        self.win_login.show()
        self.主窗口信号.发送消息("发送给子窗口")

        # 返回结果 = self.打开文件选择器()
        # print(返回结果)
        # 返回结果 = self.打开文件夹选择器()
        # print(返回结果)
        # 返回结果 = self.打开颜色选择器()
        # print(返回结果)
        # 返回结果 = self.打开字体选择器()
        # print(返回结果)
        # 返回结果 = self.打开输入框("请输入内容","请输入内容")
        # print(返回结果)

    @QtCore.Slot()
    def on_pushButton_login_clicked(self):
        pass
        print("祖国 您好~")

    @QtCore.Slot()
    def on_pushButton_clicked(self):
        pass
        self.测试代码()

        # self.消息框("信息框","标题", 1, ["确定"])
        # self.消息框("错误框","标题", 2, ["确定"])
        # self.消息框("警告框","标题", 3, ["确定"])
        # self.消息框("问题框","标题", 4, ["确定"])
        # 返回结果 = self.消息框("信息框", "标题", 1, ["确定", "取消", "是", "否", "重试", "忽略"])
        # print(返回结果)
        # self.消息框(F"你点击了{返回结果}")

        # info = self.ui.textEdit.toPlainText()
        # print(info)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication([])

    # 设置系统语言为中文
    qLocale = QLocale(QLocale.Chinese, QLocale.SimplifiedChineseScript)
    trans = QTranslator()
    trans.load("qt_zh_CN")
    app.installTranslator(trans)

    widget = MyWidget()
    # widget.show()
    sys.exit(app.exec())

```



### 子窗口 win_login.py

```
import sys
from PySide6 import QtWidgets, QtCore

from PySide6.QtCore import QLocale, QTranslator, Signal
from PySide6.QtWidgets import QDialog
from qtpy.uic import loadUi
import qtefun

from qtefun.消息通信 import 消息通信


class MyWidget(QDialog,qtefun.公共类):
    子窗口信号 = 消息通信()
    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        # 加载ui
        self.ui = loadUi("ui_login.ui", self)
        self.ui.show()

    def closeEvent(self, event):
        self.ui.lineEdit_user.setText("")
        self.ui.lineEdit_pass.setText("")

    def 父窗口消息(self, 消息内容):
        print("父窗口消息",消息内容)

    @QtCore.Slot()
    def on_pushButton_login_clicked(self):
        pass
        用户名 = self.ui.lineEdit_user.text()
        密码 = self.ui.lineEdit_pass.text()
        print(用户名, 密码)
        if 用户名 == "admin" and 密码 == "admin":
            self.子窗口信号.发送消息({
                "消息类型": "登录成功",
                "用户名": 用户名,
                "密码": 密码,
                "token": "token"
            })
            self.消息框("登录成功", "提示", 1, ["确定"])
            self.close()

        else:
            self.子窗口信号.发送消息({
                "消息类型": "登录失败",
            })
            self.消息框("登录失败", "提示", 2, ["确定"])


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    # widget.show()
    sys.exit(app.exec())


```

