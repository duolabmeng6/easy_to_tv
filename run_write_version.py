# -*- coding: utf-8 -*-
import os

def 查看系统所有环境变量():
    from icecream import ic
    # 打印系统所有的环境变量
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)
# 查看系统所有环境变量()
version = os.environ.get('version')
print("version:", version)
# 获取运行目录
# print("run dir:", os.getcwd())
# 获取文件目录
文件目录 = os.path.dirname(__file__)
print("file dir:", os.path.dirname(__file__))
versionFilePath = os.path.join(文件目录, "version.py")
print("edit file {versionFilePath} output: version = {version}")
# 覆盖写出文件 version.py 中
with open(versionFilePath, 'w') as f:
    f.write(f'version = "{version}"')

exit()
