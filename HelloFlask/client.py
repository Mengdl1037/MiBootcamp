import requests

def send_img(image_path, model_name):
    """发送图片到服务器并获取响应"""

    # 配置服务器url
    url = 'http://127.0.0.1:5000/detect'

    # 配置请求参数
    file = {'file': open(image_path, 'rb')}
    data = {'model_name': model_name}

    # 发送请求
    response = requests.post(url, files=file, data=data)
    return response

if __name__ == '__main__':
    response = send_img('.\\database\\tiger.jpg', 'yolov5s')
    print(response.text)  