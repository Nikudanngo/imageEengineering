import cv2

# 1枚のカラー画像を入力(input.jpg)として,まずグレース
# ケール画像に変換し,その後Sobelフィルタで横エッジを検
# 出するプログラムを作成しなさい.

img_benitengu = cv2.imread("img/input.jpg",0)
img_benitengu_sobel = cv2.Sobel(img_benitengu, cv2.CV_32F, 1, 0, 3)
img_benitengu_convertScaleAbs = cv2.convertScaleAbs(img_benitengu_sobel)

cv2.imwrite("img/sobel_benitengu.jpg", img_benitengu_sobel)
cv2.imwrite("img/convertScaleAbs_benitengu.jpg", img_benitengu_convertScaleAbs)
