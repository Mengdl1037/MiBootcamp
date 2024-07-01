from flask import Flask, request
import torch
from PIL import Image
import io
# import numpy as np


# 创建 flask 实例
app = Flask(__name__)

# 创建一个路由
@app.route('/detect', methods=['POST'])

# 处理 HTTP 请求并返回响应
def detect():
    """接收图像并推理"""
    # TODO：接受并处理多个图像
    # TODO: 异常处理
    # 解析请求参数
    file = request.files['file']
    model_name = request.form.get('model_name')
    img_bytes= file.read()  # file.read()读取的是图片字节流
    img = Image.open(io.BytesIO(img_bytes))  # 通过io.BytesIO将图片字节流转换为图片对象

    # 执行算法逻辑
    ## 加载模型
    model = load_model(model_name)

    ## 进行推理
    result = model(img)
    return result.xyxy[0].cpu().numpy().tolist()  ## TODO: 进一步调整输出结果


def load_model(model_name):
    """加载模型"""
    return torch.hub.load('ultralytics/yolov5', model_name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000)