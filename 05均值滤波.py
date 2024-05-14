import cv2
import numpy as np

origin = cv2.imread("img/blurCat.png",cv2.IMREAD_GRAYSCALE)
print(origin.shape)
win_name = 'Original & Blur'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
black_border = np.zeros((origin.shape[0], 12), dtype=np.uint8)

def update_blur(val):
    blur_size = max(val, 1)  # 确保blur_size至少为1
    blurred_img = cv2.blur(origin, (blur_size, blur_size))
    # 计算图像差分
    diff = cv2.absdiff( blurred_img,origin)
    _, binary_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    # 合并原图和滤波后的图
    images_combined = np.hstack((origin, black_border, blurred_img, black_border,diff,binary_diff))
    # 显示合并后的图像
    cv2.imshow(win_name, images_combined)

cv2.createTrackbar('blurWH', win_name, 1, 45, update_blur)


k = cv2.waitKey(0) & 0xFF
if k == ord('q') or k == 27:  # 27是ESC键的ASCII码
    cv2.destroyAllWindows()
pass
