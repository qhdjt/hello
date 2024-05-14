import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


class ImageProcessor:
    def __init__(self, origin_path):
        self.origin = cv2.imread(origin_path, cv2.IMREAD_GRAYSCALE)  # 确保图像是灰度图
        self.fig, self.axs = plt.subplots(nrows=1, ncols=3, figsize=(5, 5))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        self.fig.patch.set_facecolor(tuple(np.random.rand(3)))
        # 创建滑动条
        ax_slider = self.fig.add_axes([0.15, 0.05, 0.7, 0.03])  # [left, bottom, width, height]
        slider = Slider(ax_slider, 'Kernel Size', 1, 10, valstep=1, valinit=1)
        slider.on_changed(self.update)
        # 初始化
        # 显示初始图像
        self.put2axs(0, "原图", cv2.cvtColor(self.origin, cv2.COLOR_GRAY2RGB))
        self.put2axs(1, "Default", cv2.cvtColor(np.zeros_like(self.origin), cv2.COLOR_GRAY2RGB))  # 初始化空白图像
        self.put2axs(2, "Default", cv2.cvtColor(np.zeros_like(self.origin), cv2.COLOR_GRAY2RGB))  # 初始化空白图像
        plt.show()

    def put2axs(self, index, title: str, img, cmap="gray"):
        ax = self.axs.flatten()[index]
        ax.imshow(img, cmap=cmap)
        ax.set_title(title)
        ax.axis('off')

    def update(self, val=1.0):
        ksize = val if val % 2 == 1 else val + 1
        sobelx = cv2.Sobel(self.origin, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(self.origin, cv2.CV_64F, 0, 1, ksize=ksize)

        # 转换为uint8类型并计算绝对值
        sobely = cv2.convertScaleAbs(sobely)
        sobelx = cv2.convertScaleAbs(sobelx)
        self.put2axs(1, "sobely", sobely)
        self.put2axs(2, "sobelx", sobelx)


processor = ImageProcessor('./img/ddd.png')
