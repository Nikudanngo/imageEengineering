import cv2

# cv2.blurする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_blur = cv2.blur(img_benitengu, (5, 5))

cv2.imwrite("img/blur_benitengu.jpg", img_benitengu_blur)

# # cv2.GaussianBlurする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_GaussianBlur = cv2.GaussianBlur(img_benitengu, (5, 5), 0)

cv2.imwrite("img/GaussianBlur_benitengu.jpg", img_benitengu_GaussianBlur)


# # cv2.bilateralFilterする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_bilateralFilter = cv2.bilateralFilter(img_benitengu, 9, 75, 75)

cv2.imwrite("img/bilateralFilter_benitengu.jpg", img_benitengu_bilateralFilter)
