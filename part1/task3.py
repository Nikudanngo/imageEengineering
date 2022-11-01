import cv2

img_src = cv2.imread('sampleimage_1.jpg')
img_dst = img_src.copy()

height = img_src.shape[0]
width = img_src.shape[1]
average = 0
for y in range(height):
    for x in range(width):
        average = (int(img_src[y,x, 0]) + int(img_src[y, x, 1]) + int(img_src[y, x, 2]))/3
        img_dst[y][x] = [0.55*average, 0.8*average, average]

cv2.imwrite('dst3.jpg', img_dst)