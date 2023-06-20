
import os
import torch
from PIL import Image
import numpy as np

# 定义颜色映射表
PALETTE = np.array([[120, 120, 120], [180, 120, 120], [6, 230, 230], [80, 50, 50],
           [4, 200, 3], [120, 120, 80], [140, 140, 140], [204, 5, 255],
           [230, 230, 230], [4, 250, 7], [224, 5, 255], [235, 255, 7],
           [150, 5, 61], [120, 120, 70], [8, 255, 51], [255, 6, 82],
           [143, 255, 140], [204, 255, 4], [255, 51, 7], [204, 70, 3],
           [0, 102, 200], [61, 230, 250], [255, 6, 51], [11, 102, 255],
           [255, 7, 71], [255, 9, 224], [9, 7, 230], [220, 220, 220],
           [255, 9, 92], [112, 9, 255], [8, 255, 214], [7, 255, 224],
           [255, 184, 6], [10, 255, 71], [255, 41, 10], [7, 255, 255],
           [224, 255, 8], [102, 8, 255], [255, 61, 6]], dtype=np.uint8)

# 遍历指定目录下的所有PNG文件
for filename in os.listdir('./labels'):
    if filename.endswith('.png'):
        # 读取PNG文件并将像素值转换为类别标签
        label = np.array(Image.open(os.path.join('./labels', filename)))
        label = torch.from_numpy(label)

        # 将类别标签映射成颜色值
        max_label = label.max()
        if max_label >= len(PALETTE):
            # 如果类别标签的最大值超过了PALETTE的长度，将超出部分映射成默认的背景颜色
            colors = np.array(np.vstack([PALETTE, [0, 0, 0]] * (max_label + 1 - len(PALETTE))), dtype=np.uint8)[label]
        else:
            colors = np.array(PALETTE, dtype=np.uint8)[:max_label+1][label]

        # 将numpy数组转换为PIL图像，并保存为文件
        img = Image.fromarray(colors)
        img.save(os.path.join('./labels_colors', filename))
