import cv2
import numpy as np


class MorphologicalOperationsViewer:
    def __init__(self, image_path, window_name="Origin&Dilation&Erode", padding=5, initial_kernel_size=(1, 1)):
        self.origin = cv2.imread(image_path)
        self.kernel_w, self.kernel_h = initial_kernel_size
        self.both_padding = np.full((self.origin.shape[0], padding, 3), fill_value=(144, 23, 43), dtype=np.uint8)
        self.win_name = window_name
        cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
        cv2.createTrackbar('kernelW', self.win_name, 3, 21, lambda x: self.update_kernel_size(x, 'kernelW'))
        cv2.createTrackbar('kernelH', self.win_name, 3, 21, lambda x: self.update_kernel_size(x, 'kernelH'))
        self.update()

    def update(self):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.kernel_w, self.kernel_h))
        dilation = cv2.dilate(self.origin, kernel)
        erode = cv2.erode(self.origin, kernel)
        images_combined = np.hstack((self.origin, self.both_padding, dilation, self.both_padding, erode))
        cv2.imshow(self.win_name, images_combined)

    def update_kernel_size(self, value, trackbar_name):
        if trackbar_name == 'kernelW':
            self.kernel_w = max(value, 1)
        elif trackbar_name == 'kernelH':
            self.kernel_h = max(value, 1)
        self.update()

    def run(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    viewer = MorphologicalOperationsViewer("img/no.png")
    viewer.run()
