import cv2
import numpy as np
img1_src = cv2.imread('img/dog.jpg', 0)

value = 150

img_src = img1_src.copy()

img_src[img1_src < value] = 0
img_src[img1_src >= value] = 255

#cv2_imshow(img_src)

img_tmp = cv2.Sobel(img_src, cv2.CV_32F, 1, 0, 3)
img_dst = cv2.convertScaleAbs(img_tmp)

element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8) # 4 近傍
element8 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8) # 8 近傍
n = 25

img_dst = cv2.erode(img_src, element4, iterations = 1)
#img_dst = cv2.dilate(img_src, element8, iterations = 1)

for i in range(n):
  img_dst = cv2.dilate(img_dst, element4, iterations = 1)
for i in range(n):
  img_dst = cv2.erode(img_dst, element8, iterations = 1)

cv2.imwrite('img/answer_3.jpg', img_dst)