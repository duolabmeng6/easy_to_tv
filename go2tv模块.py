from 公用函数 import *
from pyefun import *
from pyefun.模块.终端类 import *

import re

if 是否为PyInstaller编译后环境():
    全局变量_资源文件目录 = 取资源文件路径()
else:
    全局变量_资源文件目录 = os.path.dirname(os.path.abspath(__file__))


def 获取设备列表():
    #     内容 = """
    # Device 1
    # --------
    # Model: Macast(chensuiongdeMBP)
    # URL:   http://192.168.31.239:57873/description.xml
    #
    # Device 2
    # --------
    # Model: 小爱音箱-3224
    # URL:   http://192.168.31.52:9999/bab5411b-9c23-4c6a-827d-4b463943da0b.xml
    # """
    if 系统_是否为window系统():
        命令 = f"{全局变量_资源文件目录}/go2tv/go2tv.exe -l"
        print(命令)
        # 内容 = 运行(命令)
        终端 = 终端类()
        终端.运行(命令)
        内容 = 终端.取返回结果()
        
    if 系统_是否为mac系统():
        命令 = f"{全局变量_资源文件目录}/go2tv/go2tv -l"
        print(命令)
        内容 = 运行(命令)


    # 正则获取内容中的 Model URL
    正则 = re.compile(r'Model: (.*?)\nURL: (.*?)\n')
    设备列表 = 正则.findall(内容)
    # 删除
    设备列表 = [{'Model': x[0], 'URL': x[1]} for x in 设备列表]
    # 删除空白字符
    设备列表 = [{'Model': x['Model'].strip(), 'URL': x['URL'].strip()} for x in 设备列表]
    return 设备列表


def 投递视频文件(设备url, 文件路径):
    # ./go2tv -v /Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP01.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4 -t http://192.168.31.10:25826/description.xml
    命令 = 取运行目录() + f"/go2tv -v {文件路径} -t {设备url}"
    运行(命令)
    # 终端 = 终端类()
    # 终端.运行(命令)
    # print(命令)
    # from applescript import tell
    # tell.app('Terminal', 'do script "' + 命令 + '"')


def 工作线程():
    设备URL = "http://192.168.31.239:57873/description.xml"
    播放文件路径 = "/Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP01.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4"
    投递视频文件(设备URL, 播放文件路径)


def 结束http服务器():
    运行("killall go2tv")


if __name__ == "__main__":
    pass
    设备列表 = 获取设备列表()
    for x in 设备列表:
        Model, URL = x['Model'], x['URL']
        ic(Model, URL)

    # 设备URL = "http://192.168.31.239:57873/description.xml"
    # 播放文件路径 = "/Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP01.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4"
    # 投递视频文件(设备URL, 播放文件路径)
    # 线程 = 启动线程(工作线程, 跟随主线程结束=True)
