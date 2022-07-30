import os
import socket
import sys
from nanodlna import dlna, devices

import 文件服务类
from pyefun import *


def 获取设备列表():
    设备列表 = []
    my_devices = devices.get_devices(3)
    for i, device in enumerate(my_devices, 1):
        设备列表.append({
            "Model": device["friendly_name"],
            "URL": device["location"],
        })
    return 设备列表


def 取局域网ip(target_ip, target_port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((target_ip, target_port))
    serve_ip = s.getsockname()[0]
    s.close()
    return serve_ip


def 正则取中文数字字母(欲处理文本: str) -> str:
    import re
    正则表达式 = re.compile(r'[^\u4e00-\u9fa5a-zA-Z0-9\.]')
    return 正则表达式.sub('', 欲处理文本)


def 投递视频文件(设备url, 文件路径):
    device = devices.register_device(设备url)
    print("device", device)
    if not device:
        sys.exit("No devices found.")
    target_ip = device["hostname"]
    局域网ip = 取局域网ip(target_ip)
    if 文件路径.startswith("http"):
        # 对文件路径url编码
        播放地址 = 文件路径
    else:
        文件名 = os.path.basename(文件路径)
        # 取扩展名
        扩展名 = os.path.splitext(文件名)[1]
        文件名 = 取短id() + "." + 扩展名

        # 文件名 = 正则取中文数字字母(文件名)
        # 文件名 = 编码_URL编码(文件名)

        文件服务类.写文件名与路径(文件名, 文件路径)
        播放地址 = f"http://{局域网ip}:6161/{文件名}"
    files_urls = {'file_video': 播放地址}
    print("Files URLs: {}".format(files_urls))
    dlna.play(files_urls, device)
    return device, 播放地址


def 暂停播放(device):
    dlna.pause(device)


def 停止播放(device):
    dlna.stop(device)


if __name__ == '__main__':
    pass
    print(获取设备列表())
    # device = 投递视频文件("http://192.168.31.239:57873/description.xml",
    #                       "/Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP01.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4")
    # sleep(5)
    # 停止播放(device)
