import cv2 
from google.colab.patches import cv2_imshow

img_src = cv2.imread('sampleimage_1.jpg')

for y in range(50):
    for x in range(100):
        img_src[100+y][100+x] = [255, 0, 0]

cv2.imwrite('dst1.jpg', img_src)
cv2_imshow(img_src)