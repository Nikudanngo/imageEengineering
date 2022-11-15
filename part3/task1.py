# from google.colab.patches import cv2_imshowy
import cv2
import numpy as np

img_1 = cv2.imread('kadai-3/alfa_1.jpg')
img_2 = cv2.imread('kadai-3/alfa_2.jpg')
img_dst = img_1.copy()
height = img_1.shape[0]
width = img_1.shape[1]

for h in range(height):
    for w in range(width):
        alpha = w / width
        beta = 1 - alpha
        img_dst[h][w] = img_1[h][w] * beta + img_2[h][w] * alpha

# cv2_imshow(img_dst)
cv2.imwrite('kadai-3/alfa_3.jpg', img_dst)