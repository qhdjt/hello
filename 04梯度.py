import cv2
import numpy as np


class ImageProcessor:
    def __init__(self, win_name, orginal_path):
        self.winName = win_name
        self.gradient = None
        self.eroded = None
        self.dilated = None
        self.trackbarName = "kernelSize"
        self.orginal = cv2.imread(orginal_path, cv2.IMREAD_GRAYSCALE)
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.createTrackbar(self.trackbarName, win_name, 1, 23, self.update)

    def getBothPadding(self):
        # 随机灰度
        return np.full((self.orginal.shape[0], 10), fill_value=(np.random.randint(0, 255)), dtype=np.uint8)

    def update(self, var=1):
        kernelSize: int = max(cv2.getTrackbarPos(self.trackbarName, self.winName), 1)
        kernel = np.ones((kernelSize, kernelSize), np.uint8)
        self.dilated = cv2.dilate(self.orginal, kernel)
        self.eroded = cv2.erode(self.orginal, kernel)
        self.gradient = cv2.morphologyEx(self.orginal, cv2.MORPH_GRADIENT, kernel)
        images_combined = np.hstack((self.orginal, self.getBothPadding(),
                                     self.dilated, self.getBothPadding(),
                                     self.eroded, self.getBothPadding(),
                                     self.gradient))
        cv2.imshow(self.winName, images_combined)

    def run(self):
        self.update()
        k = cv2.waitKey(0) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()


if __name__ == '__main__':
    ImageProcessor("www", "./img/blurCat.png").run()
