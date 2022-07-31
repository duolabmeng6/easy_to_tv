from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qtefun.组件.按钮 import 按钮
from qtefun.组件.标签 import 标签
from qtefun.组件.组合框 import 组合框
from qtefun.组件.单行编辑框 import 单行编辑框
from qtefun.组件.复选框 import 复选框
from qtefun.图标 import *
from pyefun.调试.调试输出 import *
import 投屏模块
import go2tv模块

import ui_多多投屏
import 文件服务器

import qtAutoUpdateApp.自动更新模块 as 自动更新模块
import version
from pyefun import *

全局变量_版本号 = version.version
全局_项目名称 = "duolabmeng6/easy_to_tv"
全局_应用名称 = "easy_to_tv.app"
全局_当前版本 = version.version
全局_官方网址 = "https://github.com/duolabmeng6/easy_to_tv"


class 文件服务器线程(QThread):
    def __init__(self):
        super(文件服务器线程, self).__init__()
        self.started.connect(self.ui_开始)
        self.finished.connect(self.ui_结束)

    def run(self):
        pass
        # 文w件服务器.app.run(host='0.0.0.0', port=6161, threaded=True, use_reloader=False, debug=False)
        kwargs = {'host': '0.0.0.0', 'port': 6161, 'threaded': True, 'use_reloader': False, 'debug': False}
        threading.Thread(target=文件服务器.app.run, daemon=True, kwargs=kwargs).start()

    def ui_开始(self):
        pass

    def ui_结束(self):
        pass


class 刷新设备线程(QThread):
    def __init__(self, 回调函数):
        super(刷新设备线程, self).__init__()
        self.started.connect(self.ui_开始)
        self.finished.connect(self.ui_结束)
        self.回调函数 = 回调函数
        self.数据 = None

    def run(self):
        pass
        print("刷新设备线程开始")
        # self.数据 = 投屏模块.获取设备列表()
        self.数据 = go2tv模块.获取设备列表()

    def ui_开始(self):
        pass

    def ui_结束(self):
        pass
        self.回调函数(self.数据)


class 投屏线程(QThread):
    def __init__(self, 当前选中设备URL, 文件路径, 回调函数):
        super(投屏线程, self).__init__()
        self.started.connect(self.ui_开始)
        self.finished.connect(self.ui_结束)
        self.当前选中设备URL = 当前选中设备URL
        self.文件路径 = 文件路径
        self.回调函数 = 回调函数
        self.播放设备 = None
        self.播放地址 = None

    def run(self):
        pass
        self.播放设备, self.播放地址 = 投屏模块.投递视频文件(self.当前选中设备URL, self.文件路径)

    def ui_开始(self):
        pass

    def ui_结束(self):
        pass
        self.回调函数(self.播放设备, self.播放地址)


class MainWin(QMainWindow):
    播放设备 = None
    检查更新窗口 = None

    def __init__(self):
        super().__init__()
        self.当前选中设备URL = None
        self.ui = ui_多多投屏.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # 设置窗口图标
        self.setWindowIcon(QIcon(go2tv模块.全局变量_资源文件目录 + "/app.png"))

        # 禁止最大化 伸缩大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("多多投屏 " + version.version)
        # 状态条插入标签
        self.label_zhuangtaitiao = QLabel(self)
        # 点击事件
        self.标签状态条 = 标签(self.label_zhuangtaitiao)
        self.标签状态条.绑定事件被按下(self.标签状态条被点击)
        self.statusBar().addWidget(self.label_zhuangtaitiao)

        self.注册托盘图标()

        self.按钮刷新 = 按钮(self.ui.pushButton_shuaxin)
        self.按钮刷新.绑定事件被点击(self.按钮刷新被点击)
        self.按钮选择文件 = 按钮(self.ui.pushButton_xuanzewenjjian)
        self.按钮选择文件.绑定事件被点击(self.按钮选择文件被点击)
        self.按钮开始播放 = 按钮(self.ui.pushButton_kaishibofang)
        self.按钮开始播放.绑定事件被点击(self.按钮开始播放被点击)
        self.按钮停止播放 = 按钮(self.ui.pushButton_tingzhibofang)
        self.按钮停止播放.绑定事件被点击(self.按钮停止播放被点击)
        self.组合框设备列表 = 组合框(self.ui.comboBox_shebeiliebiao)
        self.组合框设备列表.绑定事件项目被选择(self.组合框项目被选择)
        self.编辑框路径 = 单行编辑框(self.ui.lineEdit_lujing)
        self.按钮检查更新 = 按钮(self.ui.pushButton_jianchagengxin)
        self.按钮检查更新.绑定事件被点击(self.按钮检查更新被点击)
        self.选择框自动播放 = 复选框(self.ui.checkBox)
        self.选择框自动播放.选中 = True
        self.播放设备 = None
        self.检查更新窗口 = None

        #
        self.刷新设备 = 刷新设备线程(self.刷新设备线程回调函数)
        self.按钮刷新被点击()

        self.文件服务器 = 文件服务器线程()
        self.文件服务器.start()

        # self.编辑框路径.内容 = "/Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP05.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4"
        # 注册文件拖放 绑定事件
        self.ui.centralwidget.setAcceptDrops(True)
        self.ui.centralwidget.dragEnterEvent = self.拖放事件
        # 拖放结束事件
        self.ui.centralwidget.dropEvent = self.拖放结束事件

    def 按钮检查更新被点击(self):
        if self.检查更新窗口 is None:
            self.检查更新窗口 = 自动更新模块.窗口_更新软件(Github项目名称=全局_项目名称,
                                         应用名称=全局_应用名称,
                                         当前版本号=全局_当前版本,
                                         官方网址=全局_官方网址)
        self.检查更新窗口.show()

    def 注册托盘图标(self):
        self.托盘图标 = QSystemTrayIcon(self)
        icon = QIcon()
        icon.addFile(u"app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.托盘图标.setIcon(icon)
        self.托盘图标.setToolTip("多多投屏 点击隐藏或显示")
        self.托盘图标.activated.connect(self.托盘图标被点击)
        self.托盘图标.show()

    def 托盘图标被点击(self, reason):
        # 图标位置 = self.托盘图标.geometry()
        # self.move(图标位置.x(), 图标位置.y())
        # 点击显示或隐藏窗口
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def 拖放结束事件(self, event):
        # 发送点击消息

        if self.选择框自动播放.选中:
            self.按钮开始播放.对象.click()

    def 拖放事件(self, event):
        if event.mimeData().hasUrls():
            print("拖放事件")
            # 获取拖放文件的路径
            文件路径 = event.mimeData().text()
            # 替换文本  file:///
            if 系统_是否为window系统():
                文件路径 = 文件路径.replace("file:///", "")
            else:
                文件路径 = 文件路径.replace("file://", "")

            self.编辑框路径.内容 = 文件路径

            event.accept()
        else:
            event.ignore()

    def 刷新设备线程回调函数(self, 设备列表):
        self.按钮刷新.禁用 = False
        self.按钮刷新.标题 = "刷新"

        self.设备列表 = 设备列表
        self.组合框设备列表.清空()
        for x in 设备列表:
            self.当前选中设备URL = self.设备列表[0]['URL']
            Model, URL = x['Model'], x['URL']
            ic(Model, URL)
            self.组合框设备列表.添加项目(Model)

    def 按钮刷新被点击(self):
        self.按钮刷新.禁用 = True
        self.按钮刷新.标题 = "刷新中..."
        self.刷新设备.start()

    def 按钮选择文件被点击(self):
        print("按钮选择文件被点击")
        文件名 = QFileDialog.getOpenFileName(self, "选择文件", "./", "All Files (*)")
        if 文件名[0]:
            self.编辑框路径.内容 = 文件名[0]

    def 标签状态条被点击(self, e):
        # 设置剪切板文本
        QApplication.clipboard().setText(self.标签状态条.标题)
        # 提示用户
        QMessageBox.information(self, "提示", "已复制到剪切板")

    def 投屏回调函数(self, 播放设备, 播放地址):
        self.播放设备 = 播放设备
        self.播放地址 = 播放地址
        self.标签状态条.标题 = 播放地址

    def 按钮开始播放被点击(self):
        print("按钮开始播放被点击")
        if self.当前选中设备URL == None:
            QMessageBox.warning(self, "提示", "请选择设备")
            return
        self.投屏 = 投屏线程(self.当前选中设备URL, self.编辑框路径.内容, self.投屏回调函数)
        self.投屏.start()

    def 按钮停止播放被点击(self):
        print("按钮停止播放被点击")
        投屏模块.停止播放(self.播放设备)

    def 组合框项目被选择(self, 索引):
        print("组合框项目被选择", 索引)
        self.当前选中设备 = self.设备列表[索引]
        ic(self.当前选中设备)
        self.当前选中设备URL = self.设备列表[索引]['URL']
        ic(self.当前选中设备URL)

    def closeEvent(self, event: QCloseEvent) -> None:
        print("closeEvent")

        if self.播放设备:
            投屏模块.停止播放(self.播放设备)
        event.accept()


if __name__ == '__main__':
    自动更新模块.初始化()

    app = QApplication()
    window = MainWin()

    sys.exit(app.exec())
