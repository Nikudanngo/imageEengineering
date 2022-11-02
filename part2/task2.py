import cv2

# 1枚のカラー画像を入力(input.jpg)として,まずグレース
# ケール画像に変換し,その後Sobelフィルタで横エッジを検
# 出するプログラムを作成しなさい.

img_benitengu = cv2.imread("img/input.jpg",0)
img_benitengu_sobel = cv2.Sobel(img_benitengu, cv2.CV_32F, 1, 0, 3)
cv2.imwrite("img/sobel_benitengu.jpg", img_benitengu_sobel)

img_benitengu_convertScaleAbs = cv2.convertScaleAbs(img_benitengu_sobel, alpha=1, beta=1.0)
cv2.imwrite("img/convertScaleAbs_benitengu.jpg", img_benitengu_convertScaleAbs)

# SobelフィルタとconvertScaleAbsを使うことでどのよな結果が得られるか考察する
# convertScaleAbsは画像のコントラストを調整する関数である。
# 第二引数にalphaを設定することで、コントラスト変更のパラーメータとして調整することができる。
# SobelフィルタとconvertScaleAbsを使うことで、エッジを検出し、コントラストを上げることで
# エッジを強調することができる。

