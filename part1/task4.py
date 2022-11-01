import cv2
import numpy as np

img_src = cv2.imread('input.jpg',0)
img_dst = img_src.copy()

min = 0 
max = 100

img_dst = cv2.equalizeHist(img_src)

cv2.imwrite('hist.jpg', img_dst)

table = np.arange(256, dtype = np.uint8)

for i in range( 0 , min ):
    table[i] = 0
for i in range( min , max ):
    table[i] = 255 * float( i - min ) / float( max - min )
for i in range( max , 255 ):
    table[i] = 255

img_dst = cv2.LUT(img_src, table)

cv2.imwrite('cont.jpg', img_dst)