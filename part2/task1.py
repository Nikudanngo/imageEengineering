import cv2

# cv2.blurする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_blur = cv2.blur(img_benitengu, (3, 3))

cv2.imwrite("img/blur_benitengu.jpg", img_benitengu_blur)

# # cv2.GaussianBlurする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_GaussianBlur = cv2.GaussianBlur(img_benitengu, (11, 11), 1)

cv2.imwrite("img/GaussianBlur_benitengu.jpg", img_benitengu_GaussianBlur)


# # cv2.bilateralFilterする
img_benitengu = cv2.imread("img/input.jpg")
img_benitengu_bilateralFilter = cv2.bilateralFilter(img_benitengu,12, 12, 1)

cv2.imwrite("img/bilateralFilter_benitengu.jpg", img_benitengu_bilateralFilter)

# 上記では三つの平滑化処理を行ったが,それぞれの特徴を考察する。

# cv2.blurは三つの平滑化の中で最も均等にぼかすことができるフィルターであると考えられる。

# cv2.GaussianBlurは中心から外側に向かってぼかすことができるフィルターであると考えられる。


# cv2.bilateralFilterは色の近い画素同士をぼかすことができるフィルターであると考えられる。
# つまり、エッジをキープしたままぼかすことができる。
# さらに、フィルターをかける前とかけた後で画像のサイズを比較したとこと、
# かけた後の画像のサイズがかける前の画像のサイズよりも大きくなっていることがわかった。

