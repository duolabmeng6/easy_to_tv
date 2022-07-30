from flask import Flask, send_file

import 文件服务类

app = Flask(__name__)



@app.route('/<path:url_path>')
def mp4(url_path):
    print("url_path", url_path)
    path = 文件服务类.取路径(url_path)
    # 检查path的文件是否存在
    if not path:
        return "文件不存在"
    print("path", path)

    return send_file(path, as_attachment=False)


if __name__ == '__main__':
    print("123")
    文件服务类.写文件名与路径(r"1.mp4",r"C:\Users\csuil\Desktop\华为手机视频\VID_20201213_102126.mp4")
    app.run(host='0.0.0.0', port=6161, threaded=True,debug=True)
