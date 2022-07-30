# 用于绑定全局热键
# 需要安装 pynput
# pip install pynput
from pynput import keyboard

热键和函数的映射 = {}


def 注册全局热键(欲绑定的按键, 回调函数):
    """
    注册全局热键
    :param 欲绑定的按键: 按键名称 <ctrl>+1
    :param 回调函数: 回调函数
    :return:
    """
    热键和函数的映射[欲绑定的按键] = 回调函数


def 开启全局热键():
    with keyboard.GlobalHotKeys(热键和函数的映射) as h:
        h.join()


if __name__ == '__main__':
    def 按下Ctrl_1():
        print('ctrl+1 按下')


    def 按下Ctrl_2():
        print('ctrl+2 按下')


    注册全局热键('<ctrl>+1', 按下Ctrl_1)
    注册全局热键('<ctrl>+2', 按下Ctrl_2)
    开启全局热键()
