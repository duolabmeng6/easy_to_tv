# 定义一个键值对储存文件与路径的关系

文件与路径 = {}


def 写文件名与路径(文件名, 路径):
    文件与路径.update({文件名: 路径})


def 取路径(文件名):
    return 文件与路径.get(文件名)

def 清空():
    文件与路径.clear()


if __name__ == '__main__':
    pass
    写文件名与路径("aaa", "/aaaaa/bbbb.mp4")
    print(取路径("aaa"))
