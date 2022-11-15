# from google.colab.patches import cv2_imshow
import cv2
import numpy as np

back = cv2.imread('kadai-3/back.jpg')
img_1 = cv2.imread('kadai-3/fore1.jpg')
img_2 = cv2.imread('kadai-3/fore2.jpg')


def toMask(img):
    imgCatBackground = cv2.cvtColor(cv2.absdiff(img, back), cv2.COLOR_BGR2GRAY)
    # img_thresh = cv2.threshold(imgCatBackground, 15, 255, cv2.THRESH_BINARY)[1]
    # 二値化するときは、cv2.threshold()を使う
    imgBinary = cv2.threshold(imgCatBackground, 15, 255, cv2.THRESH_BINARY)[1]
    element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    imgErode = cv2.erode(imgBinary, element, iterations=1)
    imgDilate = cv2.dilate(imgErode, element, iterations=2)
    mask = cv2.bitwise_and(img, img, mask=imgDilate)
    return mask

cv2.imwrite('kadai-3/mask1.jpg', toMask(img_1))
cv2.imwrite('kadai-3/mask2.jpg', toMask(img_2))


# cv2_imshow(toMask(img_1))
# cv2_imshow(toMask(img_2))