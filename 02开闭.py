import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


class ImageProcessor:
    def __init__(self, origin_path):
        self.closed = None
        self.dilated = None
        self.opened = None
        self.eroded = None
        self.origin = cv2.imread(origin_path, cv2.IMREAD_GRAYSCALE)  # 确保图像是灰度图
        self.fig, self.axs = plt.subplots(nrows=2, ncols=3, figsize=(5, 5), )
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        self.fig.patch.set_facecolor(tuple(np.random.rand(3)))
        slider_height_ax = plt.axes((0.25, 0.05, 0.65, 0.03), facecolor='lightgoldenrodyellow')
        slider_width_ax = plt.axes((0.25, 0.1, 0.65, 0.03), facecolor='lightgoldenrodyellow')
        self.slider_height = Slider(slider_height_ax, 'Kernel Height', 1, 11, valinit=1, valstep=1)
        self.slider_width = Slider(slider_width_ax, 'Kernel Width', 1, 11, valinit=1, valstep=1)
        self.process_images(1, 1)
        self.put2axs(0, "原图", self.origin)
        self.put2axs(1, "腐蚀", self.eroded)
        self.put2axs(2, "开操作", self.opened)
        self.put2axs(3, "原图", self.origin)
        self.put2axs(4, "膨胀", self.dilated)
        self.put2axs(5, "闭", self.closed)
        self.slider_height.on_changed(self.update)
        self.slider_width.on_changed(self.update)
        plt.show()

    def put2axs(self, index, title: str, img, bgr2rgb=False):
        if isinstance(self.axs, np.ndarray):
            ax = self.axs.flatten()[index]
        else:
            ax = self.axs
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if bgr2rgb else img
        ax.imshow(img_rgb, cmap="gray")
        ax.set_title(title)
        ax.axis('off')

    def process_images(self, kernel_height, kernel_width):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_width, kernel_height))
        self.eroded = cv2.erode(self.origin, kernel)
        self.opened = cv2.morphologyEx(self.origin, cv2.MORPH_OPEN, kernel)
        self.dilated = cv2.dilate(self.origin, kernel)
        self.closed = cv2.morphologyEx(self.origin, cv2.MORPH_CLOSE, kernel)

    def update(self, val=1.0):
        plt.title(f"Kernel: ({self.slider_height.val}x{self.slider_width.val})")
        if self.slider_height.val != self.slider_height.valinit or self.slider_width.val != self.slider_width.valinit:
            self.slider_height.valinit = self.slider_height.val
            self.slider_width.valinit = self.slider_width.val
            self.process_images(self.slider_height.val, self.slider_width.val)
        self.put2axs(1, "腐蚀", self.eroded)
        self.put2axs(2, "开操作", self.opened)
        self.put2axs(4, "膨胀", self.dilated)
        self.put2axs(5, "闭", self.closed)
        self.fig.canvas.draw_idle()


processor = ImageProcessor('./img/no.png')
