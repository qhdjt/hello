import cv2
import numpy as np

origin = cv2.imread("img/binary.png", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Original & Binary', cv2.WINDOW_NORMAL)
cv2.createTrackbar('ThresholdValue', 'Original & Binary', 55, 255, lambda x: None)
while True:
    threshold = max(cv2.getTrackbarPos('ThresholdValue', 'Original & Binary'), 1)
    _, binary = cv2.threshold(origin, threshold, 255, cv2.THRESH_BINARY)
    images_combined = np.hstack((origin, binary))
    cv2.imshow('Original & Binary', images_combined)
    # 检查是否按下'q'键
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()
