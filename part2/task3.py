import cv2
import numpy as np
dogImage = cv2.imread('img/dog.jpg', 0)

value = 150

dogCopyImage = dogImage.copy()

dogCopyImage[dogImage < value] = 0
dogCopyImage[dogImage >= value] = 255

toThreshold = cv2.threshold(dogImage, 200, 255, cv2.THRESH_BINARY)[1]

element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
element8 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)

toErode = cv2.erode(toThreshold, element4, iterations = 2)
# toDilate = cv2.dilate(toThreshold, element8, iterations = 2)


toDilate = cv2.dilate(toErode, element4, iterations = 1)
# toErode = cv2.erode(toDilate, element8, iterations = 1)

cv2.imwrite('img/answer_3.jpg', toDilate)

# ここでは、Sobelフィルタを使ってエッジを検出し、convertScaleAbsでコントラストを上げることで
# エッジを強調している。さらに、膨張処理または収縮処理を行うことで犬全体の輪郭を切り抜くような処理をおこなっている。
# ここでは犬を綺麗に形どるために精密な切り取りを行うために第四近傍を用いる。
# 今回では、n=2としている。iterationsで繰り返しおこなう回数を設定することができる。
# また綺麗に形どるために、膨張処理を行った後に収縮処理を行うことで、犬の輪郭を切り抜いている。
