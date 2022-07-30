import os
import socket
import sys
from nanodlna import dlna, devices

import 文件服务类


def 获取设备列表():
    设备列表 = []
    my_devices = devices.get_devices(2)
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


def 投递视频文件(设备url, 文件路径):
    device = devices.register_device(设备url)
    print("device", device)
    if not device:
        sys.exit("No devices found.")
    target_ip = device["hostname"]
    文件名 = os.path.basename(文件路径)
    文件服务类.写文件名与路径(文件名, 文件路径)
    files_urls = {'file_video': f"http://{target_ip}:6161/{文件名}"}
    print("Files URLs: {}".format(files_urls))
    dlna.play(files_urls, device)
    return device


def 暂停播放(device):
    dlna.pause(device)


def 停止播放(device):
    dlna.stop(device)


if __name__ == '__main__':
    pass
    # print(获取设备列表())
    # device = 投递视频文件("http://192.168.31.239:57873/description.xml",
    #                       "/Users/chensuilong/Documents/lzxd/廉政行动2022.2022.EP01.HD1080P.X264.AAC.Cantonese.CHS.BDYS.mp4")
    # sleep(5)
    # 停止播放(device)