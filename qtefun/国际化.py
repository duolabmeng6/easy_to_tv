from PySide6.QtCore import Signal, QLocale, QTranslator
from PySide6.QtCore import QObject

def 设置语言为中文():
    # 设置系统语言为中文
    # qt_zh_CN.qm 需要翻译文件
    # 使用方法     app.installTranslator(设置语言为中文())
    qLocale = QLocale(QLocale.Chinese, QLocale.SimplifiedChineseScript)
    trans = QTranslator()
    trans.load("qt_zh_CN")
    return trans
