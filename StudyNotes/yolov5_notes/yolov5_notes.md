# Hello yolov5

## 安装

```安装 yolov5 repo
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

## 源码结构目录

```
yolov5/
├── data/                  # 数据集配置目录
│   ├── coco.yaml            # COCO数据集配置文件，里面有数据集的下载地址和加载的python脚本
│   ├──ImageNet.yaml           # ImageNet数据集
│   ├── custom.yaml          # 自定义数据集配置文件
│   └── ...                  # 其他数据集配置文件
├── models/                # 模型定义目录
│   ├── common.py            # 通用函数和类定义
│   ├── experimental.py      # 实验性模型定义
│   ├── export.py            # 导出模型为ONNX的脚本
│   ├── models.py            # YOLOv5模型定义
│   ├── yolo.py              # YOLO类定义
│   └── ...                  # 其他模型定义文件
├── utils/                 # 实用工具目录
│   ├── autoanchor.py        # 自动锚框生成工具
│   ├── datasets.py          # 数据集处理工具
│   ├── general.py           # 通用实用函数
│   ├── google_utils.py      # Google云平台工具
│   ├── loss.py              # 损失函数定义
│   ├── metrics.py           # 评估指标定义
│   ├── torch_utils.py       # PyTorch工具
│   ├── wandb_logging.py     # WandB日志记录工具
│   └── ...                  # 其他实用工具文件
├── runs/                 # 训练和预测的结果输出目录
│   ├── detect        # 使用detect.py训练后输出目录，输出的目录是[ex自增数字]
│   ├── train        # 使用detect.py训练后输出目录，输出的目录是[ex自增数字],包含了训练好的模型和测试集效果
├── weights/               # 预训练模型权重目录
├── .gitignore             # Git忽略文件配置
├── Dockerfile             # Docker容器构建文件
├── LICENSE                # 许可证文件
├── README.md              # 项目说明文档
├── requirements.txt       # 项目依赖包列表
├── train.py               # 训练脚本
├── detect.py               # 预测脚本
├── export.py               # 导出YOLOv5 PyTorch model to 其他格式
├── hubconf.py               # hubconf.py文件是用于定义模型和数据集的Python模块
└── ...                    # 其他源代码文件
```

## 推理

1. 使用 YOLOv5 PyTorch Hub 推理。最新 模型 将自动的从 YOLOv5 release 中下载。

    ```使用 YOLOv5 PyTorch Hub 推理
    import torch

    # Model
    model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom
    # model = torch.hub.load("ultralytics/yolov5", "yolov5m")  # or yolov5n - yolov5x6, custom
    # model = torch.hub.load("ultralytics/yolov5", "yolov5l")  # or yolov5n - yolov5x6, custom
    # model = torch.hub.load("ultralytics/yolov5", "yolov5n")  # or yolov5n - yolov5x6, custom
    # model = torch.hub.load("ultralytics/yolov5", "yolov5x")  # or yolov5n - yolov5x6, custom
    # model = torch.hub.load("ultralytics/yolov5", "yolov5x6")  # or yolov5n - yolov5x6, custom


    # Images
    img = "https://ultralytics.com/images/zidane.jpg"  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
    ```

2. 使用 detect.py 推理
detect.py 在各种来源上运行推理， 模型 自动从 最新的YOLOv5 release 中下载，并将结果保存到 runs/detect 。

    ```使用 detect.py 推理
    python detect.py --weights yolov5s.pt --source 0                               # webcam
                                                   img.jpg                         # image
                                                   vid.mp4                         # video
                                                   screen                          # screenshot
                                                   path/                           # directory
                                                   list.txt                        # list of images
                                                   list.streams                    # list of streams
                                                   'path/*.jpg'                    # glob
                                                   'https://youtu.be/LNwODJXcvt4'  # YouTube
                                                   'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
    ```

## .pt 文件

.pt 文件是模型文件。

## .yaml 文件

在 models 目录下可以看到有许多 .yaml 文件。以 yolov5s.yaml 为例，它是 YOLOv5s 模型的配置文件，其中包含了模型的结构、超参数、训练和推理相关的设置等信息。该文件可以用来训练和推理 YOLOv5 模型。主要内容如下：

- nc：需要检测的类别数。
- depth_multiple：控制网络深度的因子，通常取值为 0.33、0.67、1.0、1.33 等。
- width_multiple：控制网络宽度的因子，通常取值为 0.25、0.33、0.5、0.67、0.75、1.0 等。
- anchors：定义预设的锚框，用于检测目标的大小和比例。anchors 中包含的是 k-means 算法聚类得到的 9 个默认锚框的大小和比例。
- backbone：主干网络的配置，包括网络的类型、输出通道数、层数等。
- head：检测头的配置，包括卷积层的大小、激活函数、BN 层等。
- yolo：YOLO 检测器的配置，包括预测框的数量、锚框的尺寸和比例等。
  
在 yolov5s.yaml 中，还包含了许多其它的配置参数，例如优化器的超参数、学习率的策略、训练过程中的数据增强等。这些参数可以通过修改 yolov5s.yaml 来优化模型的性能，从而更好地适应不同的检测任务和数据集。

```[-1, 9, C3, [512]]```表示卷积层参数，其中

- -1 表示使用上一层的输出特征图作为输入。
- 9 表示该层的输出通道数。
- C3 表示该层所在的模块名称为 C3，C3 是 YOLOv5 的主干网络骨干部分之一，具体的结构可以参考 YOLOv5 的论文。
- [512] 表示该卷积层的卷积核大小为 3 × 3，同时有 512 个卷积核。

因此，该卷积层的输出特征图大小和上一层的输入特征图大小相同，而输出特征图的通道数为 9 9 9。具体的特征图大小可以根据前一层的输出特征图大小和卷积核大小来计算。

这是 YOLOv5s 的整个 backbone，由 10 层网络组成。下面是各层的具体说明：

``` YOLOv5s backbone
[[-1, 1, Conv, [64, 6, 2, 2]],  # 0-P1/2
   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
   [-1, 3, C3, [128]],
   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
   [-1, 6, C3, [256]],
   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
   [-1, 9, C3, [512]],
   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
   [-1, 3, C3, [1024]],
   [-1, 1, SPPF, [1024, 5]],  # 9
  ]
```

- 第一层是一个卷积层，输出通道数为 64，卷积核大小为 6x6，步长为 2，填充为 2，输出特征图大小为输入的一半。
- 第二层是一个卷积层，输出通道数为 128，卷积核大小为 3x3，步长为 2，输出特征图大小为输入的一半。
- 第三层是一个 C3 模块，包含 3 个卷积层，每个卷积层的输出通道数为 128，卷积核大小分别为 1x1、3x3、1x1，不改变特征图大小。
- 第四层是一个卷积层，输出通道数为 256，卷积核大小为 3x3，步长为 2，输出特征图大小为输入的一半。
- 第五层是一个 C3 模块，包含 6 个卷积层，每个卷积层的输出通道数为 256，卷积核大小分别为 1x1、3x3、1x1，不改变特征图大小。
- 第六层是一个卷积层，输出通道数为 512，卷积核大小为 3x3，步长为 2，输出特征图大小为输入的一半。
- 第七层是一个 C3 模块，包含 9 个卷积层，每个卷积层的输出通道数为 512，卷积核大小分别为 1x1、3x3、1x1，不改变特征图大小。
- 第八层是一个卷积层，输出通道数为 1024，卷积核大小为 3x3，步长为 2，输出特征图大小为输入的一半。
- 第九层是一个 C3 模块，包含 3 个卷积层，每个卷积层的输出通道数为 1024，卷积核大小分别为 1x1、3x3、1x1，不改变特征图大小。
- 第十层是一个 SPPF 层，具有金字塔式空间池化（Spatial Pyramid Pooling），输出通道数为 1024，使用大小为 5x5 的金字塔空间池化。

总的来说，YOLOv5s 的 backbone 采用了一系列的卷积层和 C3 模块，不断缩小特征图的尺寸和增加通道数，最后通过 SPPF 层得到一个 1x1x1024 的张量，再通过若干个全连接层和激活函数得到预测框的位置和类别。。

### 卷积核大小为什么分别是1x1、3x3、1x1？

这种卷积核大小的结构被称为卷积块(Convolutional Block)，它由三个不同大小的卷积核组成，分别为1x1、3x3、1x1。这种结构可以有效地提高模型的非线性拟合能力和特征表达能力，具有一定的优势。

其中，第一个1x1卷积层主要用于降低输入特征图的通道数，以减少计算量和参数数量，同时可以通过学习权重进行特征压缩，提高模型的表达能力；第二个3x3卷积层用于对特征进行空间卷积，增强特征表达能力；第三个1x1卷积层则用于恢复特征的通道数，同时可以将不同通道的特征进行组合，提高模型的表达能力。

这种结构被广泛应用于深度神经网络中，如ResNet、DenseNet等。

### 使用大小为 5x5 的金字塔空间池化有什么用

金字塔空间池化（pyramid spatial pooling）是一种多尺度池化技术，它可以用来提取图像特征。使用大小为5x5的金字塔空间池化可以从多个尺度下获取图像的特征信息，并且可以减少特征的尺寸，从而减少模型的参数数量和计算量。

具体来说，使用大小为5x5的金字塔空间池化可以将输入图像分别进行多次池化，每次池化的窗口大小分别为5x5、4x4、3x3、2x2和1x1。这样可以得到多个不同尺度的池化特征图。这些特征图可以被组合成一个多通道的特征图，用于后续的分类或检测任务。

金字塔空间池化可以提高模型对于不同尺度目标的感知能力，从而提高模型的性能。此外，金字塔空间池化可以在不增加模型复杂度的情况下提高模型的准确率。

### 从C3模块输入和输出的图像大小区别

在 YOLOv5 中，C3 模块是一个由 3 个卷积层组成的卷积块，其中第 1 和第 2 个卷积层的步幅为 2，会将输入的特征图大小减半，而第 3 个卷积层的步幅为 1，不会改变输入的特征图大小。因此，C3 模块的输出特征图大小为输入特征图大小的一半。

具体来说，如果输入的特征图大小为 H × W，那么经过 C3 模块之后的输出特征图大小为 ⌊ H 2 ⌋ × ⌊ W 2 ⌋ × C，其中 C 是卷积核的数量，通常为 512。

例如，在 YOLOv5 中，默认的输入图像大小为 640x640，经过 C3 模块之后，输出特征图大小为 320x320x512。

需要注意的是，在 YOLOv5 中，还有其他模块也会对特征图大小进行改变，例如 SPP 模块和 PANet 模块。因此，在理解 YOLOv5 的特征图处理流程时，需要考虑多个模块的影响。

## 使用预训练模型进行推理

| 列名 | 解释 |
|---|---|
| Model | 模型的名称 |
| size(pixels) | 输入图像的大小（以像素为单位） |
| mAPval0.5:0.95 | 在验证集上的平均精确度（mean Average Precision），考虑所有IOU阈值从0.5到0.95的情况，准确率是% |
| mAPval0.5 | 在验证集上的平均精确度，只考虑IOU阈值为0.5的情况 |
| Speed CPU b1(ms) | 在CPU上使用batch size为1时的推理速度（以毫秒为单位） |
| Speed V100 b1(ms) | 在NVIDIA V100 GPU上使用batch size为1时的推理速度（以毫秒为单位） |
| Speed V100 b32(ms) | 在NVIDIA V100 GPU上使用batch size为32时的推理速度（以毫秒为单位） |
| params (M) | 模型的参数量（以百万为单位） |
| FLOPs @640 (B) | 在输入图像大小为640时，模型的浮点运算次数（以十亿为单位） |

| 模型 | 尺寸（像素） | mAPval 50-95 | mAPval 50  | 推理速度CPU b1（ms） | 参数量(M) | FLOPs@640 (B) |
|---|---|---|---|---|---|---|
| YOLOv5n | 640 | 27.7 | 45.6 | 7.9 | 1.9 | 4.5 |
| YOLOv5s | 640 | 37.1 | 56.6 | 7.7 | 7.2 | 16.5 |
| YOLOv5m | 640 | 44.9 | 63.8 | 9.7 | 21.2 | 49.0 |
| YOLOv5l | 640 | 48.6 | 60.9 | 12 | 46.5 | 109.1 |
| YOLOv5x | 640 | 50.3 | 62.6 | 21.2 | 86.7 | 205.7 |

## 分类模型

| 列名 | 解释 |
|---|---|
| Model | 模型的名称 |
| size(pixels) | 输入图像的大小（以像素为单位） |
| acc top1 | top1准确率，即（所有测试图片中正确标签包含在最大分类概率中的个数）除以（总的测试图片数） |
| acc top5 | top5准确率，即（所有测试图片中正确标签包含在前五个分类概率中的个数）除以（总的测试图片数） |
| Speed ONNX CPU(ms) | 在CPU上使用batch size为1时的推理速度（以毫秒为单位） |
| Speed TensorRT V100(ms) | 在NVIDIA V100 GPU上使用batch size为1时的推理速度（以毫秒为单位） |
| params (M) | 模型的参数量（以百万为单位） |
| FLOPs @640 (B) | 在输入图像大小为640时，模型的浮点运算次数（以十亿为单位） |

| 模型 | 尺寸（像素） | acc top1 | acc top2 | 推理速度 RTX 3060 Laptop GPU（ms） | 参数量(M) | FLOPs@640 (B) |
|---|---|---|---|---|---|---|
| YOLOv5n | 640 | 64.6 | 85.4 | 5.3 | 2.4 | 3.9GFLOPs |
| YOLOv5s | 640 | 71.5 | 90.2 | 5.3 | 5.4 | 11.4GFLOPs |


## 分割模型

```
PS C:\MyProgram\Code\MyCode\MiBootcamp\Yolov5Demo\yolov5> python segment/val.py --data coco.yaml --weights yolov5s-seg.pt --batch 1                            
segment\val: data=C:\MyProgram\Code\MyCode\MiBootcamp\Yolov5Demo\yolov5\data\coco.yaml, weights=['yolov5s-seg.pt'], batch_size=1, imgsz=640, conf_thres=0.001, iou_thres=0.6, max_det=300, task=val, device=, workers=8, single_cls=False, augment=False, verbose=False, save_txt=False, save_hybrid=False, save_conf=False, save_json=False, project=runs\val-seg, name=exp, exist_ok=False, half=False, dnn=False     
YOLOv5  v7.0-331-gab364c98 Python-3.9.13 torch-2.0.0+cu117 CUDA:0 (NVIDIA GeForce RTX 3060 Laptop GPU, 6144MiB)

Fusing layers... 
YOLOv5s-seg summary: 224 layers, 7611485 parameters, 0 gradients, 26.4 GFLOPs
val: Scanning C:\MyProgram\Code\MyCode\MiBootcamp\Yolov5Demo\datasets\coco\val2017.cache... 4952 images, 48 backgrounds, 0 corrupt: 100%|██████████| 5000/5000 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95): 100%|██████████| 5000/5000 [02:27<00:00, 33.93it/s]
                   all       5000      36335          0          0          0          0          0          0          0          0
Speed: 1.0ms pre-process, 8.9ms inference, 1.8ms NMS per image at shape (1, 3, 640, 640)
Results saved to runs\val-seg\exp6
```