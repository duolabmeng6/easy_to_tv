import traceback
import datetime

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication
from qtpy.uic import loadUi

def 异常检测(function):
    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__, "函数发生异常")
            print("错误发生时间：", str(datetime.datetime.now()))
            print("错误的详细情况：", traceback.format_exc())

    return box


def 加载ui文件(ui文件名,容器=None):
    return loadUi(ui文件名, 容器)

def 应用退出():
    QCoreApplication.quit()

def 设置关闭窗口不退出():
    QApplication.setQuitOnLastWindowClosed(False)  # 关闭最后一个窗口不退出程序
