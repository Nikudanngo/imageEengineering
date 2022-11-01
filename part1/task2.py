import cv2

img_src = cv2.imread('sampleimage_1.jpg')
img_dst = img_src.copy()

height = img_src.shape[0]
width = img_src.shape[1]

for y in range(height):
    for x in range(width):
        img_dst[y][x] = [img_src[y, x, 1], img_src[y, x, 0], img_src[y, x, 2]]

cv2.imwrite('dst2.jpg', img_dst)